# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2011/R/inf_pr_ii.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':
    numbers = read_txt('2011 Stara formuła/liczby.txt')
    filename= '2011 Stara formuła/2011_wynik_6.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    numbers = [line.rstrip('\n') for line in numbers]
