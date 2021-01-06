# **FDA Recalls App**

## Overview

The FDA has open-source APIs for food, device, and drug recalls. This application stores FDA recall data on Algorand’s blockchain by encoding the FDA’s API results in a transaction notefield. This application focuses on the dates of 12/01/20 to 12/02/20 for food recalls specifically. This application can encompass other date timelines and incorporate food, drug, or medical device recalls.

After the recall data is encoded and stored on Algorand, this application then indexes transactions with the recall data based on an specific, encoded prefix. In this application, the prefix 'FDAF' is used. 

By placing recall data on an immutable ledger such as Algorand, an environment of accountability and transparency is created between consumers, the FDA, and businesses. 


## Requirements

- Python 3.0 and/or above
- Algorand SDK module
- Requests Module
- Dockerized Sandbox environment

## Additional Resources of Use

- Read and Write to the Transaction Note Field with Python Algorand Tutorial | (https://developer.algorand.org/tutorials/v2-read-and-write-transaction-note-field-python/)

- Indexer Algorand Documentation Note Field Searching | (https://developer.algorand.org/docs/features/indexer/)

- Developer Office Hours | How to set up your Algorand Sandbox Environment | (https://www.youtube.com/watch?v=OOlUXonYTNA&t=714s) 

- Algorand Sandbox | 
  (https://github.com/algorand/sandbox)

## Set Up

### Step 1
1. Install `algosdk` module
2. Install `requests` module

### Step 2
1. Locate `parse_into_json()` function from `Main.py` file
2. Set `date1` to desired year, month and date as follows YYYYMMDD
3. Set `date2` to a later date with same format, YYYYMMDD
4. Set `recall_type` to either food, drug or device

### Step 3

1. Load Dockerized Sandbox Environment
2. run `./sandbox up nightly` in the command line of terminal from sandbox folder
3. Once sandbox nightly is loaded, find the three listed private accounts or run command `./sandbox goal account list`
4. Copy the first account address, which will resemble a 59 character address like `VAJPCCDYERNMNJC6VDLAR5FCDD3OCFRBRETRTOBIG3YTBCMUG4JZXQ7J3U`
5. run command `./sandbox goal account export -a <paste 59 character address here>`
6. Copy 25 word pass phrase key for first account

### Step 4
1. Locate `send_note()` function from `Main.py` file
2. set `passphrase = "<paste 25 word pass phrase key here>"`
3. Go back to sandbox account list and copy the second or third 59 character account address, 
4. set `receiver = "<second or third account address from sandbox account list here>"`

### Step 5
1. Return to `parse_into_json()` function from `Main.py` file
2. make a debugger break for line 69 which contains `parse_final_value = int(url_Number) - 1`
3. debug to find `url_Number` value
4. `int(url_Number) - 1` is the maximum amount of results this application can index from the FDA API
5. scroll down to `results_location` and set this value equal to `0` or to the maximum amount of results indexed which equals `int(url_Number) - 1 `
6. Based on what `recall_type` set in Step 2, change prefix from `'FDAF'` in `json_note = '<prefix>' + json_note` to a prefix suited for other recall types such as `'FDAF'` for food, or `'FDADR'` for drug recalls or `'FDADE'` for medical devices

### Step 6
1. Run `Main.py` file
2. Verify transaction is sent by seeing the decoded note in the terminal
3. If more transactions wish to be sent, simply change the `results_location` value to another number equal or lower than `int(url_Number) - 1 ` and run `Main.py` file again

### Step 7
1. Locate `Indexer.py` file
2. Referring to the final step in Step 5, change `note_prefix = 'FDAF'.encode()` to `note_prefix = '<new prefix>'.encode()`
3. Run `Indexer.py` file

### Final Step
1. Indexer should now have successfully indexed all recall data encoded into the notefield of the transactions with `'<your prefix>'` 


  

## Future Improvements

- FDA could send txn with data encoded in notefield to an FDA receiver account
- Build  front-end interface for customers to create an Algorand account and scan receipts looking for recalls
- Customer locates recall item and scans/inputs UPC(or UDI for Medical Recalls)
- Indexer finds customer's recall item and confirms customer's recall item is Ongoing
- Customer recall item UPC/UDI code is verified through third-party oracle 
- Companies can send refund txns with notefield of recall item and code to customer's with Ongoing recall items.
- Company can track all their recall refunds using their own indexer parameters


