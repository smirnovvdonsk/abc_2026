

FIRST_CYRILLIC_LETTER_LOWERCASE = 'а'
FIRST_CYRILLIC_LETTER_UPPERCASE = 'А'

# В Юникоде вся русская кириллица кроме "Ё" расположена последовательно
# Мы принудительно заменим "Ё" на "Е"
# Значит букв в русском алфавите 32
CYRYLLIC_COUNT = 32

def get_letter(v: str) -> str:
    first_letter = v[0] if len(v) else ' '
    if first_letter=='ё': return 'е'
    if first_letter=='Ё': return 'Е'
    return first_letter

FIRST_CYRILLIC_LETTER_LOWERCASE_UNICODE_INDEX = ord(get_letter(FIRST_CYRILLIC_LETTER_LOWERCASE))
FIRST_CYRILLIC_LETTER_UPPERCASE_UNICODE_INDEX = ord(get_letter(FIRST_CYRILLIC_LETTER_UPPERCASE))

LETTERS_LOWERCASE = [chr(i + FIRST_CYRILLIC_LETTER_LOWERCASE_UNICODE_INDEX) for i in range(CYRYLLIC_COUNT)]
LETTERS_UPPERCASE = [chr(i + FIRST_CYRILLIC_LETTER_UPPERCASE_UNICODE_INDEX) for i in range(CYRYLLIC_COUNT)]

# Можно проверить нашу гипотезу о последовательном расположении русской кириллицы в Юникоде без буквы "Ё"
# print(LETTERS_LOWERCASE)
# print(LETTERS_UPPERCASE)

def get_encrypted_letter(raw_letter: str, indent: int) -> str:
    letter = get_letter(raw_letter)
    for alphabet in [LETTERS_LOWERCASE, LETTERS_UPPERCASE]:
        if letter in alphabet:
            return alphabet[alphabet.index(letter) - indent]
    return letter

def get_encrypted_line(line: str, line_idx: int) -> str:
    return ''.join([ get_encrypted_letter(letter, line_idx + 1) for letter in line ])

def get_encrypted(txt: str) -> str:
    return '\n'.join([ get_encrypted_line(line, line_idx) for line_idx, line in enumerate(txt.split('\n'))])

def get_unencrypted_letter(raw_letter: str, indent: int) -> str:
    letter = get_letter(raw_letter)
    for alphabet in [LETTERS_LOWERCASE, LETTERS_UPPERCASE]:
        inverted_alphabet = list(alphabet)
        inverted_alphabet.reverse()
        if letter in inverted_alphabet:
            return inverted_alphabet[inverted_alphabet.index(letter) - indent]
    return letter

def get_unencrypted_line(line: str, line_idx: int) -> str:
    return ''.join([ get_unencrypted_letter(letter, line_idx + 1) for letter in line ])


def get_unencrypted(txt: str) -> str:
    return '\n'.join([ get_unencrypted_line(line, line_idx) for line_idx, line in enumerate(txt.split('\n'))])
