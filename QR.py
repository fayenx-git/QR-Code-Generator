#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./: <<entire alphanumeric string

#things that never change
#lookup_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, ' ': 36, '$': 37, '%': 38, '*': 39, '+': 40, '-': 41, '.': 42, '/': 43, ':': 44}
ltAlternate = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:")
mode = "0010"

  #  if character not in lookup_table:
 #       print("Only uppercase letters, space, and these symbols $%*+-./: can be used")
#    digit_string[lookup_table[character]]
#print(digit_string)

input_text = input("Enter text>")
digit_string = []
for character in input_text:
    digit = ltAlternate.index(character.upper())
    digit_string.append(digit)
if len(digit_string) % 2 == 1: #if odd
    digit_string.append(36) #Adding an extra space for simplicity sake. I do not want to implement the rules for the last digit if the string is an odd number of characters.

char_count = bin(len(digit_string))[2:].zfill(9)
print(char_count)
new_digit_string = []
for i in range(0, len(digit_string), 2):
    new_digit_string.append(bin((digit_string[i] * 45)+digit_string[i+1])[2:].zfill(11))
bit_string = "".join(new_digit_string)
total_bit_stream = mode + char_count + bit_string
print(total_bit_stream)
print(len(total_bit_stream))

terminator_0 = "0"
terminator_00 = "00"
terminator_000 = "000"
terminator_0000 = "0000"

if len(total_bit_stream) < 440 and len(total_bit_stream) > 438:
    total_bit_stream += terminator_0
elif len(total_bit_stream) < 440 and len(total_bit_stream) > 437:
    total_bit_stream += terminator_00
elif len(total_bit_stream) < 440 and len(total_bit_stream) > 436:
    total_bit_stream += terminator_000
elif len(total_bit_stream) < 440 and len(total_bit_stream) > 0:
    total_bit_stream += terminator_0000

while len(total_bit_stream) % 8 != 0:
    total_bit_stream += "0"

pad_bytes = ["11101100", "00010001"] #it is fun to say it over and over again

i = 0
while len(total_bit_stream) < 440:
    total_bit_stream += pad_bytes[i % 2]
    i += 1
print(total_bit_stream)
print(len(total_bit_stream))

#copied and pasted from https://www.codestudy.net/blog/add-separator-to-string-at-every-n-characters/#2-step-1-adding-a-separator-every-8-characters

def add_separator(total_bit_stream, separator=' '):
    # Split the binary string into 8-character chunks
    chunks = [total_bit_stream[i:i+8] for i in range(0, len(total_bit_stream), 8)]
    # Join chunks with the separator
    return separator.join(chunks)
