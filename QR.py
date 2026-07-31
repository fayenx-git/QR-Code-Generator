#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./: <<entire alphanumeric string

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
table = {}

for char, pos in enumerate(chars):
    print(char, pos, "\n")
    table[char] = pos

print(table)

