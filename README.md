# MapKit JS JWS token generator

![Python 2.7](https://img.shields.io/badge/python-2.6-blue.svg) ![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg) ![MapKit JS](https://img.shields.io/badge/MapKit%20JS-5.X%20beta-yellow.svg)

A python script that generates a JWT token for the new [MapKit JS](https://developer.apple.com/documentation/mapkitjs) web API from Apple. The token generated is valid for **180 days**.

In order to run the script this packages must be installed on your system:

* [PyJWT](https://github.com/jpadilla/pyjwt)
* [Cryptography](https://github.com/pyca/cryptography)

You can check it with  `pip list` command on your Terminal. If not presented install it with

```
sudo pip install pyjwt --user
sudo pip install cryptography --user 
```

## Configuration

In order to generate a valid JWS token you must provide 3 fields and an optional, but recommended, one. The mandatory fields are...

1. Private Key file. The file with .p8 extension downloaded from Apple developer website.
2. Your Apple Team ID. Available in your developer profile.
3. MapKit Api Key ID.

The optional is a domain restriction.

1. Origin. URL where your mapkit web is hosted. If yoor website is under a subdomain you **must include it**. 


```python
# Mandatory fileds. 

private_key_file_path = "[YOUR_PRIVATE_KEY_FILE].p8"
apple_team_id = "YOUR_APPLE_TEAM_ID"
mapkit_key_id = "YOUR_MAPKIT_KEY_ID"

# Optional but recommended fields.

origin_domain = "http://subdomain.yourdomain.com"
```

## Run Script

Open Terminal app on your macOS or Command Prompt on Windows and type the follwing command

```
python mapkitjs_token_generator.py
```

A couple of seconds later you will see something like this

![Script output](https://github.com/fitomad/mapkitjs-jwt-token-generator/blob/master/Screenshots/Captura.JPG)

## Links

* Getting and Using a Mapkit JS Key. [WDC 2018 session](https://developer.apple.com/videos/play/wwdc2018/508/)
* Introducing MapKit JS. [WWDC 2018 session](https://developer.apple.com/videos/play/wwdc2018/212/)

* JWT Protocol. Website with [libraries](https://jwt.io/#libraries-io) and a [*token sandbox*](https://jwt.io/#debugger-io)

## Contact

Any question or suggestion? You will find me on twitter at [@fitomad](https://twitter.com/fitomad)
