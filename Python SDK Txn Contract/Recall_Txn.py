import json
import base64
from algosdk import algod
from algosdk import mnemonic
from algosdk.future.transaction import PaymentTxn
from Main import json_note


def send_note():
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    passphrase = "neglect struggle demand unfold knee salute mechanic enlist tray mind outside topple garage antique invest narrow gesture cat mouse solid slight myself favorite about raw"
    private_key = mnemonic.to_private_key(passphrase)
    my_address = mnemonic.to_public_key(passphrase)
    print(f'My address: {my_address}')
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = 1000
    note = json_note.encode()
    receiver = "WO4B3Z5M2NJOHCNAGVO6MAJ3KQFWHEBM5RY53ZTIAC2WSK5SJHP5LNYZQA"

    unsigned_txn = PaymentTxn(my_address, params, receiver, 100000, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)


send_note()
