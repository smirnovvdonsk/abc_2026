#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

import re

FIRST_LATIN_LETTER_LOWERCASE_UNICODE_INDEX: int = ord('a')

def decode_int(v: int) -> str:
    if v == 0: return '' # Судя по примеру, ноль должен игнорироваться
    return chr(FIRST_LATIN_LETTER_LOWERCASE_UNICODE_INDEX - 1 + v)

def decode(txt: str) -> str:
    elements = [
        decode_int(int(int_match)) if int_match else other_match
        for int_match, other_match in re.findall('(\\d+ ?)|(\\S*\\s*)', txt)
    ]
    return ''.join(elements)

ORIGINAL_ENCRYPTED = """8 5 12 12 15
8 5 12 12 15 , 0 23 15 18 12 4 !"""

decrypted = decode(ORIGINAL_ENCRYPTED)

print(decrypted)