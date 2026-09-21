#File: homework1.py

#---Variables and Data Types---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals\

b = 1.5
print(b)
print(type(b)) # b is a float, a fractional number or a number with decimals

c = 3j
print(c)
print(type(c)) # c is complex, consisting of real and imaginary components

d = "hello"
print(d)
print(type(d)) # d is a string, which are words or text

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, used to store multiple items in a single variable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, used to store data as a collection of key-value pairs

g = (1,2)
print(g)
print(type(g)) # g is a tuple, used to store a collection of data; unlike lists, they cannot be modified once created

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list

i = True
print(i)
print(type(i)) # i is a boolean, representing True or False

j = None
print(j)
print(type(j)) # j is a nonetype, used to represent the absence of a value; similar to null

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list

l = str(14)
print(l)
print(type(l)) # l is a string

m = 1e4
print(m)
print(type(m)) # m is a float

'''
1. I found nine different data types.
2. integer, float, complex, string, list, dictionary, tuple, boolean, nonetype
3. b & m, d & l, e, h, & k
4. l is a string, because the str function indicates that the 14, despite being an integer, is read as text characters
5. the data type I chose is a set.
'''
n = {1, 2, 3}
print(n)
print(type(n)) # n is a set, an unordered collection of key-value pairs to look up values quickly; must be unique and in curly brackets

#---Booleans---
print(10>9) # True, 10 is greater than 9
print(10==9) # False, 10 is not equal to 9
print(10<=9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, abc is a non-empty string
print(bool(123)) # True, numbers inside a boolean are True as long as they do not equal zero
print(bool(["apple", "cherry", "banana"])) # True, elements inside a list of a boolean are True
print(bool(True)) # True, the result of the boolean is already True
print(bool(False)) # False, the result of the boolean is already False
print(bool(0)) # False, a zero inside the boolean results as False
print(bool("")) # False, an empty string inside a boolean results in a False
print(bool(" ")) # True, a non-empty string inside a boolean results in a True; the space counts as a character in the string
print(bool(())) # False, empty tuples inside a boolean are False
print(bool([])) # False, empty lists inside a boolean are False
print(bool({})) # False, empty dicts inside a boolean are False
print(bool((True and False))) # False, "and" will result in a False if either side of the entry is False
print(bool(True and True)) # True, "and" is True only when both sides are True
print(bool(False and False)) # False, "and" will result in a False if either side of the entry is False
print(bool(True or False)) # True, "or" will result in a True if either side of the entry is True
print(bool(True or True)) # True, there is a True to the side of the "or"
print(bool(False or False)) # False, there are no True's to the sides of the "or"
print(bool(not(False))) # True, "not" will flip the value, so the result is True
print(bool(not(True))) # False, "not" flips the output
'''
1. I noticed that the expressions returning False have empty expressions or include "and" and False; for True returns, I noticed "or" and True, and if there are elements in a grouping
2. I was surpised that the "or" and "and" commands have special sets of rules regarding having True or False written in them
3. print(bool("omika is awesome)) will return as True because the string is non-empty
4. print(bool(0>1)) will return as False because 0 is not greater than 1
'''

#---Operators---
# arithmetic operators
print(10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction
print(2*4) # 8, * performs multiplication
print(6/3) # 2, / performs division
print(5%2) # 1, % performs the remainder of a division
print(3**2) # 9, ** performs an exponent
print(15//2) # 7, // performs floor division, rounding down to the nearest whole number

# comparison operators
print(5==2) # False, 5 is not equal to 2
print(10!=10) # False, 10 is equal to 10
print(2<5) # True, 2 is less than 5
print(12>5) # True, 12 is greater than 5
print(5<=6) # True, 5 is less than or equal to 6
print(1>=10) # False, 1 is not greater than or equal to 10

# assignments operators
x = 5
x+=5
print(x) # 10, += updates x by adding 5
x-=4
print(x) # 6, -= updates x by subtracting 4 (to the updated x = 10 from the operation above)
x*=3
print(x) # 18, *= updates x by multiplying it by 3

# logical operators
#1. "and" results in True iff both conditions are true
print(bool(3 and 6))
print(bool("" and 3))
#2. "or" returns False iff both conditions are False
print(bool([] or 12))
print(bool([] or ""))
# 3. "not" will negate the truth value of the input
print(bool(not("")))
print(bool(not(87)))

# more questions
'''
1. / performs exact division, while // will round the quotient down to the nearest whole number
2. % will give the remainder of a division, while // will provide a quotient rounded down to the nearest whole number
3. I found use % to calculate the remainder when dividing two numbers. An example would be print(10%3), resulting in 1
4. assignment operators will evaluate the right hand side expression first, then update the variable that was assigned to it on the left.
'''

#---Strings---
my_string="hello"
print(my_string) # prints: hello
print(my_string[0]) # prints: h
print(my_string[1]) # prints: e
print(my_string[2]) # prints: l
print(my_string[3]) # prints: l
print(my_string[4]) # prints: o
print(my_string[-1]) # prints: o
print(my_string[1:3]) # prints: el
print(my_string[0:5:2]) # prints: hlo
print(len(my_string)) # prints: 5
print(my_string+"goodbye") # prints: hellogoodbye
print(7 * my_string) # prints: hellohellohellohellohellohellohello

# questions
# 1. slicing is when you take a piece of a string using [start:stop:step]. manipulations 2-9 used slicing
name="Oski"
print("Hello, my name is", name) # prints: Hello, my name is Oski
print(f"Hello, my name is {name}") # prints: Hello, my name is Oski
# 4. the results were the same, even though the inputs were different. f-strings allow variables to be embedded directly inside a string with {} around the expression; cleaner version to build such strings

#---Terminal Commands---
'''
1. cd; changes directories; used to move from one folder to another
ex. cd Desktop
2. ls; list; lists the files/folders in the current directory
ex. ls
3. ls -a' lists all files/folder in the current directory, including hidden ones
ex. ls -a
4. mkdir; creates a new directory
ex. mkdir new_folder
5. cat; displays the contents of a file directly in the terminal
ex. cat notes.txt
6. pwd; prints the working directory, showing the full path of where you currently are
ex. pwd
7. cd ..; moves up one directory level, to the parent folder
ex. cd ..
8. cd .; refers to the current directory, mostly used in scripts
ex. cd .
9. cd ~; moves to the home directory, no matter were you currently are
ex. cd ~
10. cp; copies a file/folder from one location to another
ex. cp file.txt backup.txt
11. mv; moves or renames a file/folder
ex. mv file.txt Documents/
12. rm; deletes a file/folder; permanent
ex. rm old_file.txt
13. clear; clears the terminal screen
ex. clear
14. grep; searches for a pattern of text within an output
ex. grep "error" file.txt
'''
# questions
'''
1. head; shows the first few lines of a file; ex. head file.txt
touch; shows the last few lines of a file; ex. touch file.txt
diff; compares two files and shoes the differences; ex. diff file_1.txt file_2.txt
2. ls lists all files/folders in the current directory, while ls -a does that AND hidden files
3. a hidden file is one that starts its name with a .
4. ls -t; sorts the files/folders in the current directory by modification time; ex, ls -t
rm -f; forces deletion without asking for confirmation; ex. rm -f file.txt
rm -r; deletes a folder and everything inside of it; ex. rm -r python_decal
'''