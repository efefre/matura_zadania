# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2013/informatyka_PR_2.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
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

    # Ex.6a
    result_6a = 0
    for number in numbers_list:
        if number[0] == number[-1]:
            result_6a += 1

    # Ex.6b
    def convert_to_decimal(number):
        converted_number = int(str(number),8)
        return str(converted_number)

    result_6b = 0
    for number in numbers_list:
        converted_number = convert_to_decimal(number)
        if converted_number[0] == converted_number[-1]:
            result_6b += 1

    # Ex.6c
    def check_number(number):
        good_number = True
        previous_number = 0

        for num in str(number):
            if int(num) >= previous_number:
                previous_number = int(num)
                good_number = True
            else:
                good_number = False
                break

        return good_number

    checked_numbers = []
    for number in numbers_list:
        check = check_number(number)
        if check:
            checked_numbers.append(int(number))

    max_num = max(checked_numbers)
    min_num = min(checked_numbers)

    result_6c = f'Spełniony warunek: {len(checked_numbers)}, najmniejsza liczba to: {min_num}, największa to: {max_num}'

    save_txt(filename, f'Zadanie 6a - {result_6a}\n'
                       f'Zadanie 6b - {result_6b}\n'
                       f'Zadanie 6c - {result_6c}')