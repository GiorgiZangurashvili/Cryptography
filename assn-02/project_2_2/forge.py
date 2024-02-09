import sys, oracle

BLOCK_SIZE = 16

file = open(sys.argv[1], 'r')
message = file.read()
file.close()

oracle.Oracle_Connect()

tag = bytearray([0] * len(message))
for i in range(0, len(message), 2 * BLOCK_SIZE):
    blocks = message[i : i + 2 * BLOCK_SIZE]
    xor_value = ''.join(chr(a ^ ord(b)) for a, b in zip(tag[: BLOCK_SIZE], blocks[: BLOCK_SIZE]))
    new_tag = oracle.Mac(xor_value + blocks[BLOCK_SIZE :], 2 * BLOCK_SIZE)
    if oracle.Vrfy(xor_value + blocks[BLOCK_SIZE :], 2 * BLOCK_SIZE, new_tag):
        tag = new_tag
    
if oracle.Vrfy(message, len(message), tag):
    print(tag.hex())
else:
    print("Message verification failed: ", tag.hex())

oracle.Oracle_Disconnect()