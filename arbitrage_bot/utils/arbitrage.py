# utils/arbitrage.py

def find_arbitrage_opportunities(binance_data, coinbase_data):
    """
    Identifies arbitrage opportunities between Binance and Coinbase.
    """
    opportunities = []

    for pair in binance_data.keys():
        binance_ask = binance_data[pair]['ask']
        binance_bid = binance_data[pair]['bid']
        coinbase_ask = coinbase_data[pair]['ask']
        coinbase_bid = coinbase_data[pair]['bid']

        # Check for opportunities to buy on Binance and sell on Coinbase
        if binance_ask < coinbase_bid:
            profit = coinbase_bid - binance_ask
            opportunities.append({
                'pair': pair,
                'buy_exchange': 'Binance',
                'sell_exchange': 'Coinbase',
                'buy_price': binance_ask,
                'sell_price': coinbase_bid,
                'profit': profit
            })

        # Check for opportunities to buy on Coinbase and sell on Binance
        if coinbase_ask < binance_bid:
            profit = binance_bid - coinbase_ask
            opportunities.append({
                'pair': pair,
                'buy_exchange': 'Coinbase',
                'sell_exchange': 'Binance',
                'buy_price': coinbase_ask,
                'sell_price': binance_bid,
                'profit': profit
            })

    return opportunities
