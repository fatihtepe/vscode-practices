import os 
clear = lambda: os.system("clear")
clear()


fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]

count = 3

while count > 0:
    try :
        index = int(input("Favori meyve indexini girer misin? : "))
        print("Benim favori meyvem {}'dir.".format(fruits[index]))
        break
    
    except IndexError :
        count -= 1
        print(f"Böyle bir index bulunmamaktadır. {count} adet giris hakiniz kaldi Lütfen doğru giriş yapınız.")
    
    except ValueError :
        count -= 1
        print(f"Integer yani numeric bir değer giriniz. {count} adet giris hakkiniz kaldi.Tekrar deneyin.")
    
    else :
        print('Tebrikler.. dogru giris yaptiniz')
        break
    
    finally :
        print('Meyvelerim tazedir afiyet olsun.')



fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']

with open('fruits.txt', 'w', encoding='utf-8') as file:
    for meyve in fruits:
      file.write(meyve + '\n')
      
with open('fruits.txt', 'r') as file:
    print(file.read())

with open('fruits.txt', 'r') as file:
    print(file.readlines())


    
with open('rumi.txt', 'r') as mevlana:
    print(mevlana.read())



file = open('/Users/tepe/Desktop/fishes.txt', 'r')
print(file.read())
file.close()



number = int(input("Please enter a number: "))
print()
print("type of the input: ", type(number))
print("Here is the number you've entered: ", number)
print("And the program has finished working. BYE...")



try:
    print("now, i am in try block...")
    number = int(input("Please enter a number: "))
    print("type of the input: ", type(number))
    print("Here is the number you've entered: ", number)
except:
    print("now, i am in except block...")
    print("i cannot continue. because there is stg. wrong!!!")
print()
# print("type of the input: ", type(number))
# print("Here is the number you've entered: ", number)
print("And the program has finished working. BYE...")


try:
    number1 = int(input("please enter the first number: "))
    number2 = int(input("please enter the second number: "))
    print("number 1: ", number1)
    print("number 2: ", number2)
    print("the division of the numbers: ", number1 / number2)
except:
    print("stg happened. program crushed!!!")
print("end of our program...")




number_of_iteration = 1
while True:
    print("iteration number: ", number_of_iteration)
    try:     
        number1 = int(input("please enter the number 1: "))
        number2 = int(input("please enter the number 2: "))
        print("division: ", number1 / number2)
        break
    except:
        print("hey guy! stg. bad happened. please be careful with the inputs!")
        break
    number_of_iteration += 1
print("end of our program...")