import sys, oracle

BLOCK_SIZE = 16

file = open(sys.argv[1], 'r')
ciphertext = file.read().strip()

oracle.Oracle_Connect()
message_bytes = bytearray(bytes.fromhex(ciphertext))
result = bytearray()
while len(message_bytes) != BLOCK_SIZE:
    block = bytearray(BLOCK_SIZE)
    i = BLOCK_SIZE - 1
    while i >= 0:
        for j in range(256):
            block[i] = j
            possible_decription = message_bytes[:]
            for k in range(BLOCK_SIZE):
                xor_value = block[k] ^ (BLOCK_SIZE - i)
                possible_decription[k - 2 * BLOCK_SIZE] ^= xor_value
            if oracle.Oracle_Send(possible_decription, int(len(possible_decription) / BLOCK_SIZE)):
                break
        else:
            block[i] = -i
        i -= 1

    message_bytes = message_bytes[: -BLOCK_SIZE]
    result_copy = result[:]
    result = bytearray(block)
    for elem in result_copy:
        result.append(elem)

encoded_message = result[: -result[-1]]
print(encoded_message.decode('utf-8'))
oracle.Oracle_Disconnect()