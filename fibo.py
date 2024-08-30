def fibo(f):
  if n==1:
    return 0
  elif n==2:
    return 1
  else:
    return(fibo(f-1)+fibo(f-2))

n = 5
for i in range(1, n+1):
   print(fibo(i))