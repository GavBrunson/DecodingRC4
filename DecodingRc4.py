def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, plaintext):
    i = 0
    j = 0
    key_stream = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key_stream.append(K)
    return bytes([char ^ key_stream[k] for k, char in enumerate(plaintext)])

def rc4(key, plaintext):
    key = [ord(c) for c in key]
    S = ksa(key)
    return prga(S, plaintext)

# Example usage
key = "Key"
plaintext = b"Plaintext"
ciphertext = rc4(key, plaintext)
print("Ciphertext:", ciphertext)




        
        
