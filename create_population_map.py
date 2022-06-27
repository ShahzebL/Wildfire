import requests
# import pandas as pd

# df = pd.read_csv("us-county-boundaries.csv")
# df = pd.DataFrame(df, columns= ['Geo Shape'])
# print(df.columns)
# print(df)

import json

with open('us-county-boundaries.json') as f:
  data = json.load(f)[0]

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data['fields']['geo_shape']['coordinates'][0])