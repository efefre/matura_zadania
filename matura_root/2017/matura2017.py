# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_od_2015/informatyka/MIN-R2_1P-172.pdf

def read_txt(filename):
    file = open(filename)
    return file

def add_customer(dict, tax_number, year, kg):
    if tax_number in dict.keys():
        if dict[tax_number].get(year):
            dict[tax_number][year] += int(kg)
            dict[tax_number]['total'] += int(kg)
        else:
            dict[tax_number][year] = int(kg)
            dict[tax_number]['total'] += int(kg)
    else:
        dict[tax_number] = {year:int(kg), 'total': int(kg)}
