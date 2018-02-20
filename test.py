from datachile import ChileCube

#, {
#        "attrs": ["FOB US", "Year"],
#        "order": "ASC"
#    }

#cubes = ChileCube.get_cubes()

import json
#print()
file = open("data.json", "w")
file.write(json.dumps(ChileCube.get_cubes()))
file.close()

'''q = ChileCube.get(
    "exports", 
    {
        "drilldowns": [
            ["Date", "Year"],
            ["Destination Country", "Country", "Country"]
        ],
        "measures": ["FOB US"],
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
    False
)
'''
#q = ChileCube.get_members("exports", "Destination Country", "Continent")

#import json
#print(json.dumps(q))