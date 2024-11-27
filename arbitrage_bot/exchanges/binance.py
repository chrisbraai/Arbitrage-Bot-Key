# exchanges/binance.py

def get_binance_data():
    """
    Simulates fetching market data from Binance.
    Returns mock data.
    """
    mock_binance_data = {
        'BTC/USDT': {'ask': 50500, 'bid': 50450},
        'ETH/USDT': {'ask': 4050, 'bid': 4040}
    }
    return mock_binance_data
