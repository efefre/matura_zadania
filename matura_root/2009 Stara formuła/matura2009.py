# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2009/informatyka/PR_2.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)


if __name__ == '__main__':
    data = [line.rstrip('\n').split() for line in read_txt('2009 Stara formuła/dane.txt')]
    filename_a = '2009 Stara formuła/2009_zad_5.txt'
    filename_b = '2009 Stara formuła/2009_slowa.txt'

    for filename in (filename_a, filename_b):
        if os.path.isfile(filename):
            os.remove(filename)

    # Ex.5a
    result_5a = 0
    for row in data:
        if row[0] == row[0][::-1]:
            result_5a += 1

        if row[1] == row[1][::-1]:
            result_5a += 1

    #Ex.5b
    result_5b = 0
    for row in data:
        if row[1] in row[0]:
            result_5b += 1

    save_txt(filename_a, f'Zadanie 5a - {result_5a},\n'
                         f'Zadanie 5b - {result_5b}')
