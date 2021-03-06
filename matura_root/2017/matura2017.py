# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_od_2015/informatyka/MIN-R2_1P-172.pdf
import os


def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file


def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)


def add_customer(dictionary, tax_num, year_num, kg_sugar):
    if tax_num in dictionary.keys():
        if dictionary[tax_num].get(year_num):
            dictionary[tax_num][year_num] += int(kg_sugar)
            dictionary[tax_num]['total'] += int(kg_sugar)
        else:
            dictionary[tax_num][year_num] = int(kg_sugar)
            dictionary[tax_num]['total'] += int(kg_sugar)
    else:
        dictionary[tax_num] = {year_num: int(kg_sugar), 'total': int(kg_sugar)}


if __name__ == '__main__':
    sugar_data = read_txt('2017/cukier.txt')
    filename = '2017/2017_wynik4.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    customers = {}
    for lp, line in enumerate(sugar_data, 1):
        date_of_sale, tax_number, kg = line.rsplit('\t')
        kg = kg.replace('\n', '')
        year, month, day = date_of_sale.rsplit('-')
        add_customer(customers, tax_number, year, kg)

    # Ex. 4.1
    top_three_total_customer = sorted([[value['total'], key] for key, value in customers.items()], reverse=True)[:3]

    save_txt(filename, '\n\nZadanie 4.1\n')
    for customer in top_three_total_customer:
        total, tax_number = customer
        result = str(tax_number) + ' - ' + str(total) + '\n'
        save_txt(filename, result)

    # Ex. 4.2.
    sugar_price_data = read_txt('2017/cennik.txt')
    sugar_price = {}

    for line in sugar_price_data:
        year, price = line.rsplit('\t')
        price = price.replace('\n', '').replace(',', '.')
        year = year.strip()
        sugar_price[year] = float(price)

    total_revenue = 0
    for year in sugar_price.keys():
        for customer in customers:
            if customers[customer].get(year):
                total_revenue += customers[customer].get(year) * sugar_price[year]

    save_txt(filename, '\n\nZadanie 4.2\n')
    save_txt(filename, f'{total_revenue} zł')

    # Ex. 6.1
    filename = '2017/2017_wynik6.txt'
    pixels_data = read_txt('2017/dane.txt')

    if os.path.isfile(filename):
        os.remove(filename)

    pixels_values = []
    for line in pixels_data:
        line_list = line.split(' ')

        for pixel_value in line_list:
            pixels_values.append(int(pixel_value.replace('\n', '')))

    brightest = max(set(pixels_values))
    darkest = min(set(pixels_values))

    save_txt(filename, '\n\nZadanie 6.1\n')
    save_txt(filename, f'Najjaśniejszy piksel: {brightest}\nNajciemniejszy piksel: {darkest}')

    # Ex. 6.2
    delete_rows = 0
    pixels_data = read_txt('2017/dane.txt')

    pixels_by_row = []
    for line in pixels_data:
        line_list = line.split(' ')
        pixels_by_row.append([int(x.replace('\n', '')) for x in line_list])

    n = 0
    m = -1
    for row in pixels_by_row:
        while n < 320 / 2:
            if row[n] == row[m]:
                n += 1
                m -= 1
            else:
                delete_rows += 1
                break
        n = 0
        m = -1

    save_txt(filename, '\n\nZadanie 6.2\n')
    save_txt(filename,
             f'Minimalna liczba wierszy, które należy usunąć, żeby obraz miał pionową oś symetrii: {delete_rows}')

    # Ex.6.3
    contrast_pix = 0

    n = 0
    while n <= len(pixels_by_row) - 1:
        for m, pixel in enumerate(pixels_by_row[n]):
            if 0 < n < len(pixels_by_row) - 1:
                if 0 < m < len(pixels_by_row[n]) - 1:
                    distance_t = pixel - pixels_by_row[n - 1][m]
                    distance_b = pixel - pixels_by_row[n + 1][m]
                    distance_l = pixel - pixels_by_row[n][m - 1]
                    distance_r = pixel - pixels_by_row[n][m + 1]
                    if distance_t > 128 or distance_t < -128 \
                            or distance_b > 128 or distance_b < -128 \
                            or distance_l > 128 or distance_l < -128 \
                            or distance_r > 128 or distance_r < -128:
                        contrast_pix += 1
                # first column
                elif m == 0:
                    distance_t = pixel - pixels_by_row[n - 1][m]
                    distance_b = pixel - pixels_by_row[n + 1][m]
                    distance_r = pixel - pixels_by_row[n][m + 1]
                    if distance_t > 128 or distance_t < -128 \
                            or distance_b > 128 or distance_b < -128 \
                            or distance_r > 128 or distance_r < -128:
                        contrast_pix += 1
                # last column
                elif m == len(pixels_by_row[n]) - 1:
                    distance_t = pixel - pixels_by_row[n - 1][m]
                    distance_b = pixel - pixels_by_row[n + 1][m]
                    distance_l = pixel - pixels_by_row[n][m - 1]
                    if distance_t > 128 or distance_t < -128 \
                            or distance_b > 128 or distance_b < -128 \
                            or distance_l > 128 or distance_l < -128:
                        contrast_pix += 1
            # first row
            elif n == 0:
                if 0 < m < len(pixels_by_row[n]) - 1:
                    distance_b = pixel - pixels_by_row[n + 1][m]
                    distance_l = pixel - pixels_by_row[n][m - 1]
                    distance_r = pixel - pixels_by_row[n][m + 1]
                    if distance_b > 128 or distance_b < -128 \
                            or distance_l > 128 or distance_l < -128 \
                            or distance_r > 128 or distance_r < -128:
                        contrast_pix += 1
                # first column
                elif m == 0:
                    distance_b = pixel - pixels_by_row[n + 1][m]
                    distance_r = pixel - pixels_by_row[n][m + 1]
                    if distance_b > 128 or distance_b < -128 \
                            or distance_r > 128 or distance_r < -128:
                        contrast_pix += 1
                # last column
                elif m == len(pixels_by_row[n]) - 1:
                    distance_b = pixel - pixels_by_row[n + 1][m]
                    distance_l = pixel - pixels_by_row[n][m - 1]
                    if distance_b > 128 or distance_b < -128 \
                            or distance_l > 128 or distance_l < -128:
                        contrast_pix += 1
            # last row
            elif n == len(pixels_by_row) - 1:
                if 0 < m < len(pixels_by_row[n]) - 1:
                    distance_t = pixel - pixels_by_row[n - 1][m]
                    distance_l = pixel - pixels_by_row[n][m - 1]
                    distance_r = pixel - pixels_by_row[n][m + 1]
                    if distance_t > 128 or distance_t < -128 \
                            or distance_l > 128 or distance_l < -128 \
                            or distance_r > 128 or distance_r < -128:
                        contrast_pix += 1
                # first column
                elif m == 0:
                    distance_t = pixel - pixels_by_row[n - 1][m]
                    distance_r = pixel - pixels_by_row[n][m + 1]
                    if distance_t > 128 or distance_t < -128 \
                            or distance_r > 128 or distance_r < -128:
                        contrast_pix += 1
                # last column
                elif m == len(pixels_by_row[n]) - 1:
                    distance_t = pixel - pixels_by_row[n - 1][m]
                    distance_l = pixel - pixels_by_row[n][m - 1]
                    if distance_t > 128 or distance_t < -128 \
                            or distance_l > 128 or distance_l < -128:
                        contrast_pix += 1
        n += 1

    save_txt(filename, '\n\nZadanie 6.3\n')
    save_txt(filename,
             f'Liczba pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel: {contrast_pix}')

    # Ex.6.4
    max_rows = len(pixels_by_row)
    max_cols = len(pixels_by_row[0])

    row_num = 0
    col_num = 0
    temp_counts = 1
    counts = 0

    while col_num < max_cols:
        while row_num < max_rows:
            if row_num < max_rows - 1:
                if pixels_by_row[row_num][col_num] == pixels_by_row[row_num+1][col_num]:
                    temp_counts += 1
                    row_num += 1
                else:
                    if temp_counts > counts:
                        counts = temp_counts
                        temp_counts = 1
                        row_num += 1
                    else:
                        row_num += 1
                        temp_counts = 1
            else:
                if temp_counts > counts:
                    counts = temp_counts
                    temp_counts = 1
                    row_num = 0
                    col_num += 1
                    break
                else:
                    row_num = 0
                    col_num += 1
                    temp_counts = 1
                    break

    save_txt(filename, '\n\nZadanie 6.4\n')
    save_txt(filename,
             f'Najdłuższa linia pionowa składa się z: {counts} pikseli.')
