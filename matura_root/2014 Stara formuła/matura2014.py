# Brak arkusza na stronie CKE
# Arkusz: https://www.dlamaturzysty.info/s/1625/36234-Matura-arkusze-maturalne/133033-Informatyka-poziom-rozszerzony-matura-2014-pytania-i-odpowiedzi.htm

import os
from collections import Counter

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
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

    prime_words = 0

    for word in text_list:
        word_ascii = 0
        for letter in word:
            word_ascii += ord(letter)

        if check_if_prime_number(word_ascii):
            prime_words += 1

    result_5_1 = f'Liczba napisów pierwszych: {prime_words}'

    #Ex.5.2
    previous_ascii = 0
    growing_words = []

    for word in text_list:
        good_word = True
        for letter in word:
            letter_ascii = ord(letter)
            if letter_ascii > previous_ascii:
                previous_ascii = ord(letter)
                good_word = True
            else:
                good_word = False
                break

        previous_ascii = 0
        if good_word:
            growing_words.append(word)

    result_5_2 = ''
    for word in growing_words:
        result_5_2 += word + ' '

    #Ex.5.3
    words_more_than_one = []
    for text, count in Counter(text_list).items():
        if count > 1:
            words_more_than_one.append(text)

    result_5_3 = ''
    for word in words_more_than_one:
        result_5_3 += word + ' '

    save_txt(filename, f'Zadanie 5.1 - {result_5_1}\n'
                       f'Zadanie 5.2 - {result_5_2}\n'
                       f'Zadanie 5.3 - {result_5_3}')
