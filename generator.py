import random
import string

general_letters = string.ascii_letters
upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase

ul_code_l = []
lu_code_l = []
un_code_l = []


def gencode(name):
    for i in range(2):

        ## LU code is a code generated by a Lowercase ascii letter followed by an Uppercase ascii letter. ##

        global lu_code
        lu_code = random.choice(lower_letters) + random.choice(upper_letters)

        ## UL code is a code generated by an Uppercase ascii letter followed by a Lowercase ascii letter. ##

        global ul_code
        ul_code = random.choice(upper_letters) + random.choice(lower_letters)

        ## UN code is a unique code made by 10 random ascii letters and random numbers. ##
        for j in range(10):
            un_code = random.choice(general_letters) + str(random.randint(0,9))
            un_code_l.append(un_code)
        
        lu_code_l.append(lu_code)
        ul_code_l.append(ul_code)
    un = ''.join(un_code_l)
    print(f'{lu_code_l[i]}_{ul_code_l[i]}')
    print(f"{lu_code}_{name}_{ul_code}_{un}")