# import time

# def fibonacciNumber_with_memo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         result = fibonacciNumber_with_memo(n-1, memo) + fibonacciNumber_with_memo(n-2, memo)
#         memo[n] = result
#         return result

# def fibonacciNumber_with_list(n):
#     fib_list = [0, 1]  # Initialize list with first two Fibonacci numbers

#     # If n is 0 or 1, return the corresponding value
#     if n == 0:
#         return fib_list[0]
#     elif n == 1:
#         return fib_list[1]

#     # Calculate Fibonacci numbers up to n if not already in the list
#     for i in range(2, n + 1):
#         fib_list.append(fib_list[i - 1] + fib_list[i - 2])

#     return fib_list[n]

# # Test the performance for large value of n
# large_n = 10

# start_time_memo = time.time()
# fib_memo_result = fibonacciNumber_with_memo(large_n)
# end_time_memo = time.time()
# time_taken_memo = end_time_memo - start_time_memo

# start_time_list = time.time()
# fib_list_result = fibonacciNumber_with_list(large_n)
# end_time_list = time.time()
# time_taken_list = end_time_list - start_time_list

# # Print results
# print(f"Fibonacci({large_n}) with memoization: {fib_memo_result}")
# print(f"Time taken with memoization: {time_taken_memo:.6f} seconds")

# print(f"\nFibonacci({large_n}) with list: {fib_list_result}")
# print(f"Time taken with list: {time_taken_list:.6f} seconds")


# def fibonacciNumber(n):
#     # Write your code here.
#     l = [0,1]
#     if n == 1 or n == 2 :
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         result = fibonacciNumber(n-1)+fibonacciNumber(n-2)
#         l.append(result)
#         return l[n]

# def fibonacciNumber(n):
#     # Write your code here.
#     d = {}
#     if n in d:
#         return d[n]
#     if n == 1 or n == 2 :
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         result = fibonacciNumber(n-1)+fibonacciNumber(n-2)
#         d[n] =  result
#         return d[n]




def fibonacciNumber(n):
    mod = (10**9)+7;
    a = 0;
    b = 1;

    for i in range(2, n+1):
        c = (a+b)%mod;
        a=b;
        b=c;
    return b;
print(fibonacciNumber())   


