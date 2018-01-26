# opendata
Python client to manage Datawheel APIs

# Installing
`pip install opendata_rest`

For example, if you want to use DataChile API:

```
from opendata_rest.datachile import DataChile

q = DataChile.get(
        "exports", {
            "drilldowns": [["Date", "Year"],
                        ["Destination Country", "Country", "Continent"]],
            "measures": ["FOB US", "Geo Rank"]
        }, {"attrs":["FOB US", "Year"], "order": "ASC"})

print(q)
```
