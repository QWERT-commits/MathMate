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
    #The main menu of the program
    print ('Math Calculator v0.2')
    print ('Press 0 to exit')
    print ("Press 1 to search for what you want :)")
    print ('Press 2 for the geometry section')
    print ('Press 3 for help')
    sectionselection = int(input("Type your selection: "))
    print ("Your selection is:",sectionselection,'\n')
    if sectionselection == 0:
        exit
    elif sectionselection == 1:
        search = input("Enter the text you want to search: ")
        print(next((x for x in Allequation if x["Equation name"] == search), 'Result Not Found'))
    elif sectionselection == 2:
        geometry_section()
        
def geometry_section ():
    print ('Geometry Section: ')
    print ('Press 0 to return')
    print ('Press 1 for Pythagorean therom')
    problemselection = int(input("Type your selection: "))
    print ("Your selection is:",problemselection,'\n')
    if problemselection == 0:
        mainprogram()
    elif problemselection == 1:
        print ("Which side do you want to calculate?")
        print ("Press 1 for Hypotenuse, Press 2 for the adjacent/opposite side")
        sideselection = int(input())
        pythagoreantherom (sideselection)
      
#On Startup
print ('''
 __  __       _   _     __  __       _       
|  \/  | __ _| |_| |__ |  \/  | __ _| |_ ___ 
| |\/| |/ _` | __| '_ \| |\/| |/ _` | __/ _ \\
| |  | | (_| | |_| | | | |  | | (_| | ||  __/
|_|  |_|\__,_|\__|_| |_|_|  |_|\__,_|\__\___|\n''')
Allequation = [
    {'Equation name': 'Pythagorean therom','section':'Geometry','Serial Number':1},
]
mainprogram()