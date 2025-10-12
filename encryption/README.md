# Encryption

Encryption is the process of converting **plain text** (readable data) into **ciphertext** (unreadable data) using a **cryptographic key**.  
Only someone with the correct key can decrypt the ciphertext back into readable plain text.

**Key terms:**
- **Plaintext:** Original readable data.
- **Ciphertext:** Encrypted data.
- **Key:** Secret value used for encryption/decryption.


## Types of Encryption

1. **Symmetric Encryption**  
   - Uses the **same key** for both encryption and decryption.  
   - Example: AES (Advanced Encryption Standard).

2. **Asymmetric Encryption (Public Key Encryption)**  
   - Uses a **public key** for encryption and a **private key** for decryption.  
   - Example: RSA (Rivest–Shamir–Adleman), which is demonstrated in this folder.


## RSA Encryption Example

RSA is a widely-used asymmetric encryption algorithm.  
This example demonstrates:

1. Generating a public/private key pair.
2. Encrypting a message using the public key.
3. Decrypting the message using the private key.
4. Showing what happens when decryption is attempted with a different key.


## Security Notes

- Use **key sizes of 2048 bits or larger** for RSA to ensure security.
- RSA is not suitable for encrypting large messages directly. Instead, encrypt a symmetric key with RSA and use the symmetric key to encrypt the message.
- Smaller key sizes (like 512 bits) are **insecure** and only suitable for educational examples.
