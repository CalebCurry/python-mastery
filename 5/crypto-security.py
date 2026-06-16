import uuid
import hashlib
import zlib
import hmac
from cryptography.fernet import Fernet

## UUID

print(uuid.uuid7())

## Hashes

print(hash("hello"))
print(hash("hello"))
# hash should never change
# list is mutable -> not ideal for hashing
# print(hash(["this", "is", "a", "list"]))
message = b"hello"
print(hashlib.sha256(message).hexdigest())

# sending over network
print(hashlib.sha256(b"hello").hexdigest())
# passwords
# Store the password and a salt

# Checksum
data = b"hello"
original = zlib.crc32(data)

received = b"hell"
print(zlib.crc32(received) == original)


# signatures
# these do not HIDE any data

secret = b"top-secret-key-dont-share"

# sender side:
message = b"hello"
signature = hmac.new(secret, message, hashlib.sha256).hexdigest()
# what gets sent? the message, and the signature
# the key is known on both sides, but NOT shared through the sent message
# receiving side:
expected = hmac.new(secret, b"different", hashlib.sha256).hexdigest()
print(hmac.compare_digest(signature, expected))

# encryption

key = Fernet.generate_key()
f = Fernet(key)

# sending side:

encrypted = f.encrypt(b"hello")

# receiving side:
message = f.decrypt(encrypted)
print(message)
