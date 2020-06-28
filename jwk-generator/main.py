# from authlib.jose import JsonWebKey
# from authlib.jose import JWK_ALGORITHMS

from authlib.jose import jwk
import json

pr = jwk.dumps(open('private_key.pem').read(), kty='RSA', alg="RS256")
pu = jwk.dumps(open('public_key.pem').read(), kty='RSA', alg="RS256")
alg_name = "alg1"
pr["kid"] = alg_name
pu["kid"] = alg_name

result = {
    "keys": [
        pr
    ]
}
open('jwks-priv.json', "w").write(json.dumps(result))

result = {
    "keys": [
        pu
    ]
}
open('jwks-pub.json', "w").write(json.dumps(result))
