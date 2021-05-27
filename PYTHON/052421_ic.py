# import os 
# # clear = lambda: os.system("clear")
# # clear()
# os.system('clear')



# flowers = ['Jasmine\n', 'Rose\n', 'Lily\n', 'Daisy\n', 'Tulip\n']

# with open('flowers_24.txt', 'w', encoding='utf-8') as ff:
#     ff.writelines(flowers)
    
# with open('flowers.txt', 'r', encoding='utf-8') as ff:
#     print(ff.read())


# with open('/Users/tepe/Downloads/istiklal.txt', 'r', encoding='utf-8') as istiklal:
#     print(istiklal.read())

# with open('/Users/tepe/Downloads/istiklal.txt', 'r', encoding='utf-8') as istiklal:
#     for i, l in enumerate(istiklal.readlines()):
#         print(l, end = "")
#         if i % 4 == 3:
#             print()

# import glob
# for file in glob.glob('*.txt'):
#     print(file)
    


# import shutil
# shutil.copy('fruits.txt', '../fruits_x.txt')
        

# import os


# def my_factorial(n):
#     if n == 0: return 1
    
#     else:
#         return n * my_factorial(n-1)
    
# print(my_factorial(3))

# # fonksiyon icinde fonksiyon kullanmak bakilmali



# my_file = open('fishes.txt')

# print(my_file.read(33))

# print(my_file.read(25))

# my_file.seek(0)

# print(my_file.read(33))

# print(my_file.tell())

# my_file.close()






# poem = open('rumi.txt')

# print(poem.read(35))

# print(poem.read(13))

# print(poem.tell())

# poem.seek(15)

# print(poem.read(20))




# poem = open('rumi.txt')

# print(poem.readline())
# print(poem.readline())
# print(poem.readline(18))

# poem.close()


# poem = open('rumi.txt')
# print(poem.readline())
# print(type(poem.readlines()))
# poem.close()




# sea = open('fishes.txt', 'r')

# for line in sea:
#     print(line)
    
# sea.close()


# with open('fishes.txt', 'r', encoding='utf-8') as sea:
#     print(sea.readline())

python3 -m webbrowser -t "https://www.google.com"
