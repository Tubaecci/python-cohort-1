from crypto_utils import wallet

my_wallet = wallet('Tobey')
my_wallet.deposit("ETH", 0.7)
print(my_wallet.view_balance())

#wallet = cryptowallet("Joseph")
#wallet.deposit('BTC', 0.1)
#wallet.deposit('ETH', 0.7)

#print(wallet.view_balance())