from opendata_rest.datachile import DataChile

q = DataChile.get(
    "exports", {
        "drilldowns": [["Date", "Year"],
                       ["Destination Country", "Country", "Continent"]],
        "measures": ["FOB US", "Geo Rank"],
        "cuts": [{
            "dimension": ["Date", "Year"],
            "values": [2012, 2014]
        }]
    }, {
        "attrs": ["FOB US", "Year"],
        "order": "ASC"
    })

import json
print(json.dumps(q))