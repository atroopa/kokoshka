import mplfinance as mpf


class Theme:
    def __init__(self, theme):
        self.theme = theme
        
    def get_style(self):
        if self.theme == 'dark':
            # Define the color scheme for up and down candles
            market_colors = mpf.make_marketcolors(up='#26A69A', down='#EF5350')
            # Define the style with the custom market colors and background color
            mpf_style = mpf.make_mpf_style(marketcolors=market_colors, facecolor='#171B26')
        else:
            # Use the default style if the theme is not recognized
            mpf_style = None
        return mpf_style
