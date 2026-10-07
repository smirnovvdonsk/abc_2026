import helpers

ORIGINAL = """Однажды в студёную зимнюю пору
Я из лесу вышел - был сильный мороз"""

helpers.logger('Оригинальная фраза:')
print(ORIGINAL)

encrypted = helpers.get_encrypted(ORIGINAL)

helpers.logger('Зашифрованная фраза:')
print(encrypted)

decrypted = helpers.get_unencrypted(encrypted)

helpers.logger('Расшифрованная фраза:')
print(decrypted)

