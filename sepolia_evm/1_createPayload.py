from dotenv import load_dotenv
import os
from web3 import Web3

load_dotenv()

infura_url =  os.getenv('SEPOLIA_INFURA_URL')
web3 = Web3(Web3.HTTPProvider(infura_url))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum node")

sender_address = os.getenv('SENDER_ADDRESS')
receiver_address = os.getenv('RECEIVER_ADDRESS')
sender_private_key = os.getenv('SENDER_PRIVATEKEY')


amount_in_wei = web3.toWei(0.1, 'ether')
nonce = web3.eth.getTransactionCount(sender_address)

transaction = {
    'nonce': nonce,
    'to': receiver_address,
    'value': amount_in_wei,
    'gas': 21000, 
    'gasPrice': web3.toWei('50', 'gwei'),  
    'chainId': int(os.getenv('SEPOLIA_CHAIN_ID')) 
}

signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)
signed_tx_payload = signed_txn.rawTransaction

print(f"Signed Transaction Payload: {signed_tx_payload.hex()}")
