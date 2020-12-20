import json
import base64
from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk.future.transaction import PaymentTxn
from Main import json_note

# utility for waiting on a transaction confirmation


def wait_for_confirmation(client, transaction_id, timeout):
    start_round = client.status()["last-round"] + 1
    current_round = start_round

    while current_round <= start_round + timeout:
        client.status_after_block(current_round)
        try:
            pending_txn = client.pending_transaction_info(transaction_id)
        except Exception:
            return
        if pending_txn.get("confirmed-round", 0) > 0:
            return pending_txn
        elif pending_txn["pool-error"]:
            raise Exception(
                'pool error: {}'.format(pending_txn["pool-error"]))
            current_round += 1
    raise Exception(
        'pending tx not found in timeout rounds, timeout value = : {}'.format(timeout))


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

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)
    # send transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Send transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    print("txID: {}".format(txid), "confirmed in round: {}".format(
        confirmed_txn.get("confirmed-round", 0)))
    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=2)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    fda_dict = json.loads(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode())
    print("FDA Recall = {}".format(fda_dict["FDA"]))


send_note()
