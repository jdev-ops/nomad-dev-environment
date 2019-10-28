
from authlib.jose import JsonWebKey
from authlib.jose import JWK_ALGORITHMS

# jwk = JsonWebKey(algorithms=JWK_ALGORITHMS)
# key = open('public.pem').read()
# obj = jwk.dumps(key, kty='RSA')
# # obj is a dict, you may turn it into JSON
# key = jwk.loads(obj)

from authlib.jose import jwk
import json

pr = jwk.dumps(open('private_key.pem').read(), kty='RSA', alg="RS256")
pu = jwk.dumps(open('public_key.pem').read(), kty='RSA', alg="RS256")

open('private_key.json', "w").write(json.dumps(pr))
open('public_key.json', "w").write(json.dumps(pu))

# » openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
# » openssl rsa -pubout -in private_key.pem -out public_key.pem
