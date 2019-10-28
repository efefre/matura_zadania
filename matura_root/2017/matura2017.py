# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_od_2015/informatyka/MIN-R2_1P-172.pdf
import os

def read_txt(filename):
    file = open(filename)
    return file

def save_txt(filename, text):
    with open(filename,'a') as text_file:
        text_file.write(text)

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

if __name__ == '__main__':
    sugar_data = read_txt('2017/cukier.txt')
    filename = '2017/2017_wynik4.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    customers = {}
    for lp, line in enumerate(sugar_data,1):
        date_of_sale, tax_number, kg = line.rsplit('\t')
        kg = kg.replace('\n','')
        year, month, day = date_of_sale.rsplit('-')
        add_customer(customers,tax_number, year, kg)

    #Ex. 4.1
    top_three_total_customer = sorted([[value['total'], key] for key, value in customers.items()], reverse=True)[:3]

    save_txt(filename, '\n\nZadanie 4.1\n')
    for customer in top_three_total_customer:
        total, tax_number = customer
        result = str(tax_number) + ' - ' + str(total) + '\n'
        save_txt(filename, result)

    #Ex. 4.2.
    sugar_price_data = read_txt('2017/cennik.txt')
    sugar_price = {}

    for line in sugar_price_data:
        year, price = line.rsplit('\t')
        price = price.replace('\n','').replace(',','.')
        year = year.strip()
        sugar_price[year] = float(price)

    total_revenue = 0
    for year in sugar_price.keys():
        for customer in customers:
            if customers[customer].get(year):
                total_revenue += customers[customer].get(year) * sugar_price[year]
