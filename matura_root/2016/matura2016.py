# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_od_2015/MIN-R2_1P-162.pdf
import os
import string

def read_txt(file):
    file = open(file)
    return file


def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':
    #Ex.6.1
    dane_6_1 = read_txt('2016/dane_6_1.txt')
    filename = '2016/2016_wynik_6_1.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    words_list = []

    for line in dane_6_1:
        words_list.append(line.rstrip('\n'))
