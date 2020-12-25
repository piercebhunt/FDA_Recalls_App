Description

Python application to store OpenFDA Recall JSON results on Algorand. This application focuses on the dates of 12/01/20 to 12/02/20 for Food Recalls specifically. This app can encompass other date timelines and incorporate food, drug, or medical device recalls.

Requirements

-Python 3

-Python Algorand SDK


Additional Resources of Use

-Read and Write to the Transaction Note Field with Python Tutorial

- Indexer Algorannd Documentation


Future Improvements

- FDA could send txn with data encoded in notefield to an FDA receiver account
-Build interface for customers to create an Algorand account and scan receipts looking for recalls
-customer locates recall item and scans/inputs UPC(or UDI for Medical Recalls) and uploads
- oracle verifies with indexer that recall is ongoing
  -suggests that the customer requests refund
-create a smart contract pool with funds equivalent of the recall quantity price in algos or stablecoin
-when customer item is verified through oracle and customer requests refund. 
-oracle directs refund smart contract to appropriate company pool and requests a txn. company sends txn with notefield of recall item and code.
-company can track all refunds using their own indexer parameters

Benefites of this application
-Ease of refunds for consumers
-More transparency in the recall industry
-Chance to reward recall customers in a different way such as tokenized rewards to help repair brand damage
-this app could ease the burden of recall recovery efforts/time for small businesses to large businesses
