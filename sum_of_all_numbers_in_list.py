#Write a python program to sum all the numbers in a list.

def sum_of_list(list_var):
    print('Sum of All Numbers in a List is ',sum(list_var))

list_variable=[int(x) for x in input('Enter List Elements Separated By Comma : ').split(',')]
sum_of_list(list_variable)