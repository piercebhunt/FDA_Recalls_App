import base64
import json
from algosdk.v2client import indexer


myindexer = indexer.IndexerClient(
    indexer_token="", indexer_address="http://localhost:8980")
note_prefix = 'FDAF'.encode()
response = myindexer.search_transactions(note_prefix=note_prefix)
print("note_prefix = " + json.dumps(response, indent=2, sort_keys=True))
