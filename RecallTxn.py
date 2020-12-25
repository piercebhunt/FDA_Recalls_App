import json
import base64
import requests
from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk.future.transaction import PaymentTxn

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


def parse_into_json():
    # dates (YYYYMMDD) and recall type(food, device, drug)
    date1 = 20201201
    date2 = 20201225
    recall_type = "food"

    url = "https://api.fda.gov/" + recall_type + \
        f'/enforcement.json?search=report_date:[{date1}+TO+{date2}]&limit='

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    # find total results by extracting meta results total
    meta_total_dict = parsed["meta"]["results"]["total"]
    meta_total_json = json.dumps(meta_total_dict)

    url_Number = (meta_total_json)

    # produce new url with updated total
    new_url = url + url_Number

    # Update parse with new URL that matches total results
    upd_response = requests.get(new_url)
    upd_data = upd_response.text
    upd_parsed = json.loads(upd_data)
    results_only = upd_parsed["results"]

    # declare which keys to remove to keep data under 1KB
    remove = ('event_id', 'openfda', 'initial_firm_notification', 'address_2')

    # use for loop to remove elements to keep data under 1KB
    for element in results_only:
        for k in remove:
            element.pop(k, None)

    # find number of results with index starting at 0
    parse_final_value = int(url_Number) - 1

    # Add prefix FDA Food to specified set of results, 0 to parse_final_value
    results_location = 0
    result = results_only[results_location]

    json_note = json.dumps(result)
    json_note = "FDAF" + json_note
    return json_note


def send_note():
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    passphrase = "primary one hero whisper enhance egg screen zebra air zebra talent unveil cart pluck ski cube huge leg equal treat enhance resource nut ability shrug"
    private_key = mnemonic.to_private_key(passphrase)
    my_address = mnemonic.to_public_key(passphrase)
    print(f'My address: {my_address}')
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = 1000
    json_note = parse_into_json()
    note = json_note.encode()
    receiver = "25VPK5YXDPWQGVPC5JL5X32UWUQFZIIMMPISZ7Y3GYXXDKFO7TSY4CMNCY"

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
    # fda_dict = json.loads(base64.b64decode(
    # confirmed_txn["txn"]["txn"]["note"]).decode())
    #print("FDA Recall = {}".format(fda_dict["FDA"]))


send_note()
