# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2019/formula_od_2015/informatyka/MIN-R2_1P-192.pdf
def read_txt(filename):
    file = open(filename).readlines()
    return file

def save_txt(filename, text):
    with open(filename,'a') as text_file:
        text_file.write(text)
