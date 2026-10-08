#---Vocabulary Review---
'''
1. Git is the version control software that tracks files; GitHub is a website that hosts Git repositories
2. The command line is where you type commands, while the terminal is the application which hosts command lines
3. A local repository is the copy of a Git project stored on your computr, while a remote repository is a copy of it hosted elsewhere, like Github, that others can access
4. A system that tracks changes to files over time; git is the most common
5. The staging area is like a "waiting room" where you put things to change for the next committ
6. Git add puts things in the staging area
7. Git commit saves the changes in your local repository with a message
8. Uploads the local commits to the remote repository
9. Shows the status of the working directory; tracks, etc
10. Pulls and merges changes from the remote repository into the local one
11. Shows the full path of working directory
12. Lists the files/folders in the directory
13. Changes from directory to directory
14. Opens a text editor inside the terminal
15. Creates an empty file
16. Moves/renames a file/folder
17. Deletes a file (permanent)
18. displays the contents of a file in the terminal
'''

#---A Directory Tree---
'''
1. pwd
2. ls
3. cd ../brianna_repo + git pull
4. mv homework.py ../judy_decal/homework/
5. cd ../judy_decal/homework
6. cat homework.py
7. git add .
git commit -m "fixed typo"
git push
8. The error means that the remote repository has commits that arent in Judy's local.
git pull, then git push
9. /Users/judy/Recent
'''

# Homework 3 Review
#---Data Types---
def check_datatype(input):
    if type(input) == str:
        print("String")
    elif type(input) == bool:
        print("Boolean")
    elif type(input) == float:
        print("Float")
    else:
        print("Integer")     
check_datatype(3.14)
check_datatype(2)
check_datatype(False)
check_datatype("Hello")

def even_odd(num):
    if num%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")    
even_odd(2)
even_odd(123)

#---Loops---
numbers = [1,2,3,4,5]
def sum_loop(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)
sum_loop(numbers) 

# Homework 4 Review
#---Lists---
list = [1,2,3]
def duplicate_list(list):
    new_list = []
    for item in list:
        new_list.append(item)
        new_list.append(item) # runs twice to duplicate
    return(new_list)
print(duplicate_list(list))

#---Debugging---
def square(num):
    return num*num
print(square(2))
print(square(4))
#the issue was that there was not a colon after def square(num)

# favorite function: duplicate list
print(duplicate_list(["hello", 2, "wowowowow"])) # works!