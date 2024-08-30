d ={}
n,m = input().split()
d[n] = m
print(d)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    # print(obj)
    for y in obj:
	    print(y + ':', obj[y])
