# opendata
Python client to manage Datawheel APIs

# Installing
`pip install opendata_rest`

For example, if you want to use DataChile API:

```
from opendata.datachile import DataChile

q = DataChile.get(
        "exports",
        {
            "drilldowns": [["Date","Year"]],
            "measures": ["FOB US"]
        }
    )

print(q)
```
