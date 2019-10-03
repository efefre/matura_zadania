# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2018/formula_od_2015/informatyka/MIN-R2_1P-182.pdf

def read_txt(filename):
    file = open(filename).readlines()
    return file

def save_txt(filename, text):
    with open(filename,'w') as text_file:
        text_file.write(text)

def word_and_number_of_unique_characters(text):
    return [text.rstrip(), len(set(text.rstrip()))]


if __name__ == '__main__':
    file = read_txt('sygnaly.txt')

    # Ex.4.1
    result = ""
    for i in (file[39::40]):
        result += i[9]

    print(result)

    save_txt('wynik-4_1.txt',result)

    # Ex. 4.2
    words_with_unique_characters = []
    for word in file:
        words_with_unique_characters.append(word_and_number_of_unique_characters(word))

    sorted_list = sorted(words_with_unique_characters, key=lambda line: line[1], reverse=True)

    print(sorted_list[0][0], sorted_list[0][1])
