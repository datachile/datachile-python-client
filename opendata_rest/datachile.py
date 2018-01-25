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
                    "full_name": ".".join("[{}]".format(x) for x in dd)
                } for dd in params["drilldowns"]],
                "cut": [],
                "measures": [ {"name": item } for item in params["measures"] ]
            })
        p = json.dumps(agg.tidy)
        return p
