# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2013/informatyka_PR_2.pdf

import os

def read_txt(file):
    file = open(file)
    return file


def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':

    numbers = read_txt('2013 Stara formuła/dane.txt')
    filename = '2013 Stara formuła/2013_wynik_6.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    numbers_list = []

    for line in numbers:
        numbers_list.append(line.rstrip('\n'))