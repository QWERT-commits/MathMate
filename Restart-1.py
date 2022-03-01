#press i for insert mode
from random import randint
from math import sin

def pythagoreantherom(sideselection):
    if sideselection == 1:
        adjacentlength1 = int(input("Type the first adjacent length of the triangle: "))
        adjacentlength2 = int(input("Type the second adjacent length of the triangle: "))
        hypotenuselength1 = pow((pow(adjacentlength1,2) + pow(adjacentlength2,2)),0.5)
        print("This is the length of the hypotenuse:",hypotenuselength1)
    if sideselection == 2: 
        hypotenuselength1 = int(input("Type the length of the hypotenuse: "))
        adjece2 = int(input("Type the length of the other hypotenuse: "))
        
    
list1 = ['Press 1 for pythagorean therom']
print ('math calculator 0.1')
print ("Press 0 to search for what you want :)")
print ('Press 1 for pythagorean therom')
problemselection = int(input())
print ("Your selection is:",problemselection)
if problemselection == 0:
    search = input("Enter the text you want to search: ")
elif problemselection == 1:
    print ("Which side do you want to calculate?")
    print ("Press 1 for Hypotenuse, Press 2 for the adjacent/opposite side")
    sideselection = int(input())
    pythagoreantherom (sideselection)
        
        
        
