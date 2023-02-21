import requests
import pandas as pd
import mplfinance as mpf

# Set the Binance API endpoint
url = 'https://api.binance.com/api/v1/klines'

# Set the parameters to retrieve the BTCUSDT data from Binance
params = {
    'symbol': 'BTCUSDT',
    'interval': '1d',
    'limit': 1000
}

# Retrieve the data from Binance
response = requests.get(url, params=params)
data = response.json()

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])

# Convert the data to the appropriate data types
df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
df[['Open', 'High', 'Low', 'Close', 'Volume', 'Quote asset volume', 'Taker buy base asset volume', 'Taker buy quote asset volume']] = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Quote asset volume', 'Taker buy base asset volume', 'Taker buy quote asset volume']].astype(float)

# Set the index to be the datetime column
df.set_index('Open time', inplace=True)

# Define the color scheme for up and down candles
up = '#26A69A'  # green
down = '#EF5350'  # red
market_colors = mpf.make_marketcolors(up=up, down=down)

# Define the style with the custom market colors and a dark background
mpf_style = mpf.make_mpf_style(marketcolors=market_colors, facecolor='#171B26')

# Plot the data using Matplotlib Finance
mpf.plot(df, type='candle', title='BTCUSDT', ylabel='Price (USDT)', volume=True, style=mpf_style)
