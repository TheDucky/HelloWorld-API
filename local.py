#!/usr/bin/python3

import requests
        
req = requests.get("http://127.0.0.1:5500/APIs/HelloWorld.json")
dct = req.json()

pst = dct["Python"]
pst2 = dct["Java"][0]["Code"]
print(pst)
print(pst2)