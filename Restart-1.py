#press i for insert mode
from random import randint
from math import sin
print ('math calculator 0.1')
print ('Press 1 for pythagorean therom')
problemselection = int(input())
print ("Your selection is:",problemselection)
if problemselection == 1:
    print ("Which side do you want to calculate?")
    print ("Press 1 for Hypotenuse, Press 2 for the adjacent/opposite side")
    sideselection = int(input())
    if sideselection == 1:
        print("Type the first adjacent length of the triangle")
        adjacentlength1 = int(input())
        print("Type the second adjacent length of the triangle")
        adjacentlength2 = int(input())
        hypotenuselength = pow((pow(adjacentlength1,2) + pow(adjacentlength2,2)),0.5)
        print("This is the length of the hypotenuse:",hypotenuselength)
    if sideselection == 2:
        print("Type the length of the hypotenuse") 
        hypotenuselength = int(input())
        print("Type the length of the other hypotenuse")
        print("l")
        
        
