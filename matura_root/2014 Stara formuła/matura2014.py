# Brak arkusza na stronie CKE
# Arkusz: https://www.dlamaturzysty.info/s/1625/36234-Matura-arkusze-maturalne/133033-Informatyka-poziom-rozszerzony-matura-2014-pytania-i-odpowiedzi.htm

import os

def read_txt(file):
    file = open(file)
    return file


def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':

    numbers = read_txt('2014/NAPIS.TXT')
    filename = '2014/2014_wynik_5.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    numbers_list = []

    for line in numbers:
        numbers_list.append(line.rstrip('\n'))