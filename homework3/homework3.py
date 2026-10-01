#---Print Functions---
name = "Omika"
def say_goodbye(name):
    print("Goodbye," , name)

say_goodbye(name) # prints "Goodbye, Omika"

def area_circle(radius):
    print(3.14 * radius**2)

area_circle(1) # prints 3.14, as 3.14(1^2) is 3.14
area_circle(2) # prints 12.56, as 3.14(2^2) is 12.56

#---Return Functions---
def subtract(a,b):
    return(a - b)
print(subtract(2,1)) # prints 1; 2-1 = 1

def multiply(a,b):
    return(a*b)
print(multiply(2,1)) # prints 2; 2*1 = 2

def divide(a,b):
    return(a/b)
print(divide(2,1)) # prints 2; 2/1 = 2

#---Conditionals---
temp = [15, 13, 17, 20, 23, 28, 20]
def range_temperature(temp):
    return (min(temp), max(temp))
print(range_temperature(temp)) # prints (13, 28)

Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7
def is_weekend(num):
    if num == 6 or num == 7:
        return ("True, no classes yay!!")
    else:
        return ("False, wake up for your 8am")
print(is_weekend(3)) # prints False; its wedneday
print(is_weekend(7)) # prints True; its sunday

def fuel_efficiency(distance, fuel): # in miles and gallons
    return(distance/fuel)
print(fuel_efficiency(74.3,3)) # lick is about 74.3 miles from berkeley
# prints 24.77 mpg


def secret_code(num):
    last_digit = num%10 # gives remainder, which is last digit when dividing by a factor of 10
    everything_else = num//10 # will give everything but the decimal bc floor division rounds down to the nearest integer
    encrypted = int(str(last_digit) + str(everything_else)) # converting the integers to strings should push the results together instead of adding them mathematically
    return encrypted
print(secret_code(123)) # prints 312
print(secret_code(42808)) # prints 84280

#---Loops---
def computation(x,y):
    result = 1 # eliminates y=0
    for i in range(y):
        result = result * x # multiplies the power y x amount of times (how powers work)
    return result
print(computation(2,3)) # prints 8; 2^3 is 8

numbers = [2, 5, 3, 1, 10]
def minmax(numbers):
    min_num = numbers[0] # first number in the list (2)
    max_num = numbers[0] 
    for num in numbers: # will check every number in the list for the following conditions
        if min_num > num:
            min_num = num # min cant be greater
        if max_num < num:
            max_num = num # max cant be lesser
    return min_num, max_num
print(minmax(numbers)) # prints (1, 10)

numbers = [2, 5, 3, 1, 10]

def list_min(numbers):
    min_num = numbers[0]
    i = 1 # checks the other numbers
    while i < len(numbers):
        if numbers[i] < min_num: #checks for the smallest number in the list
            min_num = numbers[i] 
        i = i + 1
    return min_num
def list_max(numbers):
    max_num = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_num:
            max_num = numbers[i]
        i = i + 1
    return max_num
print(list_min(numbers)) # prints 1
print(list_max(numbers)) # prints 10

def calc_sum(num):
    sum = 0 # begins the running total of digits
    while num > 0: # continues loop
        last_digit = num % 10 # provides remainder when dividing by a factor of 10, which is the last digit
        sum = sum + last_digit
        num = num//10 # removes last digit, like the secret code problem
    return sum

print(calc_sum(23)) # returns 5
print(calc_sum(23040)) # returns 9

#---Running Your Script---
# favorite fxn: min of a list of numbers (6.2.2)
numbers = [2, 5, 6, 1, 8]
result = min(numbers) 
print(result) # prints 1 

print(f"The result of While Loops to find the minimum value of an integer list (6.2.2) with the list denoted is 1")

