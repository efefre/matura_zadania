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

    # Ex.6a
    result_6a = 0
    for number in numbers:
        if number[-1] == '0':
            result_6a +=1

    # Ex.6b
    decimal_numbers = [int(number, 2) for number in numbers]
    max_number = max(decimal_numbers)

    result_6b = f'Największa liczba zapisana w systemie dwójkowym: {max_number:b},\n' \
                f'największa liczba zapisana w systemie dziesiętnym: {max_number}'

    # Ex.6c
    count = 0
    sum_number = 0
    for number in numbers:
        if len(number) == 9:
            count += 1
            sum_number += int(number,2)

    result_6c = f'Liczb: {count}, Suma: {sum_number:b}'

    save_txt(filename, f'Zadanie 6a - {result_6a}\n'
                       f'Zadanie 6b - {result_6b}\n'
                       f'Zadanie 6c - {result_6c}')
