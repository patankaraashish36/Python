# def findTriplets(arr, n, k):
    
#     # Write your code here.
#     L = []
    
#     for i in arr:
#         for j in arr:
#             for m in arr:
#                 if i+j+m == k:
#                     triple = [i, j, m]
#                     triple.sort()
#                     if triple not in L:
#                         L.append(triple)
#     return L if L else [-1]
# x= findTriplets([1,2,3,4],4,11)
# print(x)


def findTriplets(arr, n, k):
    L = []
    for i in arr:
        for j in arr:
            for m in arr:
                if i + j + m == k:
                    triplet = [i, j, m]
                    triplet.sort()
                    if triplet not in L:
                        L.append(triplet)
    return L if L else [-1]


# Test the function
# arr1 = [1, 2, -3, 4, 5, -2]
# n1 = len(arr1)
# k1 = 0
# print(findTriplets(arr1, n1, k1))  # Output: [[-3, 1, 2], [-2, 0, 2], [-2, -3, 5]]

# arr2 = [1, 1, 2, 2, 3, 3]
# n2 = len(arr2)
# k2 = 6
# print(findTriplets(arr2, n2, k2))  # Output: [[1, 2, 3]]

arr3 = [1, 2, 3, 4, 5]
n3 = len(arr3)
k3 = 10
print(findTriplets(arr3, n3, k3))  # Output: [-1]
