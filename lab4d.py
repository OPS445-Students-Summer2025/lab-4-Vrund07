#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_str):
    return input_str[:5]
    # Place code here - refer to function specifics in section below

def last_seven(input_str):
    return input_str[-7:]

    # Place code here - refer to function specifics in section below

def middle_number(input_num):
    input_str = str(input_num)
    return input_str[1:3]

    # Place code here - refer to function specifics in section below

def first_three_last_three(str_a, str_b):
     return str_a[:3] + str_b[-3:]
    # Place code here - refer to function specifics in section below


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))

