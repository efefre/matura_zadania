# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2019/formula_od_2015/informatyka/MIN-R2_1P-192.pdf
import os

def read_txt(filename):
    file = open(filename).readlines()
    return file

def save_txt(filename, text):
    with open(filename,'a') as text_file:
        text_file.write(text)

if __name__ == '__main__':
    file = read_txt('liczby.txt')
    filename = '2019_wynik4.txt'

    if os.path.isfile(filename):
        os.remove(filename)

    #Ex. 4.1.
    numbers = []
    for number in file:
        number = number.replace('\n','')
        numbers.append(number)

    sorted_numbers = sorted(numbers)

    result = []
    for number in sorted_numbers:
        if number in result:
            result.append(number)
        else:
            find_x = True
            x = 1
            while find_x == True:
                if 3 ** x > int(number):
                    break
                elif int(number) **(1/x) == 3:
                    result.append(number)
                    find_x = False
                else:
                    x += 1

    save_txt(filename, '\n\nZadanie 4.1\n')
    save_txt(filename, str(len(result)))

# Ex.4.2
    def factorial(n):
        if n < 2:
            return 1
        else:
            return n * factorial(n-1)

    result = []
    for number in numbers:
        sum = 0
        for x in number:
            sum += factorial(int(x))

        if sum == int(number):
            result.append(number)

    save_txt(filename, '\n\nZadanie 4.2\n')
    for number in result:
        save_txt(filename, str(number)+"\n")

# Ex.4.3
    # NWD(num1,num2)
    def find_nwd(num1, num2):

        if num2 > num1:
            num1, num2 = num2, num1

        while num1 % num2 != 0:
            r = num1 % num2
            num1, num2 = num2, r

        return num2
