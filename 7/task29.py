#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.

# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

ENCRYPTED = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

# Ранее наш код цезаря расшифровывал только кориллицу
# Теперь, очевидно, речь идёт о латиннице

FIRST_LETTER_LOWERCASE = 'a'
FIRST_LETTER_UPPERCASE = 'A'

def get_letter(v: str) -> str:
    return v[0] if len(v) else ' '

FIRST_LETTER_LOWERCASE_UNICODE_INDEX = ord(get_letter(FIRST_LETTER_LOWERCASE))
FIRST_LETTER_UPPERCASE_UNICODE_INDEX = ord(get_letter(FIRST_LETTER_UPPERCASE))

LATIN_COUNT = 26

LETTERS_LOWERCASE = [chr(i + FIRST_LETTER_LOWERCASE_UNICODE_INDEX) for i in range(LATIN_COUNT)]
LETTERS_UPPERCASE = [chr(i + FIRST_LETTER_UPPERCASE_UNICODE_INDEX) for i in range(LATIN_COUNT)]

def get_decrypted_letter(raw_letter: str, indent: int) -> str:
    letter = get_letter(raw_letter)
    for alphabet in [LETTERS_LOWERCASE, LETTERS_UPPERCASE]:
        if letter in alphabet:
            return alphabet[alphabet.index(letter) - indent]
    return letter

def get_decrypted_line(line: str, line_idx: int) -> str:
    return ''.join([ get_decrypted_letter(letter, line_idx + 1) for letter in line ])


indent = 0

while indent < LATIN_COUNT:
    print(f"Сдвиг {indent}:\t{get_decrypted_line(ENCRYPTED, indent)}")
    indent += 1






