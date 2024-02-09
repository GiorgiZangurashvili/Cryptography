key = str(input().strip())
plaintext = str(input().strip())

key = key * (int((len(plaintext) / len(key))) + 1)

key = key[0:len(plaintext)]

print("".join(f'{ord(a) ^ ord(b):02x}' for a, b in zip(key, plaintext)))