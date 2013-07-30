#!/usr/bin/env python
import sys

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

# Turns "abcjgnhi" into int for segment activation
def str2bits(s):
    bits = 0
    for c in s:
        if ord(c) < 97 or ord(c) > 112: # a-p
            raise("Letters a-p only")
        bits = bits | (1 << (ord(c)-97))
    return bits

def set(bit, char):
    if bit:
        return char
    else:
        return " "

## Creates list of 5 lists - one per row when rendering charater in ascii
def bits_to_rows(bits):
    return [
        [" ", set(bits & 1, "_"), " ", set(bits & (1 << 1), "_"), " "],
        [set(bits & (1 << 2), "|"), set(bits & (1 << 3), "\\"), set(bits & (1 << 4), "|"), set(bits & (1 << 5), "/"), set(bits & (1 << 6), "|")],
        [" ", set(bits & (1 << 7), "-"), " ", set(bits & (1 << 8), "-"), " "],
        [set(bits & (1 << 9), "|"), set(bits & (1 << 10), "/"), set(bits & (1 << 11), "|"), set(bits & (1 << 12), "\\"), set(bits & (1 << 13), "|")],
        [" ", set(bits & (1 << 14), "-"), " ", set(bits & (1 << 15), "-"), " "]
    ]

fontmap = {
    ' ': 0x0,
    '@': "abcdefghijklmnop",
    '$': "abchinopel",
    '&': "ehil", # +
    '\'': "e",
    '*': "defhiklm",
    '+': "ehil",
    '-': "hi",
    '/': "kf",
    '0': "abgnpojckf",
    '1': "aelop",
    '2': "abghijop",
    '3': "abhiopgn",
    '4': "chign",
    '5': "abchinop",
    '6': "abchijnop",
    '7': "abfk",
    '8': "ancghijnop",
    '9': "abcghinop",
    '<': "fm",
    '>': "dk",
    '?': "abgil",
    'A': "abcghijn",
    'B': "abgnopeli",
    'C': "bacjop",
    'D': "abgnopel",
    'E': "abcjophi",
    'F': "abcjhi",
    'G': "abcjopni",
    'H': "cjgnhi",
    'I': "abopel",
    'J': "bgnpoj",
    'K': "cjhfm",
    'L': "cjop",
    'M': "cdfgjn",
    'N': "jcdmng",
    'O': "abcgjnop",
    'P': "cjhigab",
    'Q': "abgnpojcm",
    'R': "jcabgihm",
    'S': "bachinpo",
    'T': "abel",
    'U': "cjopng",
    'V': "cjkf",
    'W': "cjopngl",
    'X': "dfkm",
    'Y': "dfl",
    'Z': "abfkop",
    '[': "acjo",
    '\\': "dm",
    ']': "bgnp",
    '^': "km",
    '_': "op",
    '`': "d",
    '|': "el",
}

def generate_font(fontmap):
    font = {}
    for k in fontmap:
        if isinstance(fontmap[k], int):
            font[k] = fontmap[k]
        else:
            font[k] = str2bits(fontmap[k])
    return font

font = generate_font(fontmap)

def print_ascii_as_16seg(s):
    codes = str_to_codes(s)
    print_asciiart_from_codes(codes)
    print s + " --> ",
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

def print_all_chars():
    i = 0
    tmp = ""
    for k in sorted(font):
        tmp = tmp + k
        i = i + 1
        if(i % 10 == 0):
            print_ascii_as_16seg(tmp)
            sys.stdout.write("\n")
            tmp = ""
            i = 0


if __name__ == "__main__":
    ks = font.keys()
    ks.sort()
    while True:
        line = raw_input("String>  ")
        if line == "":
            sys.exit(0)
        if(line == "..."):
            print_all_chars()
        else:
            print_ascii_as_16seg(line)
        sys.stdout.write("\n")
