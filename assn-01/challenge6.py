import base64

# Got this frequency map from: https://en.wikipedia.org/wiki/Letter_frequency
frequencies = {'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022, 'G': 0.02, 'H': 0.061,
               'I': 0.07, 'J': 0.0015, 'K': 0.0077, 'L': 0.04, 'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019,
               'Q': 0.00095, 'R': 0.06, 'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.0098, 'W': 0.024, 'X': 0.0015,
               'Y': 0.02, 'Z': 0.00074, ' ': 0.1}


def hamming_distance(str1, str2):
    count = 0
    if len(str1) != len(str2):
        return count
    for i in range(len(str1)):
        num_diff_bits = ord(str1[i]) ^ ord(str2[i])
        while num_diff_bits != 0:
            count += num_diff_bits & 1
            num_diff_bits >>= 1
    return count


input_str_bytes = base64.b64decode(input().strip())
input_str = input_str_bytes.decode('utf-8')
min_distance = float('inf')
key_size = -1

for i in range(2, 41):
    curr_distance = 0
    for j in range(0, len(input_str), i):
        str1 = input_str[j: j + i]
        str2 = input_str[j + i: j + 2 * i]
        curr_distance += hamming_distance(str1, str2) / i

    if curr_distance < min_distance:
        key_size = i
        min_distance = curr_distance

key = ""
for i in range(key_size):
    block = input_str[i::key_size]
    max_score = -float('inf')
    xored_byte = 0
    for j in range(256):
        possible_output = ""
        for char in block:
            possible_output += chr(ord(char) ^ j)

        if len(possible_output) != 0:
            score = sum(frequencies[char] for char in possible_output.upper() if char in frequencies)
            if score > max_score:
                max_score = score
                xored_byte = j
    key += chr(xored_byte)

key = key * (int((len(input_str) / len(key))) + 1)
key = key[0:len(input_str)]
print("".join(f'{chr(ord(a) ^ ord(b))}' for a, b in zip(key, input_str)))