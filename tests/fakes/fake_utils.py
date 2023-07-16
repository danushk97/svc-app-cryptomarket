class FakeUtils:
    def calculate_sha512_hash(self, _):
        return "sha512_hash_value"

    def calculate_hmac_sha512_signature(self, secret, value):
        return f"{secret}:{value}"
