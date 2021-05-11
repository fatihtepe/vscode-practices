# Task: To find number of item within a list

        
numbers = [1,1,2,8,4,5,3,8,2,1,6,3,8,1,6,8]
eights = []
for x in numbers:
    if x == 8:
        eights.append(x)
print(f'The number of eights: {len(eights)}')


numbers = [1,1,2,8,4,5,3,8,2,1,6,3,8,1,6,8]
eights = [x for x in numbers if x == 8]
count_eights = len(eights)
print(f'The number of eights: {count_eights}')


numbers = [1,1,2,8,4,5,3,8,2,1,6,3,8,1,6,8]
eights = list(filter(lambda x: x == 8, numbers))
count_eights = len(eights)
print(f'The number of eights: {count_eights}')


numbers = [1,1,2,8,4,5,3,8,2,1,6,3,8,1,6,8]

count_eights = numbers.count(8)

print(f'The number of eights: {count_eights}')


L= []
for i in range(1, 1000):
    if i % 7 == 0:
        L.append(i)
print(L)

L = [i for i in range(1, 1000) if i % 99 == 0]
print(L)