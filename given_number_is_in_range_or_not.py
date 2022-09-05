#Write a python program to create a function to check whether a number falls in a given range.

def check(number):
    range_var=range(2,21,2)
    print('number falls in range' if number in range_var else "number isn't in range")

num=int(input('Enter a Number : '))
check(num)