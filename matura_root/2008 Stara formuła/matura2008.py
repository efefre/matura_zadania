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
    filename_c = '2008 Stara formuła/2008_slowa_a.txt'
    filename_d = '2008 Stara formuła/2008_slowa_b.txt'

    for filename in (filename_a, filename_b, filename_c, filename_d):
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

    #Ex.5b
    passwords_b = []
    for word in words:
        for i in range(len(word), 0, -1):
            if word[:i] == word[:i][::-1]:
                w1 = word[:i]
                w2 = word[i::][::-1]
                passwords_b.append(w2+word)
                break
            else:
                continue

    passwords_b_len = list(map(lambda x: len(x), passwords_b))
    combine_b_with_len = list(zip(passwords_b, passwords_b_len))

    result_5b_1 = list(filter(lambda x: x[1] == 12, combine_b_with_len))

    result_5b_1 = ", ".join(list(map(lambda x: x[0], result_5b_1)))
    result_5b_2_max = max(combine_b_with_len, key=lambda x: x[1])
    result_5b_2_min = min(combine_b_with_len, key=lambda x: x[1])

    result_5b_3 = 0
    for password in passwords_b:
        result_5b_3 += len(password)


    for password in passwords_b:
        save_txt(filename_b, f'{password}\n')

    save_txt(filename_d, f'1 - {result_5b_1}\n'
                         f'2 - najdłuższe: {result_5b_2_max[0]}, najkrótsze: {result_5b_2_min[0]}\n'
                         f'3 - {result_5b_3}')
