class Theme:
    def __init__(self, facecolor, up_color, down_color):
        self.facecolor = facecolor
        self.up_color = up_color
        self.down_color = down_color
        
    def get_style(self):
        # Define the color scheme for up and down candles
        market_colors = mpf.make_marketcolors(up=self.up_color, down=self.down_color)
        # Define the style with the custom market colors and background color
        mpf_style = mpf.make_mpf_style(marketcolors=market_colors, facecolor=self.facecolor)
        return mpf_style

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

# Create a new instance of the Theme class with the desired colors
my_theme = Theme(facecolor='#171B26', up_color='#26A69A', down_color='#EF5350')

# Get the style object from the theme
my_style = my_theme.get_style()

# Plot the data using Matplotlib Finance and the custom style
mpf.plot(df, type='candle', title='BTCUSDT', ylabel='Price (USDT)', volume=True, style=my_style)
