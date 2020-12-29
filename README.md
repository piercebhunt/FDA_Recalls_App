# FDA Recalls App

### Description

Python application to store OpenFDA Recall JSON results on Algorand and then index the results. This application focuses on the dates of 12/01/20 to 12/02/20 for Food Recalls specifically. This app can encompass other date timelines and incorporate food, drug, or medical device recalls.

### Requirements

- Python 3

- Python Algorand SDK

### Additional Resources of Use

- Read and Write to the Transaction Note Field with Python Algorand Tutorial

- Indexer Algorand Documentation

### Future Improvements

- FDA could send txn with data encoded in notefield to an FDA receiver account
- Build interface for customers to create an Algorand account and scan receipts looking for recalls
- Customer locates recall item and scans/inputs UPC(or UDI for Medical Recalls)
- Index recall items and confirm recall is Ongoing
- Customer recall item UPC/UDI code is verified through oracle 
- Company sends refund txn with notefield of recall item and code.
- Company can track all their recall refunds using their own indexer parameters

### Benefits of this Application

- Potential for refunds for consumers
- More transparency and accountability in the recall industry
- Potential to reward recall customers in a different way such as tokenized rewards to repair consumer confidence in the company placing the recall
- Improving on this application could ease the burden of recall recovery efforts/time for small businesses to large businesses
