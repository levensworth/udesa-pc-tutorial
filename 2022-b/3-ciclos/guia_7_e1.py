for i in range(9):
    print(i)

for i in range(15, 29):
    if i % 3 == 0:
        print(i)

for i in range(20, 9, -1):
    if i % 2 == 1:
        print(i)

word = input('ingrese palabra')
vocales = 'aeiou'
for c in word:
    if c in vocales:
        print(c)





