#!/usr/bin/env python3
import sys

SYMBOLS = {
    'standard': ' ',
    'blocks': ' .:+#',
    'dense': ' .:-=+*#%@',
    'shades': ' .:oO@',
    'stars': ' .*+:',
    'hash': ' #',
    'at': ' @',
    'equals': ' =',
}

BASE_PATTERNS = {
    'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
    'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
    'C': [' CCC ', 'C    ', 'C    ', 'C    ', ' CCC '],
    'D': ['DDD  ', 'D  D ', 'D   D', 'D  D ', 'DDD  '],
    'E': ['EEEEE', 'E    ', 'EEE  ', 'E    ', 'EEEEE'],
    'F': ['FFFFF', 'F    ', 'FFF  ', 'F    ', 'F    '],
    'G': [' GGG ', 'G    ', 'G  GG', 'G   G', ' GGG '],
    'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
    'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
    'J': ['JJJJJ', '   J', '   J', 'J  J', ' JJ '],
    'K': ['K   K', 'K  K ', 'KK   ', 'K  K ', 'K   K'],
    'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
    'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
    'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
    'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
    'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
    'Q': [' QQQ ', 'Q   Q', 'Q Q Q', 'Q  Q ', ' QQ Q'],
    'R': ['RRRR ', 'R   R', 'RRRR ', 'R  R ', 'R   R'],
    'S': [' SSS ', 'S    ', ' SSS ', '    S', ' SSS '],
    'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
    'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
    'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
    'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
    'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
    'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
    'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
    '0': ['0000 ', '0  00', '0 0 0', '00  0', '0000 '],
    '1': ['  1  ', ' 11  ', '  1  ', '  1  ', '11111'],
    '2': ['2222 ', '    2', ' 222 ', '2    ', '22222'],
    '3': ['3333 ', '    3', ' 333 ', '    3', '3333 '],
    '4': ['4   4', '4   4', '44444', '    4', '    4'],
    '5': ['55555', '5    ', '5555 ', '    5', '5555 '],
    '6': [' 666 ', '6    ', '6666 ', '6   6', ' 666 '],
    '7': ['77777', '    7', '   7 ', '  7  ', '  7  '],
    '8': [' 888 ', '8   8', ' 888 ', '8   8', ' 888 '],
    '9': [' 999 ', '9   9', ' 9999', '    9', ' 999 '],
    ' ': ['     ', '     ', '     ', '     ', '     '],
}


def convert_pattern(pattern, symbol_set='standard'):
    if symbol_set == 'standard':
        return pattern
    symbols = SYMBOLS.get(symbol_set, ' *#@').strip()
    if len(symbols) == 1:
        return [row.replace(' ', symbols[0]) for row in pattern]
    fill_char = symbols[-1]
    result = []
    for row in pattern:
        new_row = ''
        for char in row:
            if char == ' ':
                new_row += ' '
            else:
                new_row += fill_char
        result.append(new_row)
    return result


def text_to_ascii(text, symbol_set='standard'):
    text = text.upper()
    lines = ['', '', '', '', '']
    for char in text:
        pattern = BASE_PATTERNS.get(char)
        if pattern:
            converted = convert_pattern(pattern, symbol_set)
            for i in range(5):
                lines[i] += converted[i] + ' '
    return '\n'.join(lines)


def text_to_ascii_variant(text, symbol_set='blocks'):
    text = text.upper()
    symbol = SYMBOLS.get(symbol_set, ' ')[-1]
    lines = ['', '', '', '', '']
    for char in text:
        pattern = BASE_PATTERNS.get(char)
        if pattern:
            converted = convert_pattern(pattern, symbol_set)
            for i in range(5):
                lines[i] += converted[i] + ' '
    return '\n'.join(lines)


def text_to_ascii_border(text, symbol_set='double'):
    text = text.upper()
    symbols = SYMBOLS[symbol_set]
    lines = ['', '', '', '', '']
    for char in text:
        pattern = BASE_PATTERNS.get(char)
        if pattern:
            for row_idx, row in enumerate(pattern):
                new_row = symbols[3]
                for char_pos in row:
                    if char_pos == ' ':
                        new_row += ' '
                    else:
                        new_row += symbol_set
                new_row += symbols[3]
                lines[row_idx] += new_row
    return '\n'.join(lines)


def show_all_variants(text):
    variants = [
        ('Standard', text_to_ascii(text, 'standard')),
        ('Blocks (#)', text_to_ascii_variant(text, 'blocks')),
        ('Dense (@)', text_to_ascii_variant(text, 'dense')),
        ('Shades (@)', text_to_ascii_variant(text, 'shades')),
        ('Stars (:)', text_to_ascii_variant(text, 'stars')),
        ('Hash (#)', text_to_ascii(text, 'hash')),
        ('At (@)', text_to_ascii(text, 'at')),
        ('Equals (=)', text_to_ascii(text, 'equals')),
    ]
    for name, art in variants:
        print(f'\n=== {name} ===')
        print(art)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--all':
            text = ' '.join(sys.argv[2:]) if len(sys.argv) > 2 else 'HELLO'
            show_all_variants(text)
        else:
            text = ' '.join(sys.argv[1:])
            show_all_variants(text)
    else:
        text = input('Enter text: ')
        show_all_variants(text)
