# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2012/maj/infor/a2_pr.pdf

import os

def read_txt(file):
    file = open(file)
    return file


def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':

    tj = read_txt('2012 Stara formuła/tj.txt')
    klucze1 = read_txt('2012 Stara formuła/klucze1.txt')
    filename = '2013 Stara formuła/2013_wynik_6.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    tj_list = []

    for line in tj:
        tj_list.append(line.rstrip('\n'))

    keys1_list = []

    for line in klucze1:
        keys1_list.append(line.rstrip('\n'))
