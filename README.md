# opendata
OpenData is a Python (2 and 3) library to access the Datawheel APIs. This library enables you to use public data from differents sources in your Python applications.

# Install
`pip install opendata_rest`

# Simple Demo
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
# Documentation
More information will be found on the DataChile documentation site on March, 3th.

## DataChile
This is a global class, and connect with DataChile website data.

### DataChile.get(cube, params, sort=False, format="json")
Load data from the server using a `requests` and `mondrian_rest`.

# Development

## Contributing
Long-term discussion and bug reports are maintained via GitHub Issues. Code review is done via GitHub Pull Requests.