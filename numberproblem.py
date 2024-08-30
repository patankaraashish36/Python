import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)

def equal(arr,row):
  for i  in arr:
    if i == row:
      return (True)
    else:
      return False

row = [0,1,2,3]

print(equal(arr,row))