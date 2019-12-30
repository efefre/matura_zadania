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

    #Ex.6.2
    dane_6_2 = read_txt('2016/dane_6_2.txt')
    filename = '2016/2016_wynik_6_2.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    words_list = []

    for line in dane_6_2:
        words_list.append(line.rstrip('\n'))

    def decrypt_cesar(word, k):
        oryginal_word = ''
        for letter in word:
            letter_index = alphabet.index(letter)
            if k//len_alphabet == 0:
                oryginal_letter_index = letter_index - k
            else:
                modulo = k % len_alphabet
                oryginal_letter_index = letter_index - modulo

            oryginal_word += alphabet[oryginal_letter_index]
        return oryginal_word

    oryginal_words = []
    for data in words_list:
        word, k = data.split(' ')
        if k == '':
            error_msg = f"{word} - Uwaga! W pliku wejściowym nie podano liczby k dla tego słowa"
            oryginal_words.append(error_msg)
        else:
            k = int(k)
            oryginal_word = decrypt_cesar(word, k)
            oryginal_words.append(oryginal_word)

    print(oryginal_words)

    save_txt(filename, 'Zadanie 6.2\n')
    for word in oryginal_words:
        save_txt(filename, f'{word}\n')

    # Ex.6.3
    dane_6_3 = read_txt('2016/dane_6_3.txt')
    filename = '2016/2016_wynik_6_3.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    words_list = []

    for line in dane_6_3:
        words_list.append(line.rstrip('\n'))

  def find_wrong_encryption(oryginal_word, encrypted_word):
        word_k = 0
        wrong_encryption_word = []

        len_oryginal = len(oryginal_word)
        len_encrypted = len(encrypted_word)

        if len_oryginal == len_encrypted:
            index = 0
            while index <= len_oryginal - 1:
                letter_oryginal = oryginal_word[index]
                letter_encrypted = encrypted_word[index]

                letter_oryginal_index = alphabet.index(letter_oryginal)
                letter_encrypted_index = alphabet.index(letter_encrypted)

                if letter_encrypted_index > letter_oryginal_index:
                    k = letter_encrypted_index - letter_oryginal_index
                else:
                    k = 26 - letter_oryginal_index + letter_encrypted_index

                if index == 0:
                    word_k = k
                else:
                    if k != word_k:
                        wrong_encryption_word = oryginal_word
                        break

                index += 1

        return wrong_encryption_word
