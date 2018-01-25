from opendata.datachile import DataChile

q = DataChile.get(
        "exports",
        {
            "drilldowns": [["Date","Year"]],
            "measures": ["FOB US"]
        }
    )

print(q)