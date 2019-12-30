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

    # Ex.4.1
    counter = 0
    for number in numbers_list:
        count_1 = number.count('1')
        count_0 = number.count('0')
        if count_0 > count_1:
            counter += 1

    result_4_1 = counter

    # Ex.4.2
    div_2 = 0
    div_8 = 0

    for number in numbers_list:
        converted_number = int(str(number),2)

        if converted_number % 2 == 0:
            div_2 += 1

        if converted_number % 8 == 0:
            div_8 += 1

    result_4_2 = f'Podzielne przez 2: {div_2}, podzielne przez 8: {div_8}'

