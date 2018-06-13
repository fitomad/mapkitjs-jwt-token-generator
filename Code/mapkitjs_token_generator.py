#!/usr/bin/env python
#coding: utf-8

"""
Packages required:

- PyJWT (pip install PyJWT)
- Cryptography (pip install cryptography)

Adolfo Vera - @fitomad
"""

from os import path
import time
import jwt
from datetime import datetime

# Mandatory fileds. 

private_key_file_path = "[YOUR_PRIVATE_KEY_FILE].p8"
apple_team_id = "YOUR_APPLE_TEAM_ID"
mapkit_key_id = "YOUR_MAPKIT_KEY_ID"

# Optional but recommended fields.

origin_domain = "http://subdomain.yourdomain.com"

#
# Token life period
#

epoch = datetime.utcfromtimestamp(0)

time_iat = (datetime.utcnow() - epoch).total_seconds()
time_expt = time_iat + 15552000 # 180 days 

#
# Secret word
#

if not path.exists(private_key_file_path):
    print("File with .p8 extension doesn't exists.")
    exit()

with open(private_key_file_path) as file:
    authKey = file.read()
file.close()

#
# Payload
#

payload = {
    "iss" : apple_team_id,
    "iat" :  int(time_iat),
    "expt" :  int(time_expt)
}

if origin_domain:
    payload["origin"] = origin_domain

#
# Header
#

header = {
    "kid" : mapkit_key_id,
    "typ" : "JWT",
    "alg" : "ES256"
}

#
# Create JWT Token
#

token = jwt.encode(payload, key=authKey, algorithm="ES256", headers=header)

print("Here's your JWT Token for Apple MapKit JS\nCopy content below this line.")
print(token.decode('utf-8'))