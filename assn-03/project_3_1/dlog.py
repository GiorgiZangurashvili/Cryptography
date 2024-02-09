import math

# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(p, g, h, max_x):
    num_steps = int(math.sqrt(max_x) + 1)
    mult = pow(g, -1, p)
    hash_table = {}
    for value in range(num_steps):
        hash_table[h] = value
        h *= mult
        h %= p
    
    key = 1
    mult = pow(g, num_steps, p)
    for i in range(num_steps):
        if key in hash_table.keys():
            return i * num_steps + hash_table[key]
        key *= mult
        key %= p
        
    return -1

def main():
	p = int(input().strip())
	g = int(input().strip())
	h = int(input().strip())
	max_x = 1 << 40 # 2^40

	dlog = discrete_log(p, g, h, max_x)
	print(dlog)

if __name__ == '__main__':
	main()