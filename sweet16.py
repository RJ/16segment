#!/usr/bin/env python
import sys
# |\|/|
#  - -
# |/|\|
#  - -
def set(bit, char):
    if bit:
        return char
    else:
        return " "

#
#   a b
#   _ _

#  cdefg
#  |\|/|

#   h i
#   - -

#  jklmn
#  |/|\|

#   o p
#   - -

def str2bits(s):
    bits = 0
    for c in s:
        if ord(c) < 97 or ord(c) > 112: # a-p
            raise("Letters a-p only")
        bits = bits & (1 << (ord(c)-96))
    return bits

def bits_to_rows(bits):
    # abcd efgh ijkl mnop
    # 0123 4567 8911 1111
    #             01 2345
    return [
        [" ", set(bits & 1, "_"), " ", set(bits & (1 << 1), "_"), " "],
        [set(bits & (1 << 2), "|"), set(bits & (1 << 3), "\\"), set(bits & (1 << 4), "|"), set(bits & (1 << 5), "/"), set(bits & (1 << 6), "|")],
        [" ", set(bits & (1 << 7), "-"), " ", set(bits & (1 << 8), "-"), " "],
        [set(bits & (1 << 9), "|"), set(bits & (1 << 10), "/"), set(bits & (1 << 11), "|"), set(bits & (1 << 12), "\\"), set(bits & (1 << 13), "|")],
        [" ", set(bits & (1 << 14), "-"), " ", set(bits & (1 << 15), "-"), " "]
    ]

font = {
    ' ': 0x0,
    '!': 0b0000100000010000,
    '"': 0b0000000000010100,
    '#': 0b0010100111010011,
    '$': 0b0010100111010011,
    '%': 0xffff,
    '&': 0xffff,
    '\'': 0b0000000000010000,
    '(': 0b0001000010100000,
    ')': 0b0000010100001000,
    '*': 0b0001110110111000,
    '+': 0b0000100110010000,
    ',': 0b0000010000000000,
    '-': 0b0000000110000000,
    '.': 0b0100000000000000,
    '/': 0b0000010000100000,
    '0': 0b1110001001000111,
    '1': 0b0000001000000100,
    '2': 0b1100001111000011,
    '3': 0b1110000111000011,
    '4': 0b0010000111000100,
    '5': 0b1110000110000111,
    '6': 0b1110001110000100,
    '7': 0b0000010000100011,
    '8': 0b1110001111000111,
    '9': 0b0010000111000111,
    ':': 0b0000100000010000,
    ';': 0b0000010000010000,
    '<': 0b0001000000001000,
    '=': 0b1000000100000000,
    '>': 0b0001000000001000,
    '?': 0xffff,
    '@': 0xffff,
    'A': 0b0010001111000111,
    'B': 0b1110100101010011,
    'C': 0b1100001000000111,
    'D': 0b1110100001010011,
    'E': 0b1100001110000111,
    'F': 0b0000001110000111,
    'G': 0b1110001100000111,
    'H': 0b0010001111000100,
    'I': 0b1100100000010011,
    'J': 0b0100100000010011,
    'K': 0b0001001010100100,
    'L': 0b1100001000000100,
    'M': 0xffff,
    'N': 0xffff,
    'O': 0b1110001001000111,
    'P': 0b0000001111000111,
    'Q': 0b1111001001000111,
    'R': 0xffff,
    'S': 0xffff,
    'T': 0xffff,
    'U': 0xffff,
    'V': 0xffff,
    'W': 0xffff,
    'X': 0xffff,
    'Y': 0xffff,
    'Z': 0xffff,
    '[': 0xffff,
    '\\': 0b0000010000100000,
    ']': 0xffff,
    '^': 0xffff,
    '_': 0xffff,
    '`': 0xffff,
    'a': 0xffff,
    'b': 0xffff,
    'c': 0xffff,
    'd': 0xffff,
    'e': 0xffff,
    'f': 0xffff,
    'g': 0xffff,
    'h': 0xffff,
    'i': 0xffff,
    'j': 0xffff,
    'k': 0xffff,
    'l': 0xffff,
    'm': 0xffff,
    'n': 0xffff,
    'o': 0xffff,
    'p': 0xffff,
    'q': 0xffff,
    'r': 0xffff,
    's': 0xffff,
    't': 0xffff,
    'u': 0xffff,
    'v': 0xffff,
    'w': 0xffff,
    'x': 0xffff,
    'y': 0xffff,
    'z': 0xffff,
    '{': 0xffff,
    '|': 0xffff,
    '}': 0xffff,
    '~': 0xffff,
}



def print_ascii_as_16seg(s):
    codes = str_to_codes(s)
    print_asciiart_from_codes(codes)
    print "Codes: ",
    for c in codes:
        print c,
    sys.stdout.write("\n")

def str_to_codes(s):
    codes = []
    for char in s:
        if not char in font:
            fontcode = 0xffff
        else:
            fontcode = font[char]
        codes.append(fontcode)
    return codes

def print_asciiart_from_codes(codes):
    rowchars = [bits_to_rows(fontcode) for fontcode in codes]
    # Print!
    for rownum in range(0,5):
        for character in rowchars:
            for char in character[rownum]:
                sys.stdout.write(char)
            sys.stdout.write(" ") # end of character column spacing
        sys.stdout.write("\n")

if __name__ == "__main__":
    ks = font.keys()
    ks.sort()
    while True:
        line = raw_input("String>  ")
        if line == "":
            sys.exit(0)

        print_ascii_as_16seg(line)
        sys.stdout.write("\n")
