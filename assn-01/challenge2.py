buff1 = input().strip()
buff2 = input().strip()

buff1 = int(buff1, base=16)
buff2 = int(buff2, base=16)

print(hex(buff1 ^ buff2)[2:])
