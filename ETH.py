import web3

# Verbindung zum Ethereum-Netzwerk herstellen
w3 = web3.Web3(web3.Web3.HTTPProvider('https://mainnet.infura.io/v3/7687ba4d053b42819a88a2039d4a5bf5'))

# Wallet generieren
private_key = w3.eth.account.create().privateKey
address = w3.eth.account.privateKeyToAccount(private_key).address

# Balance abfragen
balance = w3.eth.getBalance(address)
balance_eth = w3.fromWei(balance, 'ether')

# In Euro umrechnen
eth_price = w3.eth.getEthPrice()
balance_euro = balance_eth * eth_price

# Ausgabe
print("Wallet-Adresse:", address)
print("ETH-Balance:", balance_eth)
print("Balance in Euro:", balance_euro)

while True:
    answer = input("Möchten Sie weitermachen? (j/n)")
    if answer == 'j':
        continue
    elif answer == 'n':
        break
    else:
        print("Ungültige Eingabe. Bitte 'j' oder 'n' eingeben.")
