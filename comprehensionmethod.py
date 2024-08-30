a=[i for i in range(12)]
print(a)
l= "hello i am aashish patankar and your welcome here"
if [ i for i in l if "aashish patnakar" in i]:
    l="aashish patankar"
    print(l)


# if __name__ == '__main__':
students = []
for _ in range(2):
    name = input()
    score = float(input())
    students.append([name, score])
second_lowest = sorted(list(set([name for name, score in students])))[1]
second_lowest_students = sorted([name for name, score in students if score == second_lowest])
print(second_lowest)
for student in second_lowest_students:
    print(student)
