# Arkusz: https://cke.gov.pl/images/stories/Matura2005/inf_a2.pdf

import os


def read_txt(filename):
    with open(filename, "r") as f:
        file = f.readlines()
        return file


def save_txt(file, text):
    with open(file, "a") as text_file:
        text_file.write(text)


def find_best_sum(data):
    present_sum = 0
    best_sum = None
    for i in data:
        if not best_sum:
            best_sum = i

        present_sum += i

        if present_sum < 0:
            present_sum = 0

        best_sum = max(present_sum, best_sum)

    return best_sum


if __name__ == "__main__":
    data_1 = [
        int(line.rstrip("\n")) for line in read_txt("2005 Stara formuła/dane5-1.txt")
    ]
    data_2 = [
        int(line.rstrip("\n")) for line in read_txt("2005 Stara formuła/dane5-2.txt")
    ]
    data_3 = [
        int(line.rstrip("\n")) for line in read_txt("2005 Stara formuła/dane5-3.txt")
    ]

    filename = "2005 Stara formuła/raport5.txt"

    if os.path.isfile(filename):
        os.remove(filename)

    # Ex.5a
    data_a = [1, -2, 6, -5, 7, -3]
    data_a_1 = [1, -2, 2, 2, 2, -5, 3, 3, 1, -3]

    result_data_a = find_best_sum(data_a)
    result_data_a_1 = find_best_sum(data_a_1)

    if result_data_a_1 == result_data_a:
        result_data_a_1_description = "Najlepsza suma drugiego ciągu jest taka sama jak najlepsza suma pierwszego ciągu."
    elif result_data_a_1 > result_data_a:
        result_data_a_1_description = "Najlepsza suma drugiego ciągu jest większa od najlepszej sumy pierwszego ciągu."
    else:
        result_data_a_1_description = "Najlepsza suma drugiego ciągu jest mniejsza od najlepszej sumy pierwszego ciągu."

    save_txt(
        filename, f"a)\n- {result_data_a}\n" f"- {result_data_a_1_description}\n\n"
    )

    # Ex. 5b
    result_data_1 = find_best_sum(data_1)
    save_txt(filename, f"b)\n- {result_data_1}\n")
    result_data_2 = find_best_sum(data_2)
    save_txt(filename, f"- {result_data_2}\n")
    result_data_3 = find_best_sum(data_3)
    save_txt(filename, f"- {result_data_3}\n")
