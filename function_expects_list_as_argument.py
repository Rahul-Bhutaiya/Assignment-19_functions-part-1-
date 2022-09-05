#Write a python program to create a function which expects a list as an argument.

def fun(list):
    print('Entered List as an Argument :',list,type(list))

list_var=[eval(x) for x in input('Enter List Elements Separated By Comma : ').split(',')]
fun(list_var)