from datachile.chilecube import ChileCube

#, {
#        "attrs": ["FOB US", "Year"],
#        "order": "ASC"
#    }

q = ChileCube.get(
    "exports", 
    {
        "drilldowns": [
            ["Date", "Year"],
            ["Destination Country", "Country", "Country"]
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
    "es",
    False,
    "csv"
)

#q = DataChile.get_members("exports", "Destination Country", "Continent")

import json
print(json.dumps(q))