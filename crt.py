import requests
import pandas as pd

# Ask user for query
query = input("Enter query: ")

# URL to query
url = f'https://crt.sh/?q={query}&output=json'

# Retrieve data
response = requests.get(url)
data = response.json()

# Create dataframe from data
df = pd.DataFrame(data)

# Create Excel writer
with pd.ExcelWriter('crtsh_data.xlsx') as writer:
    # Write dataframe to Excel sheet
    df.to_excel(writer, sheet_name='crtsh_data', index=False)
