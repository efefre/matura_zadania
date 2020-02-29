# Arkusz: https://cke.gov.pl/images/stories/mat3_07/inf_pr_cz2.pdf

import os


def save_txt(file, text):
    with open(file, "a") as text_file:
        text_file.write(text)


def digits_sum(number):
    dig_sum = 0
    for num in str(number):
        dig_sum += int(num)

    return dig_sum


def binary_sum(number):
    bin_sum = 0
    for num in f"{number:08b}":
        bin_sum += int(num)
    return bin_sum


def is_super_b_prime_number(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            if len(str(number)) > 1:
                num_sum = digits_sum(number)

                for num in range(2, num_sum):
                    if num_sum % num == 0:
                        break
                else:
                    num_sum = binary_sum(number)
                    for num in range(2, num_sum):
                        if num_sum % num == 0:
                            break
                    else:
                        return True
            else:
                num_sum = binary_sum(number)
                if num_sum > 1:
                    for num in range(2, num_sum):
                        if num_sum % num == 0:
                            break
                    else:
                        return True


def is_prime_number(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
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

    # # Ex.5a
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

    # Ex.5b
    count = 0
    for number in data_2:
        num_sum = 0
        for num in str(number):
            num_sum += int(num)

        if is_prime_number(num_sum):
            count += 1

    print(
        f"W przedziale <100,10000> jest {count} liczb, których suma cyfr jest liczbą pierwszą"
    )

    super_b_sum = is_prime_number(sum(result_a2))

    if super_b_sum:
        print(
            "Suma wszystkich liczb „super B pierwszych” z przedziału <100,10000> jest liczbą pierwszą"
        )
    else:
        print(
            "Suma wszystkich liczb „super B pierwszych” z przedziału <100,10000> NIE jest liczbą pierwszą"
        )
