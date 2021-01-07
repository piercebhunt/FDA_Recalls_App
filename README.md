# **FDA Recalls Application**

## Overview

The FDA has open-source APIs for food, device, and drug recalls; this application stores FDA recall data on Algorand’s blockchain by encoding the FDA’s API results in a transaction notefield using Python. After the recall data is encoded and stored on Algorand, this application then indexes transactions with the recall data based on an specific, encoded prefix.

This application focuses on the dates of 12/01/20 to 12/02/20 for food recalls specifically; the prefix 'FDAF' is used for the indexer portion. This application can encompass other date timelines and incorporate food, drug, or medical device recalls. 


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


## Conclusion/ Future Improvements

- FDA could send txn with data encoded in notefield to an FDA receiver account
- Build  front-end interface for customers to create an Algorand account and scan receipts looking for recalls
- Customer locates recall item and scans/inputs UPC(or UDI for Medical Recalls)
- Indexer finds customer's recall item and confirms customer's recall item is Ongoing
- Customer recall item UPC/UDI code is verified through third-party oracle 
- Companies can send refund txns with notefield of recall item and code to customer's with Ongoing recall items.
- Company can track all their recall refunds using their own indexer parameters


