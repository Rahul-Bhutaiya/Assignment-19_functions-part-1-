#Write a python program to create a function which expects an unknown number of arguments.

def fun(*t):
    print('Sum of Entered Values :',sum(t))

tuple_var=tuple([int(x) for x in input('Enter Elements Which You Want To Use As An Argument Separated By Comma : ').split(',')])
fun(*tuple_var)