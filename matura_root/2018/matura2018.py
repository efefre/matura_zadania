# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2018/formula_od_2015/informatyka/MIN-R2_1P-182.pdf
import string
import os

def read_txt(filename):
    file = open(filename).readlines()
    return file

def save_txt(filename, text):
    with open(filename,'a') as text_file:
        text_file.write(text)

def word_and_number_of_unique_characters(text):
    return [text.rstrip(), len(set(text.rstrip()))]

def create_alphabet_list():
    return list(string.ascii_uppercase)

def count_distance_between_letters(text, alphabet):
    alphabet_position = []

    for character in text.rstrip():
        alphabet_position.append(alphabet.index(character.upper()))

    sorted_alphabet_position = sorted(alphabet_position)


    if sorted_alphabet_position[-1] - sorted_alphabet_position[0] <= 10:
        return(text.rstrip())



if __name__ == '__main__':
    file = read_txt('2018/sygnaly.txt')
    filename = '2018/2018_wynik4.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    # Ex.4.1
    result = ""
    for i in (file[39::40]):
        result += i[9]

    print(result)

    save_txt(filename, '\n\nZadanie 4.1\n')
    save_txt(filename,result)

    # Ex. 4.2
    words_with_unique_characters = []
    for word in file:
        words_with_unique_characters.append(word_and_number_of_unique_characters(word))

    sorted_list = sorted(words_with_unique_characters, key=lambda line: line[1], reverse=True)
    result = f'{sorted_list[0][0]} - {sorted_list[0][1]}'
    print(result)

    save_txt(filename, '\n\nZadanie 4.2\n')
    save_txt(filename, result)
    # Ex. 4.3
    alphabet = create_alphabet_list()

    result = []
    for word in file:
        result.append(count_distance_between_letters(word, alphabet))

    save_txt(filename, '\n\nZadanie 4.3\n')
    for word in result:
        if word:
            print(word)
            word = word + '\n'
            save_txt(filename, word)

