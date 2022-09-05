#Write a python program to create a function that finds a maximum of four numbers.

def maximum(numbers):
    print('Enter Four[4] Numbers Only...') if len(numbers)>4 or len(numbers)<4 else print('Maximum out of Four Entered Numbers :',max(numbers))

list_of_numbers=[int(x) for x in input('Enter Four Numbers Separated By Comma : ').split(',')]        
maximum(list_of_numbers)