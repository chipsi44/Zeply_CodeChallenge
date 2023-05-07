from bitcoinaddress import Wallet

def bitcoin_address_generator(private_key) :
    if private_key : 
        #create a bitcoin address with the wallet function and the private key
        wallet = Wallet(private_key)
        return_private_key = private_key
    else : 
        #create a bitcoin address and private key with the wallet function 
        wallet = Wallet()

        #The way the private key is delivered to us is a complete mess, so here is a bit of data refactoring
        generated_private_key = wallet.address.__dict__['key'].__str__().split("\n")
        generated_private_key = generated_private_key[1].split(" ")[-1]
        return_private_key = generated_private_key
    #return the seed, the private key and the public key
    return(wallet.key.__dict__['seed'].__str__(),
           return_private_key,
           wallet.address.__dict__['mainnet'].__dict__['pubaddr1'])