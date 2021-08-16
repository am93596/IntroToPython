import requests
# from pprint import pprint
import json
from postcode import PostCode

postcode_url = "https://api.postcodes.io/postcodes/"
# postcode_request = requests.get(postcode_url + "B7 4BB")
#
# print(postcode_request, type(postcode_request))
#
# print(postcode_request.status_code == 200)
# print(postcode_request.headers, type(postcode_request.headers))
# print(postcode_request.content, type(postcode_request.content))
#
# pprint(postcode_request.json())
# print(type(postcode_request.json()))
#
# # Print the latitude and longitude of this postcode
# postcode_info = postcode_request.json().get('result')
# print(f"(Latitude: {postcode_info.get('latitude')}, Longitude: {postcode_info.get('longitude')})")

postcodes = {'postcodes': ["PR3 0SG", "M45 6GN", "EX16 5BL"]}
body = json.dumps(postcodes)
headers = {'Content-Type': 'application/json'}
multi_pc_req = requests.post(postcode_url, headers=headers, data=body)
# print(multi_pc_req)
multi_pc = multi_pc_req.json()['result']
# pprint(multi_pc, sort_dicts=False)

# Print each postcode, followed by its latitude and longitude
for postcode in multi_pc:
    pc = PostCode(postcode['result'])
    print(pc)
    print(pc.get_location())
    print(pc.get_location(en=True))
    print()
