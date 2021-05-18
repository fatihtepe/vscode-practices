wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

test = "hello"
l=[]
for i, x in enumerate(test):
    if x != ' ':
        x = x.upper()
        for y in test[i]:
            y = x
            changed_test_1 = test[i:].replace(test[i], y, 1)
            changed_test = test[:i] + changed_test_1
            l.append(changed_test)
print(l)

def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
printMax(3, 4)




lam = lambda x:'odd' if x % 2 else 'even'
print(lam(55))



vowel_list = ['a', 'e', 'i', 'o', 'u']
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  
vowels = filter(lambda x: True if x in vowel_list else False, first_ten) 

print('Vowels are :', list(vowels))