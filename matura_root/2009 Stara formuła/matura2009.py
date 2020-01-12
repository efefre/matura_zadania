# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2009/informatyka/PR_2.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)


if __name__ == '__main__':
    data = [line.rstrip('\n').split() for line in read_txt('2009 Stara formuła/dane.txt')]
    filename_a = '2009 Stara formuła/2009_zad_5.txt'
    filename_b = '2009 Stara formuła/2009_slowa.txt'

    for filename in (filename_a, filename_b):
        if os.path.isfile(filename):
            os.remove(filename)

    # Ex.5a
    result_5a = 0
    for row in data:
        if row[0] == row[0][::-1]:
            result_5a += 1

        if row[1] == row[1][::-1]:
            result_5a += 1

    #Ex.5b
    result_5b = 0
    for row in data:
        if row[1] in row[0]:
            result_5b += 1

    #Ex.5c
    result_5c = 0

    for row in data:
        if row[1] in row[0]:
            continue
        else:
            i = 0
            for i in range(0, len(row[1])):
                if row[0][:i] == row[1][-i:] or row[1][:i] == row[0][-i:]:
                    break
            else:
                result_5c +=1

    save_txt(filename_a, f'Zadanie 5a - {result_5a},\n'
                         f'Zadanie 5b - {result_5b},\n'
                         f'Zadanie 5c - {result_5c}')

    #Ex.5d
    result_5d = []
    for row in data:
        if row[1] in row[0]:
            result_5d.append(row[0])
        else:
            for i in range(len(row[1]), 0, -1):
                if row[0][:i] == row[1][-i:]:
                    result_5d.append(row[1][:i]+row[0])
                    break
                elif row[1][:i] == row[0][-i:]:
                    result_5d.append(row[0]+row[1][i:])
                    break
            else:
                result_5d.append(row[0]+row[1])

    for row in result_5d:
        save_txt(filename_b, f'{row}\n')
