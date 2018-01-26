from mondrian_rest import Cube, MondrianClient
from opendata_rest import client
import json

API_BASE = "http://chilecube.datawheel.us"


class DataChile(object):
    def __init__():
        return True

    def get(cube_id, params={}, format="json"):
        _client = MondrianClient(API_BASE)
        cube = _client.get_cube(cube_id)

        agg = _client.get_aggregation(
            cube, {
                "drilldown": [{
                    "full_name":
                    ".".join("[{}]".format(x) for x in dd)
                } for dd in params["drilldowns"]],
                "cut": [],
                "measures": [{
                    "name": item
                } for item in params["measures"]]
            })
        q = agg.tidy

        data = []
        n_axes = len(q["axes"])

        for item in q["data"]:
            obj = {}
            for i, dd in enumerate(q["axes"]):
                obj[dd["level"]] = item[i]["caption"]
            for i, ms in enumerate(q["measures"]):
                obj[ms["caption"]] = item[n_axes + i]
            data.append(obj)


        q["data"] = data
        p = json.dumps(q)
        return p
