a = int(input("lol"))

def fibonacci_sequence(a):
    if a == 1 or a == 2:
        return 1
    sum_of_previous_term = fibonacci_sequence(a-1)
    sum_of_previous_second_term = fibonacci_sequence(a-2)
    return sum_of_previous_term + sum_of_previous_second_term


fibonacci_sequence(a)
print (fibonacci_sequence(a))