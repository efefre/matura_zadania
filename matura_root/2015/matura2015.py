# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/MIN-R2_1P-152.pdf

import os
import string

def read_txt(file):
    file = open(file)
    return file


def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':

    numbers = read_txt('2015/liczby.txt')
    filename = '2015/2015_wynik_4.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    numbers_list = []

    for line in numbers:
        numbers_list.append(line.rstrip('\n'))
