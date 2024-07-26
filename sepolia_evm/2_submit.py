from dotenv import load_dotenv
import os
from web3 import Web3

load_dotenv()

infura_url =  os.getenv('SEPOLIA_INFURA_URL')
web3 = Web3(Web3.HTTPProvider(infura_url))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum node")

signed_payload = "0xf87004850ba43b740082520894de1c4cf6e992748cf56481da68e43627bbc23cae88016345785d8a0000808401546d72a052147db1c4d55b0e00384c646b29f53e596d34aa141efc5a40e7a1f458ee49e1a010052e690ef516e248729d5219754ffb53b4a4b46d551daed5b2f6094a71240c"
signed_tx = bytes.fromhex(signed_payload[2:])
txn_hash = web3.eth.send_raw_transaction(signed_tx)

print(f"Transaction hash: {txn_hash.hex()}")
