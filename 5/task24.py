# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

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

FILE_NAME = 'message.txt'

original_lines = ['']

with open(FILE_NAME, 'r', encoding='utf-8') as file:
    original_lines = file.readlines()
    file.close()

print('Оригинальный файл:')
print(''.join(original_lines))
print('')


encrypted_lines = [get_encrypted_line(line, line_idx) for line_idx, line in enumerate(original_lines)]

print('Зашифрованный файл:')
print(''.join(encrypted_lines))
print('')


# Расшифровываем обратно для проверки:

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

unencrypted_lines = [get_unencrypted_line(line, line_idx) for line_idx, line in enumerate(encrypted_lines)]

print('Расшифрованный обратно файл:')
print(''.join(unencrypted_lines))
print('')








