coin = 'BTC'
dic_coin_function = {
        'BTC' : lambda x : bitcoin_address_generator(x),
        'ETH' : lambda x : ETH_address_generator(x)
    }
if coin not in dic_coin_function.keys() :
  print("BTC")