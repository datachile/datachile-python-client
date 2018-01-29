from opendata_rest.datachile import DataChile
'''
, {
        "attrs": ["FOB US", "Year"],
        "order": "ASC"
    }

q = DataChile.get(
    "exports", 
    {
        "drilldowns": [
            ["Date", "Year"],
            ["Destination Country", "Country", "Continent"]
        ],
        "measures": ["FOB US", "Geo Rank"],
        "cuts": [
            {
                "dimension": ["Date", "Year"],
                "values": [2012, 2014]
            }, {
                "dimension": ["Export HS", "HS", "HS2"],
                "values": ["010103", "010203"]
            }
        ],
        "parents": True
    },
    "es"
)
'''
q = DataChile.get_members("exports", "Destination Country", "Continent")

import json
print(json.dumps(q))