import math
import sys
import numpy as np
#Module used: math | pynput

#The main menu of the program
def main_program():
    print ('''
Math Calculator v0.7.４
Press 0 for exit
Press 1 for search
Press 2 for the geometry section
Press 3 for the algebra section
Press 4 for advanced mathematics section
Press 5 for others section
Press 6 for help''')
#    try:
    section_selection = int(input("Type your selection: "))
#    print ("Your selection is:",section_selection,'\n')
    print ('\n')
    current_menu_locator(section_selection,-1)
    if section_selection == 0:
        quit()
    elif section_selection == 1:
        search()
    elif section_selection == 2:
        geometry_section()
    elif section_selection == 3:
        algebra_section()
    elif section_selection == 4:
        advanced_mathematics_section()
    elif section_selection == 5:
        others_section()
    elif section_selection == 6:
        help() 
#    except:
#        print ("\nUnknown error, please check if you enter the correct input as requested!\n")
#        main_program()

def search():
    search = input("Enter the text you want to search: ")
    equation_search_result = False
    section_search_result = False
    serial_number_search_result = False
    print (' ')
    print ("These are the search results for equation '" + search + "':")
    for i in all_equations: 
        if i['Equation name'] == search :
            print (i)
            equation_search_result = True
    if equation_search_result is False:
        print ("No results has been found regarding to the '" + search + "' equation\n")
    else:
        print (' ')
    print ("These are the search results for section '" + search + "':")
    for i in all_equations: 
        if i['Section'] == search :
            print (i)
            section_search_result = True
    if section_search_result is False:
        print ("No results has been found regarding to the '" + search + "' section\n")
    else:
        print (' ')
    print ("These are the search results for serial number '" + search + "':")
    for i in all_equations:
        if search.isdigit() == True and i['Serial number'] == int(search):
            print (i)
            serial_number_search_result = True
    if serial_number_search_result is False:
        print ("No results has been found regarding to the serial number '" + search + "'\n")
    else:
        print (' ')
    return_to_menu()  

def help():
    print('List of the problem solver： ')
    for i in all_equations: 
        if i['Section'] == 'Geometry' :
            print (i)
    for i in all_equations:
        if i['Section'] == 'Algebra' :
            print (i)
    return_to_menu()

def return_to_menu():
    global actual_menu_number
    actual_menu_number = menu_number_save - 1
    print('Execution completed, returning to',get_key_from_value(actual_menu_number),'......')
    if menu_number_save == 2:
        geometry_section()
    elif menu_number_save == 3:
        algebra_section()
    elif menu_number_save == 4:
        advanced_mathematics_section()
    elif menu_number_save == 5:
        others_section()
    else:
        main_program()

def get_key_from_value(val):
    for key, value in menu_number.items():
         if val == value:
             return key
    return "Main menu"
    
def current_menu_locator(menu_number_static,submenu_number_static):
    global menu_number_save
    global submenu_number_save
    if menu_number_static != -1:
        menu_number_save = menu_number_static
    if submenu_number_static != -1:
        submenu_number_save = submenu_number_static
    
#Problem solver for the geometry section
def pythagorean_theorem(side_selection):
    if side_selection == 1:
        adjacent_length_1 = float(input("Type the first adjacent length of the triangle: "))
        adjacent_length_2 = float(input("Type the second adjacent length of the triangle: "))
        hypotenuse_length_1 = pow((pow(adjacent_length_1,2) + pow(adjacent_length_2,2)),0.5)
        print("This is the length of the hypotenuse:",hypotenuse_length_1)
        return_to_menu()
    if side_selection == 2: 
        hypotenuse_length_1 = float(input("Type the length of the hypotenuse: "))
        adjacent_length_2 = float(input("Type the length of the other hypotenuse: "))
        hypotenuse_length_1 = pow((pow(hypotenuse_length_1,2) - pow(adjacent_length_2,2)),0.5)
        print("This is the length of the other adjacent side:",hypotenuse_length_1)
        return_to_menu()
        
def triangle_area_from_three_sides():
    Side_1 = float(input('Please type the longest length among the three sides of the triangle: '))
    Side_2 = float(input('Please type the length of the second side: '))
    Side_3 = float(input('Please type the length of the third side: '))
    if pow(Side_2,2) + pow(Side_3,2) == pow (Side_1,2):
        Triangle_Area = 0.5 * Side_2 * Side_3
    else:
        Triangle_Area = 0.5 * Side_3 * pow((pow(Side_2,2) - pow((pow(Side_3,2)+pow(Side_2,2)-pow(Side_1,2))/(2 * Side_3),2)),0.5)
    print('The area of the triangle is:',Triangle_Area)
    return_to_menu()
    #Some results are not yet accurate

#Problem solver for the algebra section
def linear_function_generator():
    print('Linear function generator: ')
    print("Please type the two set of coordinate points (x1,y1),(x2,y2)")
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
    First_Point_X_Value = 0
    First_Point_Y_Value = 0
    Second_Point_X_Value = 0
    Second_Point_Y_Value = 0
    return_to_menu()
    
def arithmetic_progression_calculator():
    print('Arithmetic Progression Calculator')
    print("Please input the three value of the standard form of arithmetic progression calculator:\n(a + 0*b) + (a + 1*b) +...+ (a + n*b)")
    a = float(input('Please type the value of a: '))
    b = float(input('Please type the value of b: '))
    n = float(input('Please type the value of n: '))
    sum = (1+n)*(a+(n*b*0.5))
    print('The sum of this sequence is: ',sum)
    return_to_menu()
    
def quadratic_equation_calculator ():
    print('Quadratic Equation Calculator')
    print('Please input the three value of the standard form of quadratic equation:\na * x² + b * x + c = 0')
    a = float(input('Type the value of a: '))
    b = float(input('Type the value of b: '))
    c = float(input('Type the value of c: '))
    Solution_1 = (-b+pow(pow(b,2)+4*a*c,0.5))/2*a
    Solution_2 = (-b-pow(pow(b,2)+4*a*c,0.5))/2*a
    print ('The first solution is: ',Solution_1)
    print ('The second solution is: ',Solution_2)
    return_to_menu()
    
def linear_function_rotation():
    print('Linear Function Rotation')
    print('Please input the three value of the standard form of linear equation:\ny = a * x + b')
    a = float(input('Type the value of a: '))
    b = float(input('Type the value of b: '))
    print('Please input the point of rotation')
    Rotation_Point_X_Value = float(input("Type the x-value of the rotation point: "))
    Rotation_Point_Y_Value = float(input("Type the y-value of the rotation point: "))
    Rotation_Degree = float(input("Please input the degree of rotation (counter-clockwise): "))
    Tangent_Function = math.ceil (math.atan(a))
    Tangent_Outcome = Tangent_Function+Rotation_Degree
    Tangent_Result = math.floor (math.tan(Tangent_Outcome))
    Y_Intercept_Final = Rotation_Point_Y_Value - Tangent_Result * Rotation_Point_X_Value
    print ("Full Linear Equation (Show tan): y = tan(", Tangent_Outcome, ") * x + ", Rotation_Point_Y_Value, " - tan(", Tangent_Outcome,") * ",Rotation_Point_X_Value)
    print ("Full Linear Equation (Only numbers): y = ",Tangent_Result, " * x + ", Y_Intercept_Final)
    a = 0
    b = 0
    return_to_menu()
    
def quadratic_function_generator():
    print('Quadratic Function Generator')
    print("Please type the three set of coordinate points (x1,y1),(x2,y2),(x3,y3)")
    First_Point_X_Value = float(input("Type the x-value of the first point: "))
    First_Point_Y_Value = float(input("Type the y-value of the first point: "))
    Second_Point_X_Value = float(input("Type the x-value of the second point: "))
    Second_Point_Y_Value = float(input("Type the y-value of the second point: "))
    Third_Point_X_Value = float(input("Type the x-value of the third point: "))
    Third_Point_Y_Value = float(input("Type the y-value of the third point: "))
    Calculation_Temp_1 = pow(Third_Point_X_Value,2) - pow(Second_Point_X_Value,2)
    Calculation_Temp_2 = pow(Second_Point_X_Value,2) - pow(First_Point_X_Value,2)
    Calculation_Temp_3 = Third_Point_X_Value - Second_Point_X_Value
    Calculation_Temp_4 = Second_Point_X_Value - First_Point_X_Value
    Calculation_Temp_5 = Third_Point_Y_Value - Second_Point_Y_Value
    Calculation_Temp_6 = Second_Point_Y_Value - First_Point_Y_Value
    a = ((Calculation_Temp_5 * Calculation_Temp_4) - (Calculation_Temp_6 * Calculation_Temp_3))/((Calculation_Temp_1 * Calculation_Temp_4 - Calculation_Temp_2 * Calculation_Temp_3))
    b = ((Calculation_Temp_5 * Calculation_Temp_2) - (Calculation_Temp_6 * Calculation_Temp_1))/((Calculation_Temp_3 * Calculation_Temp_2 - Calculation_Temp_4 * Calculation_Temp_1))
    c = First_Point_Y_Value - (a * pow(First_Point_X_Value,2)) - (b * First_Point_X_Value)
    print ('Full Quadratic Function: ', "y = (",a,") * x^2 + (",b,") * x + (",c,")")
    Vertex_X_Value = (-1 * b)/(2*a)
    Vertex_Y_Value = (a * pow(Vertex_X_Value,2)) + (b * Vertex_X_Value) + c
    print ("Vertex location: ",Vertex_X_Value,",",Vertex_Y_Value)
    return_to_menu()
    
#Problem solver for the advanced mathematics section
def matrix_multiplier ():
    print ('Matrix Multiplier')
    row_of_first_matrix = int(input("Please enter the row of the first array: "))
    column_of_first_matrix = int(input("Please enter the column of the first array: "))
    print("\nEnter the elements in your first matrix from upper left to lower right")
    list_number_of_first_matrix = row_of_first_matrix * column_of_first_matrix
    array_mirror_of_first_matrix = [1.1145141919810]
    for i in range(2,list_number_of_first_matrix + 2):
        array_mirror_of_first_matrix_temp = float(input("Please enter the %d element in your matrix: " %(i - 1)))
        array_mirror_of_first_matrix.insert (i,array_mirror_of_first_matrix_temp)
    del array_mirror_of_first_matrix[0]
    np_array_mirror_of_first_matrix = np.asarray(array_mirror_of_first_matrix)
    first_matrix = np_array_mirror_of_first_matrix.reshape(column_of_first_matrix,row_of_first_matrix)
    print("This is your first matrix: \n",first_matrix,"\n")
    #==========★==========#
    row_of_second_matrix = int(input("Please enter the row of the second array: "))
    column_of_second_matrix = int(input("Please enter the column of the second array: "))
    print(" ")
    if row_of_first_matrix != column_of_second_matrix:
        print(row_of_first_matrix,column_of_second_matrix)
        print("The column of the first matrix needs to equal the row of the second matrix")
        return_to_menu()
    list_number_of_second_matrix = row_of_second_matrix * column_of_second_matrix
    array_mirror_of_second_matrix = [1.1145141919810]
    for i in range(2,list_number_of_second_matrix + 2):
        array_mirror_of_second_matrix_temp = float(input("Please enter the %d element in your matrix: " %(i - 1)))
        array_mirror_of_second_matrix.insert (i,array_mirror_of_second_matrix_temp)
    del array_mirror_of_second_matrix[0]
    np_array_mirror_of_second_matrix = np.asarray(array_mirror_of_second_matrix)
    second_matrix = np_array_mirror_of_second_matrix.reshape(column_of_second_matrix,row_of_second_matrix)
    print("This is your second matrix: \n",second_matrix,"\n")
    #==========★==========#
    array_mirror_of_multiplied_matrix = [1.1145141919810]
    list_number_of_multiplied_matrix = column_of_first_matrix * row_of_second_matrix
    for i in range (0,list_number_of_multiplied_matrix):
        array_mirror_of_multiplied_matrix.insert (i,0)
    del array_mirror_of_multiplied_matrix[0]
    np_array_mirror_of_multiplied_matrix = np.asarray(array_mirror_of_multiplied_matrix)
    multiplied_matrix = np_array_mirror_of_multiplied_matrix.reshape(column_of_first_matrix,row_of_second_matrix)
    for row_location_of_multiplied_matrix in range(0,column_of_first_matrix):
        for column_location_of_multiplied_matrix in range(0,row_of_second_matrix):
            temp_value_in_grid = 0
            for i in range(0,row_of_first_matrix):
                temp_value_1 = first_matrix[row_location_of_multiplied_matrix,i]
                temp_value_2 = second_matrix[i,column_location_of_multiplied_matrix]
                temp_value_in_grid = temp_value_in_grid + temp_value_1 * temp_value_2
            multiplied_matrix[row_location_of_multiplied_matrix,column_location_of_multiplied_matrix] = temp_value_in_grid
    print("This is the multiplied matrix: ")
    print(multiplied_matrix)
    return_to_menu()
    
def matrix_property():
    print("3*3 Matrix property")
    row_of_first_matrix = 3
    column_of_first_matrix = 3
    print("\nEnter the elements in your first matrix from upper left to lower right")
    list_number_of_first_matrix = row_of_first_matrix * column_of_first_matrix
    array_mirror_of_first_matrix = [1.1145141919810]
    for i in range(2,list_number_of_first_matrix + 2):
        array_mirror_of_first_matrix_temp = float(input("Please enter the %d element in your matrix: " %(i - 1)))
        array_mirror_of_first_matrix.insert (i,array_mirror_of_first_matrix_temp)
    del array_mirror_of_first_matrix[0]
    np_array_mirror_of_first_matrix = np.asarray(array_mirror_of_first_matrix)
    first_matrix = np_array_mirror_of_first_matrix.reshape(column_of_first_matrix,row_of_first_matrix)
    #-------------------------------------#
    a = first_matrix[0,0]
    b = first_matrix[0,1]
    c = first_matrix[0,2]
    d = first_matrix[1,0]
    e = first_matrix[1,1]
    f = first_matrix[1,2]
    g = first_matrix[2,0]
    h = first_matrix[2,1]
    i = first_matrix[2,2]
    array_temp = [
        e*i-f*h,
        c*h-i*b,
        b*f-c*e,
        f*g-d*i,  
        a*i-c*g,
        c*d-a*f, 
        d*h-g*e,
        b*g-a*h,
        a*e-d*b
    ]
    #np_array_mirror_of_first_matrix = np.asarray(array_mirror_of_first_matrix)
    np_array_temp = np.asarray(array_temp)
    adjugate_matrix = np_array_temp.reshape(3,3)
    determinant = a*(e*i-h*f) - b*(d*i-g*f) + c*(d*h-g*e)
    if determinant == 0:
        print("\nThis matrix does not have a inverse\n")
        return_to_menu()
    array_inverse_temp = [1.14]
    for i in range(0,9):
        number_temp = array_temp[i]/determinant
        array_inverse_temp.insert (i+1,number_temp)
    del array_inverse_temp[0]
    np_array_inverse_temp = np.asarray(array_inverse_temp)
    array_inverse = np_array_inverse_temp.reshape(3,3)
    #-------------------------------------#
    print("\nThis is your matrix: \n",first_matrix,"\n")
    print("This is its adjugate matrix: \n", adjugate_matrix, "\n")
    print("This is its inverse matrix: \n", array_inverse, "\n")
    print("This is its determinant: ", determinant, "\n")
    return_to_menu()

#Problem solver for the others section

def fibonacci_sequence_calculator():
    location_of_term = int(input("Input the location of term(n) in fibonacci sequence: "))
    fibonacci_sequence(location_of_term)
    print ("This is the nth term in fibonacci sequence: ", fibonacci_sequence(location_of_term))
    return_to_menu()
    
    #--Subfunction for calculator above:
def fibonacci_sequence(location_of_ter):
    if location_of_ter == 1 or location_of_ter == 2:
        return 1
    sum_of_previous_term = fibonacci_sequence(location_of_ter-1)
    sum_of_previous_second_term = fibonacci_sequence(location_of_ter-2)
    return sum_of_previous_term + sum_of_previous_second_term

#Sections
def geometry_section ():
    print ('''
Geometry Section: 
Press 0 to return
Press 1 for Pythagorean theorem
Press 2 for Triangle area from three sides''')
    problem_selection = int(input("Type your selection: "))
    print ("Your selection is:",problem_selection,'\n')
    if problem_selection == 0:
        main_program()
    elif problem_selection == 1:
        print ('Pythagorean theorem: ')
        print ("Which side do you want to calculate?")
        print ("Press 1 for Hypotenuse, Press 2 for the adjacent/opposite side")
        side_selection = int(input())
        pythagorean_theorem (side_selection)
    elif problem_selection == 2:
        print ('Triangle area from three sides:')
        triangle_area_from_three_sides()
        
def advanced_mathematics_section ():
    print('''
Advanced mathematics section:
Press 0 to return
Press 1 for Matrix multiplier
Press 2 for 3*3 Matrix property''')
    problem_selection = int(input("Type your selection: "))
    print ("Your selection is:",problem_selection,'\n')
    if problem_selection == 0:
        main_program()
    elif problem_selection == 1:
        matrix_multiplier()
    elif problem_selection ==2:
        matrix_property()

def algebra_section ():
    print ('''
Algebra Section:
Press 0 to return
Press 1 for linear function generator
Press 2 for arithmetic progression calculator
Press 3 for quadratic equation calculator
Press 4 for linear function rotation
Press 5 for quadratic function generator''')
    problem_selection = int(input("Type your selection: "))
    print ("Your selection is:",problem_selection,'\n')
    if problem_selection == 0:
        main_program()
    elif problem_selection == 1:
        linear_function_generator()
    elif problem_selection == 2:
        arithmetic_progression_calculator()
    elif problem_selection == 3:
        quadratic_equation_calculator()
    elif problem_selection == 4:
        linear_function_rotation()
    elif problem_selection == 5:
        quadratic_function_generator()
        
def others_section():
    print('''
Others Section:
Press 0 to return
Press 1 for fibonacci sequence calculator
          ''')
    problem_selection = int(input("Type your selection: "))
    print ("Your selection is:",problem_selection,'\n')
    if problem_selection == 0:
        main_program()
    elif problem_selection == 1:
        fibonacci_sequence_calculator()
      
#On Startup
startup_image =  r'''
 __  __       _   _     __  __       _       
|  \/  | __ _| |_| |__ |  \/  | __ _| |_ ___ 
| |\/| |/ _` | __| '_ \| |\/| |/ _` | __/ _ \
| |  | | (_| | |_| | | | |  | | (_| | ||  __/
|_|  |_|\__,_|\__|_| |_|_|  |_|\__,_|\__\___|'''
print (startup_image)
#Add a comma behind each dictionary (except the last one) and ' is not the same as ‘！！！
all_equations = [
     {'Equation name': 'Pythagorean theorem','Section': 'Geometry','Serial number': 1},
     {'Equation name': 'Linear function generator','Section': 'Algebra','Serial number': 1},
     {'Equation name': 'Triangle area from three sides','Section': 'Geometry','Serial number': 2},
     {'Equation name': 'Quadratic equation calculator','Section': 'Algebra', 'Serial number': 2},
     {'Equation name': 'Arithmetic progression calculator','Section': 'Algebra', 'Serial number': 3},
     {'Equation name': 'Linear function rotation', 'Section': 'Algebra', 'Serial number': 4},
     {'Equation name': 'Quadratic function generator', 'Section': 'Algebra', 'Serial number': 5},
     {'Equation name': 'Matrix multiplier', 'Section': 'Advanced mathematics', 'Serial number': 1},
     {'Equation name': '3*3 Matrix Property', 'Section': 'Advanced mathematics', 'Serial number': 2},
     {'Equation name': 'Fibonacci sequence calculator', 'Section': 'Others', 'Serial number': 1}
]
menu_number = {'Geometry section':1, 'Algebra section':2, 'Advanced mathematics section':3, 'Others section':4}
#Submenu Number : 
current_menu = 0
current_submenu = 0
main_program()
