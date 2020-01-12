# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2008/inform_cz_2.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':
    words = [line.rstrip('\n') for line in read_txt('2008 Stara formuła/slowa.txt')]
    filename_a = '2008 Stara formuła/2008_hasla_a.txt'
    filename_b = '2008 Stara formuła/2008_hasla_b.txt'
    filename_c = '2008 Stara formuła/2008_slowa_b.txt'

    for filename in (filename_a, filename_b, filename_c):
        if os.path.isfile(filename):
            os.remove(filename)

    # Ex.5a
    passwords_a = [word[::-1] for word in words]
    passwords_len = list(map(lambda x: len(x), passwords_a))

    combine = list(zip(passwords_a,passwords_len))
    longest_password = max(combine, key=lambda x: x[1])
    shortest_password = min(combine, key=lambda x: x[1])


    for password in passwords_a:
        save_txt(filename_a, f'{password}\n')



    save_txt(filename_c, f"Najdłuższe hasło: {longest_password[0]} {longest_password[1]},\n"
                         f"najkrótsze hasło: {shortest_password[0]} {shortest_password[1]}" )
