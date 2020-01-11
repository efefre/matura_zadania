# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2010/Informatyka/pr_ii.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':
    anagrams = [line.rstrip('\n').split() for line in read_txt('2010 Stara formuła/anagram.txt')]
    filename= '2010 Stara formuła/2010_wynik_6.txt'

    if os.path.isfile(filename):
        os.remove(filename)
