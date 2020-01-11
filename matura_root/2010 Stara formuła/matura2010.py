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
    filename_a= '2010 Stara formuła/2010_odp_4a.txt'
    filename_b = '2010 Stara formuła/2010_odp_4b.txt'

    for filename in (filename_a, filename_b):
        if os.path.isfile(filename):
            os.remove(filename)

    # Ex. 4a
    for list_words in anagrams:
        if len(list_words[0]) == len(list_words[1]) == len(list_words[2]) == len(list_words[3]) == len((list_words[4])):
            row = f"{str(list_words).replace('[','').replace(']','')}\n"
            row = row.replace("'","")
            save_txt(filename_a, row)




