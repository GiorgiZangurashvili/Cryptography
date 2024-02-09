# Got this frequency map from: https://en.wikipedia.org/wiki/Letter_frequency
frequencies = {'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022, 'G': 0.02, 'H': 0.061,
               'I': 0.07, 'J': 0.0015, 'K': 0.0077, 'L': 0.04, 'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019,
               'Q': 0.00095, 'R': 0.06, 'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.0098, 'W': 0.024, 'X': 0.0015,
               'Y': 0.02, 'Z': 0.00074, ' ': 0.1}

str_hex = input().strip()
output = ""
min_deviation = float("inf")

for i in range(256):
    deviation = 0
    possible_output = ""
    for byte in bytes.fromhex(str_hex):
        possible_output += chr(byte ^ i)

    if len(possible_output) != 0:
        for letter in frequencies:
            deviation += abs(possible_output.upper().count(letter) / len(possible_output) - frequencies[letter])

        if deviation < min_deviation:
            min_deviation = deviation
            output = possible_output
print(output)