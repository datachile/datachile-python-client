from mondrian_rest import Cube, MondrianClient
from datachile import client, download
import json

API_BASE = "https://chilecube.datawheel.us"

class ChileCube(object):
    def __init__(self):
        return True

    def get_cubes(self):
        _client = MondrianClient(API_BASE)
        return [{
            "dimensions": item.std_dimensions,
            "measures": item.measures_by_name
        } for item in _client.get_cubes()]

    def get_cube(self, cube_id):
        _client = MondrianClient(API_BASE)
        cube = _client.get_cube(cube_id)
        return {
            "dimensions": cube.std_dimensions,
            "measures": cube.measures_by_name
        }

    def get_measures(self, cube_id):
        _client = MondrianClient(API_BASE)
        cube = _client.get_cube(cube_id)
        return [ ms for key, ms in cube.measures_by_name.items() ] 

    def get_drilldowns(self, cube_id):
        _client = MondrianClient(API_BASE)
        cube = _client.get_cube(cube_id)
        
        dd = []

        for key, dimension in cube.std_dimensions.items():
            for hierarchy in dimension["hierarchies"]:
                for level in hierarchy["levels"][1:]:
                    dd.append({
                        "dimension": dimension["name"],
                        "hierarchy": hierarchy["name"],
                        "level": level["name"],
                        "drilldown": [
                            dimension["name"], 
                            hierarchy["name"], 
                            level["name"]
                        ]
                    })
        return dd

    def get_regiones(self):
        return [{
            "region_id": comuna["key"],
            "region": comuna["name"]
        } for region in MondrianClient(API_BASE).get_members(
            "exports", "Geography", "Region")["members"]]

    def get_comunas(self):
        return [{
            "comuna_id": comuna["key"],
            "comuna": comuna["name"],
            "region_id": comuna["ancestors"][0]["key"],
            "region": comuna["ancestors"][0]["name"]
        } for comuna in MondrianClient(API_BASE).get_members(
            "exports", "Geography", "Comuna")["members"]]

    def get_members(self, cube_id, dimension, level):
        return MondrianClient(API_BASE).get_members(cube_id, dimension, level)

    def get(self, cube_id, params={}, lang="en", sort=False, fm="json"):
        _client = MondrianClient(API_BASE)
        cube = _client.get_cube(cube_id)

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

        if params["cuts"]:
            for cut in params["cuts"]:
                dd = ".".join("[{}]".format(x) for x in cut["dimension"])
                output = []
                for value in cut["values"]:
                    output.append("{}.&[{}]".format(dd, value))
                output = ",".join(output)
                output = "{" + output + "}"
                obj["cut"].append(output)

        if params["parents"]:
            obj["parents"] = params["parents"]

        agg = _client.get_aggregation(cube, obj)
        q = agg.tidy

        data = []
        n_axes = len(q["axes"])
        import json
        for item in q["data"]:
            obj = {}
            for i, dd in enumerate(q["axes"]):
                obj[dd["level"]] = item[i]["caption"]
            for i, ms in enumerate(q["measures"]):
                obj[ms["caption"]] = item[n_axes + i] if item[n_axes
                                                              + i] else 0
            data.append(obj)

        q["data"] = data
        if sort:
            #print(q["data"].sort(key=lambda x: x["FOB US"]))
            q["data"].sort(
                key=lambda x: [x[attr] for attr in sort["attrs"]],
                reverse=(True if sort["order"] == "DESC" else False))

        if fm == "json":
            return q
        elif fm == "xml":
            return download.Download(q).xml
        elif fm == "csv":
            #print(download.Download(q).csv)
            return download.Download.csv(q, q)
