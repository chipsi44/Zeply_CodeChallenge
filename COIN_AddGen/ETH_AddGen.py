from eth_account import Account
import secrets

def ETH_address_generator(private_key) :
    if  private_key :
        acct = Account.from_key(private_key)
        print("Address:", acct.address)
    else : 
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        print ("SAVE BUT DO NOT SHARE THIS:", private_key)
        acct = Account.from_key(private_key)
        print("Address:", acct.address)
        