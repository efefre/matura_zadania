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

    alphabet = list(string.ascii_uppercase)
    len_alphabet = len(alphabet)

    k = 107

    words_list_cesar = []

    for word in words_list:
        new_word = ''
        for letter in word:
            letter_index = alphabet.index(letter)
            if k//len_alphabet == 0:
                dist_end_alph = len_alphabet - letter_index - 1
                new_letter = k - dist_end_alph
                new_letter_index = new_letter - 1
            else:
                modulo = k % len_alphabet
                dist_end_alph = len_alphabet - letter_index - 1
                new_letter = modulo - dist_end_alph
                new_letter_index = new_letter - 1
            new_word += alphabet[new_letter_index]
        print(word, '>', new_word)
        words_list_cesar.append(new_word)

    save_txt(filename, 'Zadanie 6.1\n')
    for word in words_list_cesar:
        save_txt(filename, f'{word}\n')
