from datachile import ChileCube

client = ChileCube()

x = client.get_all([ 
    [
        "casen_household", 
        {
            "drilldowns": [
                ["Geography", "Geography", "Region"],
                ["Walls Material", "Walls Material", "Walls Material"]
            ],
            "measures": ["Expansion Factor Comuna"]
        }
    ],
    [   
        "crimes", 
        {
            "drilldowns": [
                ["Geography", "Geography", "Region"],
                ["Crime", "Crime", "Crime Group"]
            ],
            "measures": ["Number of records"]
        }
    ]
])

print(x)

'''from json import dumps
file = open("data.json", "w")
file.write(dumps(query1["data"]))
file.close()'''