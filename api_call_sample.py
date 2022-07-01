import json

import requests
import random

from requests import post

n = range(1)
for num in n:
    ip = '.'.join(map(str, (random.randint(0,255) for _ in range(4))))
    url_end_point  = "https://ipinfo.io/" + ip + "/geo"
    response = requests.get(url=url_end_point, )
    data = response.json()
    print(data)


post_url = "https://jsonplaceholder.typicode.com/posts"
data = {
            "title": "fo0",
            "body": "bar",
            "userId": 1
        }
post_headers = {
  'Content-Type': 'application/json'
}

print(type(post_headers))
print(type(json.dumps(post_headers)))

response = requests.request("POST", post_url, headers={}, data=data)
print(response.text)




