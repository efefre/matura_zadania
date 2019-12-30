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

    text = read_txt('2014 Stara formuła/NAPIS.TXT')
    filename = '2014 Stara formuła/2014_wynik_5.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    text_list = []

    for line in text:
        text_list.append(line.rstrip('\n'))

    # Ex.5.1
    def check_if_prime_number(number):
        i = 2
        while i < number:
            if number % i == 0:
                return False
            i += 1
        return True

