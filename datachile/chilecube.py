from mondrian_rest import Cube, MondrianClient
from datachile import client
from .exception import InvalidParamException

API_BASE = "https://chilecube.datawheel.us"


class ChileCube(object):
    def __init__(self):
        self.client = MondrianClient(API_BASE)

    def get_cube(self, cube_id):
        cube = self.client.get_cube(cube_id)
        return {
            "name": cube.name,
            "dimensions": cube.dimensions,
            "measures": cube.measures,
            "annotations": cube.annotations
        }

    def get_cubes(self):
        return [{
            "name": cube.name,
            "dimensions": cube.dimensions,
            "measures": cube.measures,
            "annotations": cube.annotations
        } for cube in self.client.get_cubes()]

    def get_drilldowns(self, cube_id):
        cube = self.client.get_cube(cube_id)

        dd = []

        for dimension in cube.dimensions:
            for hierarchy in dimension["hierarchies"]:
                for level in hierarchy["levels"][1:]:
                    dd.append({
                        "dimension":
                        dimension["name"],
                        "hierarchy":
                        hierarchy["name"],
                        "level":
                        level["name"],
                        "drilldown":
                        [dimension["name"], hierarchy["name"], level["name"]],
                        "mdx": level["full_name"]
                    })

        return dd

    def get_measures(self, cube_id):
        cube = self.client.get_cube(cube_id)
        return [ms for ms in cube.measures]
    
    def get_members(self, cube_id, dimension, level):
        return self.client.get_members(cube_id, dimension, level)

    def get_regiones(self):
        return [{
            "region_id": comuna["key"],
            "region": comuna["name"]
        } for region in self.client.get_members(
            "exports", "Geography", "Region")["members"]]

    def get_comunas(self):
        return [{
            "comuna_id": comuna["key"],
            "comuna": comuna["name"],
            "region_id": comuna["ancestors"][0]["key"],
            "region": comuna["ancestors"][0]["name"]
        } for comuna in self.client.get_members(
            "exports", "Geography", "Comuna")["members"]]

    def get(self, cube_id, params={}, df=False, lang="en"):
        cube = self.client.get_cube(cube_id)

        if "drilldowns" not in params:
            raise InvalidParamException("At least one drilldown is missing")

        if "measures" not in params:
            raise InvalidParamException("At least one measure is missing")

        obj = {
            "caption":
            lang,
            "drilldown": [{
                "full_name": ".".join("[{}]".format(x) for x in dd)
            } for dd in params["drilldowns"]],
            "cut": [],
            "measures": [{
                "name": item
            } for item in params["measures"]]
        }

        if "cuts" in params:
            for cut in params["cuts"]:
                dd = ".".join("[{}]".format(x) for x in cut["drilldown"])
                output = []
                for value in cut["values"]:
                    output.append("{}.&[{}]".format(dd, value))
                output = ",".join(output)
                output = "{" + output + "}"
                obj["cut"].append(output)

        if "parents" in params:
            obj["parents"] = params["parents"]

        agg = self.client.get_aggregation(cube, obj)
        
        q = agg.tidy

        data = []
        n_axes = len(q["axes"])
        for item in q["data"]:
            obj = {}
            for i, dd in enumerate(q["axes"]):
                obj["ID " + dd["level"]] = int(item[i]["key"])
                obj[dd["level"]] = item[i]["caption"]
            for i, ms in enumerate(q["measures"]):
                obj[ms["caption"]] = item[n_axes + i] if item[n_axes
                                                              + i] else 0
            data.append(obj)

        q["data"] = data
        q["count"] = len(data)

        if df:
            from pandas import DataFrame
            return DataFrame(data=q["data"])

        return q

    def get_all(self, queries):
        merged = []
        n_queries = len(queries)

        q = {key: None for key in list(range(n_queries))}
        
        for key, query in enumerate(queries):
            q[key] = self.get( *query, df=False )
            merged += list(q[key]["data"][0].keys())

        unique_keys = list(
            set([x for x in merged if merged.count(x) > 1 and x[:3] == "ID "])
        )

        result = []

        def condition_generator(keys, item1, item2):
            for key in keys:
                if item1[key] != item2[key]:
                    return False
            
            return True

        i = 0
        for item1 in q[i]["data"]:
            for item2 in q[i + 1]["data"]:
                if condition_generator(unique_keys, item1, item2):
                    item = {**item1, **item2}
                    result.append(item)
                    break
        
        return result
