evens = []
odds = []

for i in range(1,10):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(evens)
print(odds)

list = [i for i in range(1,10) if not i % 2]
print(list)



ex_list = [11, 2, 3, 4, 5, 45, 67]
count_even = 0
count_odd = 0
for i in ex_list:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print('The number of even numbers:', count_even)
print('The number of odd numbers:', count_odd)



for i in range (1, 10):
    print(i*str(i))



toplam = 0
for i in range(1, 75):
    toplam += i
print(toplam)


print(sum(i for i in range(1, 75)))


names = ["susan", "tom", "edward"] 
mood = ["happy", "sad"]
for n in names:
    for m in mood:
        print(n,'is', m)

line = 10
print()
for i in range(line):
    print(' '*16+' '*19+'*'*12+' '*7+'*'*12+' '*7+'*'*(line-1-i)+'*'*(3*i+1))
for i in range(line*2-7):
    print(' '*(line+5-i)+'*'*(i+1)+'*'*12+' '*7+'*'*12+' '*7+'*'*12+' '*7+'*'*12)
for i in range(5):
    print(' '*16+'*'*19+'*'*19+'*'*12+' '*7+'*'*12)



names = ["susan", "tom", "edward"] 
mood = ["happy", "sad"]

for n in names:
    for m in mood:
        print(n, 'is', m)


my_list = [1, 2, 3, 4, 5, 6]
new_list = []
for i in my_list:
    if i % 2:
        new_list.append(i ** 2)
print(new_list)

print([i ** 2 for i in my_list if i % 2])

print(i for i in my_list)
print(*my_list)

