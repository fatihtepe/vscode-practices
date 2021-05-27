import os

os.system('clear')

with open('test.csv', 'r', encoding='utf-8') as file:
  print(file.read())
  

import csv
with open('test.csv', 'r', newline = '', encoding='utf-8') as file:
    csv_rows = csv.reader(file)
    
    for row in csv_rows:
        print(row)
        
print('-----------')

import csv
with open('test.csv', 'r', newline = '', encoding='utf-8') as file:
    csv_rows = csv.reader(file, delimiter=',')
    
    for row in csv_rows:
        print(row)
        
print('-----------')

import csv
with open('test.csv', 'r', newline = '', encoding='utf-8') as file:
    csv_rows = csv.reader(file, delimiter='-')
    
    for row in csv_rows:
        print(row)
        
import pandas as pd

titanic = pd.read_csv('titanic.csv')

print(titanic)

try:
    f = open('fishes.txt')
    print(f.read())
except:
    print('something went wrong')
finally:
    f.close()


with open('rumi.txt') as our_new_file:
    print(our_new_file.readline())



try:
    print('beginning of the try block, in "try" section...') 
    ourfile = open('fishes.txt')
    print()
    print(ourfile.read())
    print(99/0)
    print('this is the last line of try block...')
except:
    print('something went wrong')
finally:
    print('this block will always executed...')
    ourfile.close()
    print('this the end...')
     

with open('mike.txt', 'w', encoding='utf-8') as f:
    f.write('''Target Audience
Are you a developer looking to shift your career towards a more DevOps model?
Are you are a classically trained Ops person and you would like to get a feeling of what this whole DevOps thing is all about?
Or are you neither, and having spent some time working with technology you are now simply looking for a career change and have no idea where to start?
If so, read on, for we are going to see how to become a mid-level DevOps engineer in six months!
Finally, if you have been doing this DevOps thing for years now, you might still find this useful as a validation of where we are and where this is going.''')
    
with open('mike.txt', 'r', encoding='utf-8') as f:
    print(f.read())


listem = ['elma', 'armut']    

with open('i', 'w', encoding='utf-8') as f:
    f.write('arget Audience we are and where this is going.')
    
for i in listem:
   with open(i, 'w', encoding='utf-8') as f:
    f.write('arget Audience we are and where this is going.')
    
with open('i', 'r', encoding='utf-8') as f:
    print(f.read())
    

listem = ['you', 'me']    

  
for i in listem:
   with open(i, 'w')as f:
    f.write('testing')
    
with open('i', 'r')as f:
    print(f.read())


file_name = ''
for i in range(10):
    file_name = (str(i)+'.txt')
    with open(file_name, 'w') as f:
        f.write('testing')
        
with open(file_name, 'r') as f:
    print(f.read())




test = "test3.txt"
anothervar = "anotherfile"
for i in range(10)
with open(anothervar, "w") as ourFirstNewFile:
    ourFirstNewFile.write("qqqqqqqqqqqq wwwwww eeeeeeeee")
with open("newFile.txt", "r") as ourFile:
    print(ourFile.read())
print("this is the end of our program...")
myFileList = ["first", "second", "third.txt", "fourth.test", "fifth.py"]
for i in myFileList:
    with open(i, "w") as newFile:
        newFile.write(i)
file_name = ""
for i in range(1, 11):
    file_name = (str(i) + ".txt")
    with open(file_name, "w") as f:
        f.write(file_name)
    with open(file_name, "r") as f2:
        print(f2.read())



flowers = ['jasmine\n', 'rose\n', 'lily\n', 'daisy\n', 'tulip\n']


with open('flowers.txt', 'w') as f:
    f.writelines(flowers)
        
with open('flowers.txt', 'r') as f:
    print(f.readlines())

with open('flowers.txt', 'r') as f:
    print(f.read())
    
    
flowers = ['jasmine\n', 'rose\n', 'lily\n', 'daisy\n', 'tulip\n']
with open('flowers.txt', 'a') as f:
    f.write('orchid\n')

with open('flowers.txt', 'r') as f:
    print(f.read())



user_input = input('enter flower name: ') + '\n'
with open('flowers.txt', 'a') as f:
    f.write(user_input)

with open('flowers.txt', 'r') as f:
    print(f.read())
    

with open('fruit.csv', 'r') as f:
    print(f.read())


import csv
with open('fruit.csv', 'r') as file:
    csv_rows = csv.reader(file)
    
    for row in csv_rows:
        print(row)
    
import pandas as pd

flw = pd.read_csv('fruit.csv')

print(flw)