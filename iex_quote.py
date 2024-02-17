import requests
import pandas as pd
import math
import os

import main.ipynb

# batch size
batch_size = 100
total_batches = math.ceil(len(screener_df) / batch_size)
print(f"Total batches: {total_batches}")

# initialize a list to story data
quote_data_list = []

def fetch_quote_data(symbols_batch, iex_key):
    symbols_str = ','.join(symbols_batch)
    url = f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={symbols_str}&types=quote&token={iex_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}
    
# initialize a counter for completed batches
completed_batches = 0

# define the length of the progress bar
progress_bar_length = 50

"""scalable endpoint variable data request"""
for i in range(0, len(screener_df), batch_size):
    batch_symbols = screener_df['symbol'].iloc[i:i+batch_size].tolist()
    batch_data = fetch_quote_data(batch_symbols, iex_key)
    
    # process and append data for each symbol in the batch
    for symbol in batch_symbols:
        quote_data = batch_data.get(symbol, {}).get('quote', {})
        quote_data_list.append({
            'symbol': symbol, # KEY
            'latestPrice': quote_data.get('latestPrice', None),
            'previousClose': quote_data.get('previousClose', None), # PREV DAY CLOSE
            'extendedPrice': quote_data.get('extendedPrice', None), # EXTENDED HOURS PRICE
            'extendedChangePercent': quote_data.get('extendedChangePercent', None), # EXTENDED HOURS CHANGE
            'extendedPriceTime': quote_data.get('extendedPriceTime', None), # EXTENDED HOURS PRICE TIME
            'latestVolume': quote_data.get('latestVolume', None), # LATEST VOLUME
            'companyName': quote_data.get('companyName', None) # COMPANY NAME
        })
    
    # increment completed batches counter
    completed_batches += 1

    # calculate progress
    progress = (completed_batches / total_batches)
    filled_length = int(round(progress_bar_length * progress))
    
    # create progress bar
    bar = '█' * filled_length + '-' * (progress_bar_length - filled_length)
    
    # print progress bar with percentage
    print(f"\rProgress: |{bar}| {progress*100:.2f}% Complete", end="\r")

# Convert the combined data into a DataFrame
quote_df = pd.DataFrame(quote_data_list)