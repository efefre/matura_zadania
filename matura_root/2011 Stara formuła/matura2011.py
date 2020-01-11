# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2011/R/inf_pr_ii.pdf

import os

def read_txt(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
        return file

def save_txt(file, text):
    with open(file, 'a') as text_file:
        text_file.write(text)