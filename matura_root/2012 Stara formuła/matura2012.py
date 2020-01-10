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
    klucze1_file = read_txt('2012 Stara formuła/klucze1.txt')
    filename = '2012 Stara formuła/2012_wynik_4.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    tj_list = [line.rstrip('\n') for line in tj]

    keys1_list = [line.rstrip('\n') for line in klucze1_file]

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


    save_txt(filename, f'Zadanie 4a\n')
    for lp, word in enumerate(tj_list):
        save_txt(filename, f'{encryption(word, keys1_list[lp])}\n')



