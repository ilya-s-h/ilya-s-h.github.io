'''
3.4. Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования,
использующего сдвиг на определенное количество знаков (шифр Цезаря). Сдвиг задается пользователем.
'''


def encrypt(text: str, offset: int = 1) -> str:
    alphabet_cyr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_lat = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for symbol in text:
        is_letter = False
        for alphabet in [alphabet_cyr, alphabet_lat, alphabet_cyr.upper(), alphabet_lat.upper()]:
            if symbol in alphabet:
                s += alphabet[(alphabet.index(symbol) + offset) % len(alphabet)]
                is_letter = True
        if not is_letter:
            s += symbol
    return s

if __name__ == '__main__':
    text = input('Введите текст: ')
    encrypted_text = encrypt(text)
    print(encrypted_text)
