
tuttugum_sayi = 36
bilbakalim = int(input('Aklimdan bir sayi tuttum bil bakalim kac?: '))

if bilbakalim == tuttugum_sayi:
    print('Tebrikler')
else:
    print('bilemedin!')

a = 1
while a < 10:
    a += 1
    print('bilgisayar cildirdi!')


while True:
    letter = input('please enter a letter: ')    
    if letter == 'q':
        print('exiting....')
        break
    else:
        print('invalid input')


a = 0
while a < 10:
    a += 1
    if a >= 5:
        print('a is bigger than 5')
    else:
       print('a is less than 10') 



evenlist = []
oddlist = []
a = 0
while a < 20:
    a += 1
    if a % 2 == 0:
        evenlist.append(a)
    else:
        oddlist.append(a)
print(evenlist)
print(oddlist)


name = 'fatihtepe'
print(*name)

for letter in name:
    print(letter)

a = 0
while a < len(name):
    print(a, end=" ")
    a += 2



sayilar = "123456789"
sayilarlist = []
for sayi in sayilar:
    a = int(sayi) * 2
    sayilarlist.append(a)
print(sayilarlist)


sayilar = "123456789"
liste = []

for i in sayilar:
    if int(i) < 5:
        liste.append(i)
print(liste)
        

while True:
    password = input('enter your password: ')
    if not password:
        print('you have enter a password: ')
    elif len(password) > 8 or len(password) < 3:
        print('password can not be longer than 8 or less 3 character')
    else:
        print('your password is', password)
        break


while True:
    sayı = int(input("Bir sayı girin: "))
    if sayı == 0:
        break
    elif sayı < 0:
        pass
    else:
        print(sayı)
        break