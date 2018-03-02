from datachile import ChileCube

client = ChileCube()

# Health System by Year and Region in 2014
query1 = client.get(
    "casen_health_system", 
    {
        "drilldowns": [
            ["Date", "Date", "Year"],
            ["Geography", "Geography", "Region"],
            ["Health System", "Health System", "Health System"]
        ],
        "measures": ["FOB US"],
        "cuts": [
            {
                "drilldown": ["Date", "Date", "Year"],
                "values": [2014]
            }
        ],
        "parents": True
    }
)

# Exports from Chile in 2012-2014, divided in Year and Destination Country
query2 = client.get(
    "exports", 
    {
        "drilldowns": [
            ["Date", "Date", "Year"],
            ["Destination Country", "Country", "Country"]
        ],
        "measures": ["FOB US"],
        "cuts": [
            {
                "drilldown": ["Date", "Date", "Year"],
                "values": [2012, 2013, 2014]
            }
        ],
        "parents": True
    }
)


print(query1)
print(query2)