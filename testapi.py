#!/usr/bin/python3

import requests
        
req = requests.get("https://theducky.github.io/HelloWorld-API/APIs/HelloWorld.json")
dct = req.json()

pst = dct["Python"]
pst2 = dct["Java"][0]["Code"]
print(pst)
print(pst2)