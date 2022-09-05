#Write a python program to multiply all the numbers in a list.

def multiply_list(list_var):
    mul=1
    for x in list_var:
        mul*=x 
    return mul

list_variable=[int(x) for x in input('Enter Numbers Separated By Comma : ').split(',')]
mul=multiply_list(list_variable)
print('Multiplyied  All The Numbers of List :',mul)