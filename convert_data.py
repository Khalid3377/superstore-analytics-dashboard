import pandas as pd
import json

df = pd.read_excel('super.xls')
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.strftime('%Y-%m-%d')
df['Ship Date'] = pd.to_datetime(df['Ship Date']).dt.strftime('%Y-%m-%d')

cols = ['Row ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Segment', 'City', 'State', 'Region', 'Category', 'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit']
df = df[cols]

records = df.to_dict(orient='records')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('window.SUPERSTORE_DATA = ' + json.dumps(records) + ';')

print(f"Successfully exported {len(records)} records to data.js")
