import random
import string

text = input("Введіть слово: ")

def decrypt(text):
    result = ""
    for i in range(0, len(text), 2):
        result += text[i]
    return result

def encrypt(text):
    result = ""
    for char in text:
        result += char + random.choice(string.ascii_letters)
    return result

encrypted = encrypt(text)
print('Зашифроване слово: ' + encrypted)

decrypted = decrypt(encrypted)
print('Розшифроване слово: ' + decrypted)