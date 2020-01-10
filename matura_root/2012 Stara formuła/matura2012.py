# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2012/maj/infor/a2_pr.pdf

import os
import string


def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':
    tj = read_txt('2012 Stara formuła/tj.txt')
    sz = read_txt('2012 Stara formuła/sz.txt')
    klucze1_file = read_txt('2012 Stara formuła/klucze1.txt')
    klucze2_file = read_txt('2012 Stara formuła/klucze2.txt')
    filename_a = '2012 Stara formuła/2012_wynik_4a.txt'
    filename_b = '2012 Stara formuła/2012_wynik_4b.txt'

    for filename in (filename_a, filename_b):
        if os.path.isfile(filename):
            os.remove(filename)

    tj_list = [line.rstrip('\n') for line in tj]
    keys1_list = [line.rstrip('\n') for line in klucze1_file]

    sz_list = [line.rstrip('\n') for line in sz]
    keys2_list = [line.rstrip('\n') for line in klucze2_file]

    alphabet = list(string.ascii_uppercase)

    # Ex. 4a
    def encryption(word, key):
        result = []

        for lp, letter in enumerate(word):
            letter_code = ord(letter)
            key_letter = key[lp % len(key)]
            key_letter_number = 1 + alphabet.index(key_letter)
            encrypted_letter_code = letter_code + key_letter_number

            if encrypted_letter_code > 90:
                encrypted_letter_code = encrypted_letter_code - 26
                result.append(chr(encrypted_letter_code))
            else:
                result.append(chr(encrypted_letter_code))

        return ''.join(result)

    save_txt(filename_a, f'Zadanie 4a\n')
    for lp, word in enumerate(tj_list):
        save_txt(filename_a, f'{encryption(word, keys1_list[lp])}\n')


    # Ex. 4b
    def decrytpion(word, key):
        result = []

        for lp, letter in enumerate(word):
            letter_code = ord(letter)
            key_letter = key[lp % len(key)]
            key_letter_number = 1 + alphabet.index(key_letter)
            decrypted_letter_code = letter_code - key_letter_number

            if decrypted_letter_code < 65:
                decrypted_letter_code = decrypted_letter_code + 26
                result.append(chr(decrypted_letter_code))
            else:
                result.append(chr(decrypted_letter_code))

        return ''.join(result)


    save_txt(filename_b, f'Zadanie 4b\n')
    for lp, word in enumerate(sz_list):
        save_txt(filename_b, f'{decrytpion(word, keys2_list[lp])}\n')
