# SFS Lab 3 - Python Regex Questions
# EC May, 2022
# Add your answer to each of the questions
import re


# Q1 Import the apache log and print out the contents
# your code here
apache_log = "apache_log"
# with open(apache_log) as f:
#     for line in f:
#         print(line)
# # text = "192"
# # with open(apache_log) as f:
# #     for line in f:
# #         if text in line:
# #             print(line)
# once you have answer for Q1 comment out the print statement to keep things tidy

# Q2 Use regex to find any instance of the word notice?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('notice', file)
    print(x)

# Q3 Use regex to find any instance of the word error?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('error', file)
    print(x)

# Q4 Use regex to count any instance of the word notice?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('notice', file)
    print(len(x))
    #or
#     countnotice = file.count('notice')
#     print(countnotice)
    

# Q5 Use regex to count any instance of the word error?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('error', file)
    print(len(x))
    #or
#     countnotice = file.count('error')
#     print(countnotice)

# Q6 Use regex to count any instance of the letter p?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('p', file)
    print(len(x))
    #or
#     countnotice = file.count('p')
#     print(countnotice)

# Q7 Use regex to find any instance of the string jk2_init?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('jk2_init', file)
    print(len(x))
    #or
#     countnotice = file.count('jk2_init')
#     print(countnotice)

# Q8 Use regex to find any appearance of the number 6754?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('6754', file)
    print(len(x))
    #or

#     countnotice = file.count('6754')
#     print(countnotice)

# Q9 Use regex to find any appearance of the number 6?
# your code here
with open (apache_log) as f:
    file = f.read()
    x = re.findall('6', file)
    print(len(x))
    #or
#     countnotice = file.count('6')
#     print(countnotice)

# Q10 Use regex to find any ip addresses?
# your code here
# with open (apache_log) as f:
#     file = f.read()
#     ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
#     print("Ip addresses in list =", len(ip_pattern))
#     iplist = re.findall(ip_pattern, file)
#     print(*iplist, sep="\n")
    
# Q11 Create a script that will ask for user input, ask the user to enter a letter, then use regex to return any matches of that letter in the file?
# your code here
# userinput = input("enter a letter to count how many times it appears in apache file: ")
# print(len(re.findall(userinput, file)))

# Q12 adapt your answer from Q11, to use a function to search the file, the function should take one parameter - the letter you are searching for?
# your code here
def letter_lookup():
    userinput = input("enter a letter to count how many times it appears in apache file: ")
    print(len(re.findall(userinput, file)))

letter_lookup()
# your code here

