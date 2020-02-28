# Arkusz: https://cke.gov.pl/images/stories/mat3_07/inf_pr_cz2.pdf

import os


def save_txt(file, text):
    with open(file, "a") as text_file:
        text_file.write(text)


def digits_sum(number):
    sum = 0
    for num in str(number):
        sum += int(num)

    return sum


def binary_sum(number):
    sum = 0
    for num in f"{number:08b}":
        sum += int(num)
    return sum


def is_super_b_prime_number(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            if len(str(number)) > 1:
                sum = digits_sum(number)

                for num in range(2, sum):
                    if sum % num == 0:
                        break
                else:
                    sum = binary_sum(number)
                    for num in range(2, sum):
                        if sum % num == 0:
                            break
                    else:
                        return True
            else:
                sum = binary_sum(number)
                if sum > 1:
                    for num in range(2, sum):
                        if sum % num == 0:
                            break
                    else:
                        return True


if __name__ == "__main__":

    filename_a = "2007 Stara formuła/2007_1.txt"
    filename_b = "2007 Stara formuła/2007_2.txt"
    filename_c = "2007 Stara formuła/2007_3.txt"

    for filename in (filename_a, filename_b, filename_c):
        if os.path.isfile(filename):
            os.remove(filename)

    # Ex.5a
    data_1 = range(2, 1001)
    data_2 = range(100, 10001)
    data_3 = range(1000, 100001)

    result_a1 = list(filter(is_super_b_prime_number, data_1))
    for number in result_a1:
        save_txt(filename_a, f"{str(number)}\n")

    result_a2 = list(filter(is_super_b_prime_number, data_2))
    for number in result_a2:
        save_txt(filename_b, f"{str(number)}\n")

    result_a3 = list(filter(is_super_b_prime_number, data_3))
    for number in result_a3:
        save_txt(filename_c, f"{str(number)}\n")

    print(
        f"Liczba wystąpień liczb „super B pierwszych” w przedziale <2,1000>: {len(result_a1)}\n"
        f"Liczba wystąpień liczb „super B pierwszych” w przedziale <100,10000>: {len(result_a2)}\n"
        f"Liczba wystąpień liczb „super B pierwszych” w przedziale <1000,100000>: {len(result_a3)}\n"
    )

