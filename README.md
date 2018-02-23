# opendata
OpenData is a Python 3 library to access the DataChile API. This library enables you to use public data from differents sources in your Python applications.

# Install
`pip install datachile`

# Simple Demo

Get exports from Chile in 2012-2014, divided in Year and Destination Country
```
from datachile import ChileCube

client = ChileCube()

query = client.get(
    "exports", 
    {
        "drilldowns": [
            ["Date", "Year"],
            ["Destination Country", "Country", "Country"]
        ],
        "measures": ["FOB US"],
        "cuts": [
            {
                "drilldown": ["Date", "Year"],
                "values": [2012, 2013, 2014]
            }
        ],
        "parents": True
    }
)

print(query)
```

Get all datasets availables in DataChile

```
from datachile import ChileCube

client = ChileCube()
query = client.get_cubes()

print(query)
```

Get drilldowns availables from "Election Participation" dataset.
```
from datachile import ChileCube

client = ChileCube()
cube = "election_participation"

dd = client.get_drilldowns(cube)
ms = client.get_measures(cube)

print(dd)
print(ms)
```
# Documentation
Please refer to our extensive Wiki documentation for more information.

## ChileCube
This is a global class, and connect with DataChile website data.

### ChileCube.get(cube, params, sort=False, format="json")
Load data from the server using a `requests` and `mondrian_rest`.

# Development

## Contributing
Long-term discussion and bug reports are maintained via GitHub Issues. Code review is done via GitHub Pull Requests.