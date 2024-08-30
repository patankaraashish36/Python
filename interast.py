# pa = int(input())
# roi = float(input())
# tp = int(input())

# si = (pa*roi*tp)//100

# print(si)

# print(4*5.1//2)

print(0.1+0.2)


import math

def convert_fahrenheit_to_celsius_table(start: float, end: float, step: float) -> None:
    print("Fahrenheit   Celsius")
    print("---------------------")
    
    fahrenheit = start
    while fahrenheit <= end:
        celsius = (fahrenheit - 32) * 5.0/9.0
        if celsius >= 0:
            celsius = math.floor(celsius)  # Round down if non-negative
        else:
            celsius = math.ceil(celsius)   # Round up if negative
        print(f"{fahrenheit:9.2f}   {celsius:7.2f}")
        
        fahrenheit += step

# Test the function

start = 0
end = 100
step = 10

convert_fahrenheit_to_celsius_table(start, end, step)


from math import *

#Your code goes here
def fer_to_cel(start , end , step):
    fer = start
    
    while fer  <=  end:
        cel = 5/9 *(fer - 32)
        if cel >= 0:
            cel = floor(cel)
        else:
            cel = ceil(cel)

        print(fer , cel)
        fer = fer+ step

start = int(input())
end = int(input())
step = int(input())

fer_to_cel(start, end, step)