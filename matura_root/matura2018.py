# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2018/formula_od_2015/informatyka/MIN-R2_1P-182.pdf

def read_txt(filename):
    file = open(filename).readlines()
    return file

def save_txt(filename, text):
    with open(filename,'w') as text_file:
        text_file.write(text)


if __name__ == '__main__':
    file = read_txt('sygnaly.txt')

    result = ""
    for i in (file[39::40]):
        result += i[9]

    print(result)
