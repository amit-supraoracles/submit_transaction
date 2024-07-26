from dotenv import load_dotenv
import os
from web3 import Web3

load_dotenv()

rpc_url = os.getenv('LOCAL_NODE_URL')
web3 = Web3(Web3.HTTPProvider(rpc_url))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum node")

signed_payload = "SIGNED PAYLOAD HERE"
signed_tx = bytes.fromhex(signed_payload[2:])
txn_hash = web3.eth.send_raw_transaction(signed_tx)

print(f"Transaction hash: {txn_hash.hex()}")
