tuple1=(5,10,15,20,25)
print(len(tuple1))
# tuple1[2]=100            # TypeError: 'tuple' object does not support item assignment
# print(tuple1[5])        #  IndexError: tuple index out of range
tuple1=tuple1+(8,9,"h")  # Concatination in tuple is possible.
print(tuple1) 