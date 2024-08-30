s1 = ".|."
s2 = "WELCOME"
n, m = map(int, input().split())
for i in range(n//2):
    print((s1*((i*2)+1)).center(m, "-"))

print(s2.center(m, "-"))

for i in range(((n//2)-1), -1, -1):
    print((s1*((i*2)+1)).center(m, "-"))
    