import rsa

# Generate public and private keys (secure size)
publicKey, privateKey = rsa.newkeys(2048)

message = "Hello, secure world!"

# Encrypt the message
encMessage = rsa.encrypt(message.encode(), publicKey)
print("Original string:", message)
print("Encrypted string:", encMessage)

# Decrypt the message
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("Decrypted string:", decMessage)

# Show decryption failure with a different key
wrongPublic, wrongPrivate = rsa.newkeys(2048)
try:
    decMessage = rsa.decrypt(encMessage, wrongPrivate).decode()
except rsa.pkcs1.DecryptionError:
    print("Decryption failure expected with a different key")