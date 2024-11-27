# exchanges/coinbase.py

def get_coinbase_data():
    """
    Simulates fetching market data from Coinbase.
    Returns mock data.
    """
    mock_coinbase_data = {
        'BTC/USDT': {'ask': 50600, 'bid': 50550},
        'ETH/USDT': {'ask': 4060, 'bid': 4055}
    }
    return mock_coinbase_data
