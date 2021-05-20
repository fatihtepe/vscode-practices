import math

num = '5'
print(math.pow(num, 0))


while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except:
        print("Something went wrong...Try again.")
        break


while True:
    a = int(input('ilk sayı:'))
    b = int(input('ikinci sayı:'))
    try:
        c = a / b 
        print(c)
        break
    except:
        print('bir şeyler ters gitti')
    

while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")

try :
    print("4" + 4)
except TypeError :
    print("Type hatası var. Tipi kontrol etsen iyi olur.")
else :
    print("Aaaa demek ki exception yükselmemiş. MMmm. Super.")
finally:
    print("Eh nihayet bana sıra geldi. Ben çalıştım.")


try:
    isim = input('isminiz: ')
    print(a)
except Exception as hatam:
    print(hatam)
    print(type(hatam))
    

from upper_package import my_package1, my_package2 
from upper_package.my_package1 import my_module_1, my_module_2
# print(dir(my_package1))

from upper_package.my_package2 import my_module_3, my_module_4
# print(dir(my_package2))


print(my_module_2.divide(10, 5))
print(my_module_3.repeater('clarusway ', 3))

