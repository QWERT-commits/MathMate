#press i for insert mode
from random import randint
from math import sin

#The main menu of the program
def mainprogram():
    print ('Math Calculator v0.2')
    print ('Press 0 to exit')
    print ("Press 1 to search for what you want :)")
    print ('Press 2 for the geometry section')
    print ('Press 3 for the algebra section')
    print ('Press 4 for help')
    sectionselection = int(input("Type your selection: "))
    print ("Your selection is:",sectionselection,'\n')
    if sectionselection == 0:
        exit
    elif sectionselection == 1:
        search = input("Enter the text you want to search: ")
        print(next((x for x in allequation if x["Equation name"] == search), 'Result Not Found'))
    elif sectionselection == 2:
        geometry_section()
    elif sectionselection == 3:
        algebra_section()
    elif sectionselection == 4:
        help()

def help():
    print('List of the problem solver')

def returnmenu():
    print('Execution completed, returning to home menu... \n')
    mainprogram()
    
#Problem solver for the geometry section
def pythagoreantherom(sideselection):
    if sideselection == 1:
        adjacentlength1 = int(input("Type the first adjacent length of the triangle: "))
        adjacentlength2 = int(input("Type the second adjacent length of the triangle: "))
        hypotenuselength1 = pow((pow(adjacentlength1,2) + pow(adjacentlength2,2)),0.5)
        print("This is the length of the hypotenuse:",hypotenuselength1)
        returnmenu()
    if sideselection == 2: 
        hypotenuselength1 = int(input("Type the length of the hypotenuse: "))
        adjacentlength2 = int(input("Type the length of the other hypotenuse: "))
        hypotenuselength1 = pow((pow(hypotenuselength1,2) - pow(adjacentlength2)),0.5)
        print("This is the length of the other adjacent side:",hypotenuselength1)
        returnmenu()

#Problem solver for the algebra section
def linearfunctiongenerater():
    print('Linear function generator: ')
    print("Please type the two set of coordinate points (x1,y1)(x2,y2)")
    First_Point_X_Value = int(input("Type the x-value of the first point: "))
    First_Point_Y_Value = int(input("Type the y-value of the first point: "))
    Second_Point_X_Value = int(input("Type the x-value of the second point: "))
    Second_Point_Y_Value = int(input("Type the y-value of the second point: "))
    Slope = (Second_Point_Y_Value - First_Point_Y_Value)/(Second_Point_X_Value - First_Point_X_Value)
    Y_Intercept = ((Second_Point_X_Value * First_Point_Y_Value) - (Second_Point_Y_Value * First_Point_X_Value))/(Second_Point_X_Value - First_Point_X_Value)
    X_Intercept = ((Second_Point_Y_Value * First_Point_X_Value) - (Second_Point_X_Value * First_Point_Y_Value))/(Second_Point_Y_Value - First_Point_Y_Value)
    if Y_Intercept >=0:
        print('Full linear equation:',"y = x * (",Slope,") +",Y_Intercept)
    elif Y_Intercept <0:
        print('Full linear equation:',"y = x * (",Slope,") -",abs(Y_Intercept))
    print('Y_Intercept',Y_Intercept)
    print('X_Intercept',X_Intercept)
    returnmenu()
        
def geometry_section ():
    print ('Geometry Section: ')
    print ('Press 0 to return')
    print ('Press 1 for Pythagorean theorem')
    problemselection = int(input("Type your selection: "))
    print ("Your selection is:",problemselection,'\n')
    if problemselection == 0:
        mainprogram()
    elif problemselection == 1:
        print ('Pythagorean theorem: ')
        print ("Which side do you want to calculate?")
        print ("Press 1 for Hypotenuse, Press 2 for the adjacent/opposite side")
        sideselection = int(input())
        pythagoreantherom (sideselection)

def algebra_section ():
    print ('Algebra Section:')
    print ('Press 0 to return')
    print ('Press 1 for linear function generator')
    problemselection = int(input("Type your selection: "))
    print ("Your selection is:",problemselection,'\n')
    if problemselection == 0:
        mainprogram()
    elif problemselection ==1:
        linearfunctiongenerater()
      
#On Startup
print ('''
 __  __       _   _     __  __       _       
|  \/  | __ _| |_| |__ |  \/  | __ _| |_ ___ 
| |\/| |/ _` | __| '_ \| |\/| |/ _` | __/ _ \\
| |  | | (_| | |_| | | | |  | | (_| | ||  __/
|_|  |_|\__,_|\__|_| |_|_|  |_|\__,_|\__\___|\n''')
allequation = [
    {'Equation name': 'Pythagorean theorem','section':'Geometry','Serial Number':1},
    {'Equation name': 'Linear function generator','section': 'Algebra','Serial Number':1}
]
mainprogram()