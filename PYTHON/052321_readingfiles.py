import os 
clear = lambda: os.system("clear")
clear()

'''Orca is a kind of Dolphin.
Blue Whale is the largest animal known on earth.
Sharks are the sister group to the Rays (batoids).
The Tuna Fish can weigh up to 260 kg.
Squid and Octopus are in the same class.'''


sea = open('fishes.txt', 'r')
print(sea.read())
sea.close()


sea = open('fishes.txt', 'r')
print(sea.read(33))
print(sea.read(33))
sea.seek(0)
print(sea.read(33))
sea.close()


sea = open('fishes.txt', 'r')
print(sea.readline())
print(sea.readline())
print(sea.readline())
print(sea.readline())
sea.close()



sea = open("fishes.txt", 'r')   

print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))

sea.close()




sea = open("fishes.txt", 'r')   
print(sea.readlines())
sea.close()



sea = open("fishes.txt", 'r')   
print(type(sea.readlines()))  # <class 'list'>
sea.close()



sea = open('fishes.txt', 'r')
for line in sea:
    print(line)

sea.close()



1
my_file = open('fishes.txt') 
print(type(my_file))

2
my_file = open('fishes.txt') 
print(my_file.read())
my_file.close()


3
my_file = open('fishes.txt') 
print(my_file.read(40))
my_file.close()


4
my_file = open("fishes.txt", 'r')   
print(my_file.readline()) 
my_file.close()


5
my_file = open("fishes.txt", 'r')   
print(my_file.readline(9)) 
my_file.close()


6
my_file = open("fishes.txt", 'r')   
print(my_file.readlines()) 
my_file.close()



7
my_file = open("fishes.txt", 'r')   

for line in my_file:
    print(line)

my_file.close()



with open("dummy_file.txt", 'w', encoding="utf-8") as file:  
# we create and open the file

    file.write('This is the first line of my text file')  
    # writes str data into file

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the 'dummy_file'
    




with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('This is the new line for my dummy_file')  
    # we write new str data into it 

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the 'dummy_file'
    
    
    
    
with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('My first sentence')
    file.write('My second sentence,')
    file.write('My third sentence\n')
    file.write('My fourth sentence ')
    file.write('My last sentence')

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())




fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    for basket in fruits:
        file.write(basket + '\n')  # adds a newline character to each string
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())  # reads and displays entire lines in a list




fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    file.writelines(fruits)  # takes an iterator for writing
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())



fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    file.writelines(fruits)  # creates a file containing the elements of the list

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the file

with open("fruits.txt", 'a', encoding="utf-8") as file:
    file.write('Melon\n')  # adds "Melon" to the end of the existing file
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the last content of the file

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())



with open("new_file.txt", "w", encoding="utf-8") as file:  
# create and open the file

    file.write('Hello Richard. This is my file.')  
    # write str data into the file



colors = ['red\n', 'green\n', 'yellow\n', 'white\n', 'black\n']

with open("new_file.txt", 'w', encoding="utf-8") as file:
    file.writelines(colors)   




colors = ['red', 'green', 'yellow', 'white', 'black']

with open("new_file.txt", 'w', encoding="utf-8") as file:
    for i in colors:
        file.write(i + '\n')  # we create "new_file.txt" for you 
        
with open('new_file.txt', 'a', encoding='utf-8') as file:
    file.write('blue\n')  # add "blue" to the end of the text




with open("fruits.csv", 'r', encoding="utf-8") as file:
    print(file.read())
 
 
    
import csv  # loads csv module

with open("fishes.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file)  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows: 
        print(row)    



import csv

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter= ",")  # gives the same output as the previous one
                                 
    for row in csv_rows: 
        print(row)   



import csv 

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter = ':')  # we specified a char ":" that is not used
                                                  # in the csv file as a value of delimiter
    for row in csv_rows: 
        print(row)        




with open("annual_assesment.csv",'r', encoding='utf-8') as file:
    print(file.read())

