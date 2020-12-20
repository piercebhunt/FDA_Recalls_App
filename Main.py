import requests
import json

# dates and recall type
date1 = 20201201
date2 = 20201202
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

# print to find results based on API total
# print(parse_final_value)

# Add prefix FDAF to specified result location
parse_location = 0
result = results_only[parse_location]

fdaf_dict = {'FDA': 'Food'}
fdaf_dict.update(result)
json_note = json.dumps(fdaf_dict)
