# End-of-day Data
# * Intraday Data
# * Real-Time Updates
# * Historical Data
# * Real-time Stock Market Prices
# * Commodity Prices
# * Commodities History Prices
# * Company Ratings
# * Splits data
# * Dividends data
# * Tickers
# * Tickers List
# * Tickers Info
# * Stock Market Index List
# * Stock Market Index Info
# * Exchanges
# * Currencies
# * Timezones
# * Bonds List
# * Bonds Info
# * ETF Holdings List
# * ETF Holdings Info
# * ETF Holdings Timeframe


api_functions = {
    "End-of-day": {
        "endpoint": "eod",
        "required_params": ["symbols"],
    },
    "Intraday": {
        "endpoint": "",
        "required_params": ["symbol", "interval"],
        "default_params": {"datatype": "json"},
    },
    "Real-Time-Updates": {
        "endpoint": "",
        "required_params": ["symbol", "interval"],
        "default_params": {"datatype": "json"},
    },
}