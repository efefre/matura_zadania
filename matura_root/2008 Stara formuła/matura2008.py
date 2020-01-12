# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2008/inform_cz_2.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':
    slowa = [line.rstrip('\n') for line in read_txt('2008 Stara formuła/slowa.txt')]
    filename_a = '2008 Stara formuła/2008_hasla_a.txt'
    filename_b = '2008 Stara formuła/2008_hasla_b.txt'
    filename_c = '2008 Stara formuła/2008_slowa_b.txt'

    for filename in (filename_a, filename_b, filename_c):
        if os.path.isfile(filename):
            os.remove(filename)
