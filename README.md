# opendata
OpenData is a Python 3 library to access the DataChile API. This library enables you to use public data from differents sources in your Python applications.

# Install
`pip install datachile`

# Simple Demo
```
from datachile import ChileCube

q = ChileCube.get(
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
        }
    )

print(q)
```
# Documentation
More information will be found on the DataChile documentation site on March, 3th.

## DataChile
This is a global class, and connect with DataChile website data.

### DataChile.get(cube, params, sort=False, format="json")
Load data from the server using a `requests` and `mondrian_rest`.

# Development

## Contributing
Long-term discussion and bug reports are maintained via GitHub Issues. Code review is done via GitHub Pull Requests.