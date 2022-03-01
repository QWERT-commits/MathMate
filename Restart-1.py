#press i for insert mode
from random import randint
from math import sin

def returnmenu():
    mainprogram()
    
def pythagoreantherom(sideselection):
    if sideselection == 1:
        adjacentlength1 = int(input("Type the first adjacent length of the triangle: "))
        adjacentlength2 = int(input("Type the second adjacent length of the triangle: "))
        hypotenuselength1 = pow((pow(adjacentlength1,2) + pow(adjacentlength2,2)),0.5)
        print("This is the length of the hypotenuse:",hypotenuselength1)
        print('Execution completed, returning to homemenu... \n')
        returnmenu()
    if sideselection == 2: 
        hypotenuselength1 = int(input("Type the length of the hypotenuse: "))
        adjacentlength2 = int(input("Type the length of the other hypotenuse: "))
        hypotenuselength1 = pow((pow(hypotenuselength1,2) - pow(adjacentlength2)),0.5)
        print("This is the length of the other adjacent side:",hypotenuselength1)
        print('Execution completed, returning to homemenu... \n')
        returnmenu()
        
def mainprogram():  
    list = ['Press 1 for pythagorean therom']
    print ('math calculator 0.1')
    print ('Press 0 to exit')
    print ("Press 1 to search for what you want :)")
    print ('Press 2 for pythagorean therom')
    problemselection = int(input("Type your selection: "))
    print ("Your selection is:",problemselection)
    if problemselection == 0:
        exit
    elif problemselection == 1:
        search = input("Enter the text you want to search: ")
    elif problemselection == 2:
        print ("Which side do you want to calculate?")
        print ("Press 1 for Hypotenuse, Press 2 for the adjacent/opposite side")
        sideselection = int(input())
        pythagoreantherom (sideselection)
       
mainprogram() 
        
        
