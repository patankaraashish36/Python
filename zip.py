letters = ['a', 'b', 'c']
numbers = [0, "c", 2]
c = 0
for l,n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    if l == n :
        c += 1
print(c)
...
# Letter: a
# Number: 0
# Letter: b
# Number: 1
# Letter: c
# Number: 2