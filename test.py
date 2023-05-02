from bitcoinaddress import Wallet

def bitcoin_adress_generator() :
    private_key = '5KAVmfYtCvGcvv2PaKkKvpm16nMZbrrSzYVzuiPTi7fx5dVgyvc'
    if private_key : 
        wallet = Wallet(private_key)
    else : 
        wallet = Wallet()

    return(wallet.key.__dict__['seed'].__str__(),
           wallet.address.__dict__['key'].__str__(),
           wallet.address.__dict__['mainnet'].__dict__['pubaddr1'])
print(bitcoin_adress_generator())


'''
No, one private key cannot have multiple public keys in Bitcoin. In Bitcoin, each private key corresponds to one and only one public key, 
which in turn corresponds to one and only one Bitcoin address.
The relationship between a private key, a public key, and a Bitcoin address is one-to-one and cannot be changed.

Meaning that in my data  base if I use the same private key, i'll have the same public key but with a differents ID
'''

'''
Public Address 1 and Public Address 1 compressed: These are legacy Bitcoin addresses, also known as Pay-to-Public-Key-Hash (P2PKH) addresses, 
which are still widely used in the Bitcoin network. These addresses start with the number "1". 
They are derived from the public key and are generated using a cryptographic hash function.

Public Address 3: This is a legacy Bitcoin address, also known as Pay-to-Script-Hash (P2SH) address. It is used to send Bitcoin to a script, 
which can be a multi-signature address or a script that enables more advanced transaction types. This address starts with the number "3".

Public Address bc1 P2WPKH and Public Address bc1 P2WSH: These are newer Bitcoin addresses that are used in Segregated Witness (SegWit) transactions. 
SegWit is a protocol upgrade that improves the efficiency and security of the Bitcoin network. 
These addresses start with the prefix "bc1" and can be either Pay-to-Witness-Public-Key-Hash (P2WPKH) or Pay-to-Witness-Script-Hash (P2WSH) addresses.
'''