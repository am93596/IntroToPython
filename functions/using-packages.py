import requests

bbc_r = requests.get("https://www.bbc.co.uk/news")
print(bbc_r)
print(bbc_r.content)
