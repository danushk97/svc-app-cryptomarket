import hashlib
import hmac


def calculate_sha512_hash(value: str):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(value.encode('utf-8'))

    return sha512_hash.hexdigest()


def calculate_hmac_sha512_signature(data, secret_key):
    hmac_digest = hmac.new(
        secret_key.encode('utf-8'), 
        data.encode('utf-8'), 
        hashlib.sha512
    )
    signature = hmac_digest.hexdigest()

    return signature
