import jwt
import datetime

def create_token(payload, key='pass'): #створення токену
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    return jwt.encode(
        payload=payload,
        key=key,
        algorithm='HS256',
    )

def is_token_expired(token, password):  #передача пароля як аргумента
    try:
        decoded = jwt.decode(
            token,
            password,
            algorithms=['HS256'],
        )
        exp = decoded.get('exp', 0)
        current_time = datetime.datetime.utcnow()
        return exp < current_time.timestamp()  #перетворення datetime в timestamp
    except jwt.ExpiredSignatureError:
        return True
    except jwt.InvalidTokenError:
        return True

def is_valid_password(token, password):
    try:
        decoded = jwt.decode(
            token,
            password,
            algorithms=['HS256'],
        )
        return True
    except jwt.InvalidTokenError:
        return False

def decode_token(token, password):
    try:
        decoded = jwt.decode(
            token,
            password,
            algorithms=['HS256'],
        )
        return decoded
    except jwt.InvalidTokenError:
        return {}

#приклад застосування:

# payload = {
#     'my name': 'Oleg',
#     'my_age': 78,
# }

# password = 'pass'  #визначення паролю
# token = create_token(payload)
# print(f"Token: {token}")

# if not is_token_expired(token, password):
#     print("Token is not expired.")
# else:
#     print("Token is expired.")

# if is_valid_password(token, password):
#     print("Password is valid.")
# else:
#     print("Password is not valid.")

# decoded_payload = decode_token(token, password)
# print(f"Декодований Payload: {decoded_payload}")