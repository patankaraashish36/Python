def halfPyramid():
    for i in range(5):
        for j in range(i+1):
            print(end="* ")
        print()
def invertedHalfPyramid():
    for i in range(5):
        for j in range(i, 5):
            print(end="* ")
        print()
def fullPyramid():
    for i in range(5):
        for s in range(i,5):
            print(end=" ")
        for j in range(i+1):
            print(end="* ")
        print()
def invertedFullPyramid():
    for i in range(5):
        for s in range(i):
            print(end=" ")
        for j in range(i,5):
            print(end="* ")
        print()
halfPyramid()
print("------------------------")
invertedHalfPyramid()
print("------------------------")
fullPyramid()
print("------------------------")
invertedFullPyramid()