# lines=["12,34,56""\n","43,5,6,7","\n","34,5,67"]
# f.writelines((lines))
# f.close()
# with  open("hello.txt", "r") as f:
#   i=0
#   while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#       break
    
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"student {i}  marks in en {m1}")
#     print(f"student {i}  marks in maths {m2}")
#     print(f"student {i}  marks in sceince {m3}")


    # Advance file handling
with open("help.txt","w") as k:
    k.write("HELLO PYTHON")
    k.seek(17)
    with open("help.txt","r") as j:
      j.seek(6)
      print(j.tell())
      m=j.read(6)
      print(m)

with open("pa.txt","w")as p:
   p.write("PA 122 0R 123 132 0R 133" )
   p.truncate(2)
with open("pa.txt", "r")as p:
   print(p.read())