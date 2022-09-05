#Write a python program to create a function to check whether a given number is even or odd.

def odevn(number):
    (print('Odd Number' if number%2 else 'Even Number')) if number else print('Enter Valid Number')

num=int(input('Enter a Number : '))
odevn(num)