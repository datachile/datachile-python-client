# DataChile Python Client
`DataChile Python Client` is a Python 3 library to access the DataChile API. This library enables you to use public data from differents sources in your Python applications.

# Install
`pip install datachile`

# Simple Demo

* Get all datasets availables in DataChile

```
from datachile import ChileCube

client = ChileCube()
query = client.get_cubes()

print(query)
```

* Get drilldowns availables from "Election Participation" dataset.
```
from datachile import ChileCube

client = ChileCube()
cube = "election_participation"

dd = client.get_drilldowns(cube)
ms = client.get_measures(cube)

print(dd)
print(ms)
```

* Get exports from Chile in 2012-2014, divided in Year and Destination Country
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

# Documentation
Please refer to our Wiki documentation for more information or [Datachile API Documentation Website](https://datachile.io/about/api).

# Development

## Contributing
Long-term discussion and bug reports are maintained via GitHub Issues. Code review is done via GitHub Pull Requests. 

# License
The MIT License (MIT)

Copyright (c) 2018 Carlos Navarrete & Datawheel LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
