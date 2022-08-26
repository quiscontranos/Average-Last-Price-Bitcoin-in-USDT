import ccxt
ex_1=ccxt.binance({})
ex_2=ccxt.coinbasepro({})
def last_price_ex_1():
    price=float(ex_1.fetchTicker('BTC/USDT')['last'])
    print(price)
def last_price_ex_2():
    price=float(ex_2.fetchTicker('BTC/USDT')['last'])
    print(price)
def average_last_price_ex_all():
    price=float(((ex_1.fetchTicker('BTC/USDT')['last'])+(ex_2.fetchTicker('BTC/USDT')['last']))/2)
    print(price)

last_price_ex_1()
last_price_ex_2()
average_last_price_ex_all()