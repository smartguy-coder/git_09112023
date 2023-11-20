import datetime

import jwt

import settings

payload = {
    "my_name": "Vasyl",
    "age": 10,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
}

encode_jwt = jwt.encode(
    payload=payload,
    key=settings.JWT_SECRET,
    algorithm="HS256",
)
print(encode_jwt)

decoded = jwt.decode(
    encode_jwt,
    settings.JWT_SECRET,
    algorithms=["HS256"],
    # options={
    #     'verify_signature': False,
    # }
)
print(decoded)
