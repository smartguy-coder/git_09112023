import hashlib

from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(value: str) -> str:
    hash = context.hash(value)
    return hash


get_password_hash('password')
get_password_hash('password')
get_password_hash('password')
get_password_hash('password')
get_password_hash('password')


















def encode_md5(value: str) -> str:
    hash = hashlib.md5(value.encode()).hexdigest()
    return hash
