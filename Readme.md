
## Transfer Sepolia Faucet

### Install necessary dependencies: 
```
pip install web3 python-dotenv
```


- ### Step 1: Create Signed Transaction

```
python3 sepolia_evm/1_createPayload.py
```

 ## NOTE: Make sure to place the OUTPUT (signed payload) against `signed_payload`


- ### Step 2: Submit Sepolia Signed Transaction

```
python3 sepolia_evm/2_submit.py
```
<br> <br>

## Transfer Supra-EVM Faucet 

- ### Step 1: Create Signed Transaction

```
python3 supra_evm/1_createPayload.py
```
## NOTE: Make sure to place the OUTPUT (signed payload) against `signed_payload`

- ### Step 2: Submit Sepolia Signed Transaction

```
python3 supra_evm/2_submit.py
```
