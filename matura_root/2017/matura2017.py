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

    save_txt(filename, '\n\nZadanie 4.2\n')
    save_txt(filename, f'{total_revenue} zł')

    #Ex. 6.1
    filename = '2017/2017_wynik6.txt'
    pixels_data = read_txt('2017/dane.txt')

    if os.path.isfile(filename):
        os.remove(filename)

    pixels_values = []
    for line in pixels_data:
        line_list = line.split(' ')

        for pixel_value in line_list:
            pixels_values.append(int(pixel_value.replace('\n','')))

    brightest = max(set(pixels_values))
    darkest = min(set(pixels_values))

    save_txt(filename, '\n\nZadanie 6.1\n')
    save_txt(filename, f'Najjaśniejszy piksel: {brightest}\nNajciemniejszy piksel: {darkest}')

    #Ex. 6.2
    delete_rows = 0
    pixels_data = read_txt('2017/dane.txt')

    pixels_by_row = []
    for line in pixels_data:
        line_list = line.split(' ')
        pixels_by_row.append((line_list))

    n = 0
    m = -1
    for row in pixels_by_row:
        while n < 320/2:
            if row[n].replace('\n', '') == row[m].replace('\n', ''):
                n += 1
                m -= 1
            else:
                delete_rows += 1
                break
        n = 0
        m = -1

    save_txt(filename, '\n\nZadanie 6.2\n')
    save_txt(filename, f'Minimalna liczba wierszy, które należy usunąć, żeby obraz miał pionową oś symetrii: {delete_rows}')