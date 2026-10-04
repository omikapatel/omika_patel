#---Lists---
fav_foods = ["samosa", "thai curry", "paneer", "ramen", "popcorn"]
print(fav_foods[1])
print(fav_foods[-1])

fav_foods.append("tofu")
print(fav_foods) # prints w/ tofu at the end

fav_foods.insert(0, "apple")
print(fav_foods) # prints w/ apple to the beginning
'''
I encountered this error:
SyntaxError: invalid syntax (detected in line 9)
I originally wrote: fav_foods.insert([0],"apple")
i did not need the square brackets around the 0, so i fixed it by removing them
'''
fav_foods.remove("paneer")
print(fav_foods) # prints w/o paneer
print(len(fav_foods)) # prints 6

for food in fav_foods:
    print(food.upper())
'''
I encountered this error:
AttributeError: 'list' object has no attribute 'upper'(line 22)
I originally wrote print(fav_foods.upper())
I had to write print(food.upper()) due to the way i defined the items in the list
'''
new_list = [fav_foods[0], fav_foods[5]]
print(new_list) # prints ["apple", "tofu"]

def has_potato(fav_foods):
    if "potato" in fav_foods:
        return("A potato!")
    else:
        return("No potato!")
print(has_potato(fav_foods)) # returns No potato!

#---Slicing and Striding---
numbers = list(range(0,21))
print(numbers)

def get_first_15(numbers):
    return(numbers[0:15])
print(get_first_15(numbers))

def get_every_5th(lst):
    return(lst[::5])
print(get_every_5th(get_first_15(numbers)))
'''
I encountered this error:
NameError: name 'lst' is not defined (line 49)
I orginally wrote print(get_every_5th(lst))
I could not use lst in the print function, since it was not actually defined. I had to use my defined numbers list and then edit the print function.
'''

def reverse_and_stride(lst2):
    return(lst2[::-1], lst2[1::3])
print(reverse_and_stride(get_every_5th(get_first_15(numbers))))

#---Nested Lists---
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(numbers[2]) # prints the last row
print(numbers[1][1]) # prints 5

numbers.append([10,11,12])
print(numbers)

def sum_nested(numbers):
    sum = 0
    for row in numbers:
        for num in row:
            sum += num
    return (numbers, sum)
print(sum_nested(numbers)) # 78

#---Create a 5x5 List---
def create_5x5():
    list = []
    input = 1
    for row in range(5):
        new_row = []
        for column in range(5):
            new_row.append(input)
            input += 1
        list.append(new_row)
    return(list)
print(create_5x5()) # creates a 5x5 from 1-25

list_5x5 = create_5x5() # storing in a new name

def multiple_3(lst):
    for row in lst:
        for i in range(len(row)): # for every element in the range of the length of the row
            if row[i]%3 == 0:
                row[i] = "?"
    return(lst)
question_marks = (multiple_3(list_5x5))
print(question_marks)

def sum_nonquestion(lst1):
    sum = 0
    for row in lst1:
        for num in row:
            if num != "?":
                sum += num
    return(sum)
print(sum_nonquestion(question_marks)) # 217

#---Dictionaries---
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"]) # 30
ages.update({"Mira": 100})
print(ages) # Mira is now 100

ages.update({"Milana": 52})
print(ages) # Milana added!

del ages["Mariam"]
print(ages)

def the_goats(ages):
    for (name, age) in ages.items():
        print(name, age) # return stops the loop
the_goats(ages)

# fav function: the potato one
print(has_potato(fav_foods)) # no potato!