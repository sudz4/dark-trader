import requests
import pandas as pd
import math
import os
from dotenv import load_dotenv #pip3 install python-dotenv
load_dotenv()

iex_key = os.getenv("IEX_API_KEY")
ref_data_url = 'https://cloud.iexapis.com/stable/ref-data/symbols?token=' + iex_key
ref_data_response = requests.get(ref_data_url)
ref_data = ref_data_response.json()
screener_df = pd.DataFrame(ref_data)

# NYSE and NASDAQ symbols only (filter)
screener_df = screener_df[screener_df['exchange'].isin(['XNYS', 'XNAS'])]
# filter columns
screener_df = screener_df[['symbol', 'exchange', 'exchangeName']]
data_size = len(screener_df.index)
print(f"Data size: {data_size}") # get length of dataframe
print(screener_df.head())