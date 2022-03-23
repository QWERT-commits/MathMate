#press i for insert mode
from math import sin
from math import sqrt

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
        print(next((x for x in allequations if x["Equation name"] == search), 'Result Not Found'))
        returnmenu()
    elif sectionselection == 2:
        geometry_section()
    elif sectionselection == 3:
        algebra_section()
    elif sectionselection == 4:
        help()

def help():
    print('List of the problem solver： ')
    print(allequations)

def returnmenu():
    print('Execution completed, returning to home menu... \n')
    mainprogram()
    
#Problem solver for the geometry section
def pythagoreantherom(sideselection):
    if sideselection == 1:
        adjacentlength1 = float(input("Type the first adjacent length of the triangle: "))
        adjacentlength2 = float(input("Type the second adjacent length of the triangle: "))
        hypotenuselength1 = pow((pow(adjacentlength1,2) + pow(adjacentlength2,2)),0.5)
        print("This is the length of the hypotenuse:",hypotenuselength1)
        returnmenu()
    if sideselection == 2: 
        hypotenuselength1 = float(input("Type the length of the hypotenuse: "))
        adjacentlength2 = float(input("Type the length of the other hypotenuse: "))
        hypotenuselength1 = pow((pow(hypotenuselength1,2) - pow(adjacentlength2)),0.5)
        print("This is the length of the other adjacent side:",hypotenuselength1)
        returnmenu()
        
def triangleareafromthreesides():
    Side_1 = float(input('Please type the longest length among the three sides of the triangle: '))
    Side_2 = float(input('Please type the length of the second side: '))
    Side_3 = float(input('Please type the length of the third side: '))
    if pow(Side_2,2) + pow(Side_3,2) == pow (Side_1,2):
        Triangle_Area = 0.5 * Side_2 * Side_3
    else:
        Triangle_Area = 0.5 * Side_3 * pow((pow(Side_2,2) - pow((pow(Side_3,2)+pow(Side_2,2)-pow(Side_1,2))/(2 * Side_3),2)),0.5)
    print('The area of the triangle is:',Triangle_Area)
    returnmenu()
    #Some results are not yet accurate

#Problem solver for the algebra section
def linearfunctiongenerater():
    print('Linear function generator: ')
    print("Please type the two set of coordinate points (x1,y1)(x2,y2)")
    First_Point_X_Value = float(input("Type the x-value of the first point: "))
    First_Point_Y_Value = float(input("Type the y-value of the first point: "))
    Second_Point_X_Value = float(input("Type the x-value of the second point: "))
    Second_Point_Y_Value = float(input("Type the y-value of the second point: "))
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
        
#Sections
def geometry_section ():
    print ('Geometry Section: ')
    print ('Press 0 to return')
    print ('Press 1 for Pythagorean theorem')
    print ('Press 2 for Triangle area from three sides')
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
    elif problemselection == 2:
        print ('Triangle area from three sides:')
        triangleareafromthreesides()

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
allequations = [
     {'Equation name': 'Pythagorean theorem','section': 'Geometry','Serial Number': 1},
     {'Equation name': 'Linear function generator','section': 'Algebra','Serial Number': 1},
     {'Equation name': 'Triangle area from three sides','section': 'Geometry','Serial Number': 2},
]
mainprogram()