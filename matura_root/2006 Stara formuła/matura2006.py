# Arkusz: https://cke.gov.pl/images/stories/Matura2006/a2_inform.pdf

import os
from collections import Counter


def read_txt(filename):
    with open(filename, "r") as f:
        file = f.readlines()
        return file


def save_txt(file, text):
    with open(file, "a") as text_file:
        text_file.write(text)


if __name__ == "__main__":
    data = [line.rstrip("\n") for line in read_txt("2006 Stara formuła/dane.txt")]
    filename = "2006 Stara formuła/2006_wynik.txt"

    if os.path.isfile(filename):
        os.remove(filename)

    # Ex.6a
    words_more_than_one = []
    for text, count in Counter(data).items():
        if count > 1:
            words_more_than_one.append(text)

    save_txt(
        filename,
        f"a)\n- W pliku dane.txt jest {len(words_more_than_one)} słów występujących więcej niż jeden raz.\n"
        f"- Słowo o największej liczbie wystąpień: {Counter(data).most_common(1)[0][0]}\n"
        f"- Liczba jego wystąpień: {Counter(data).most_common(1)[0][1]}",
    )
