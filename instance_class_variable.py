class student:
    sub_name="python"  #  Class variable
    no_of_student=0

    def __init__(self,name,roll):
        self.name=name  # instance variable
        self.roll=roll
        self.id=132
        student.no_of_student+=1

    def details(self):
        print(f"The name is {self.name} , roll number is {self.roll} , id is {self.id} and subject name is {self.sub_name} . The total number of student is { self.no_of_student}")


s1=student("Aashish Patankar","D06")
# s1.details()
# student.sub_name="DS"
s1.sub_name="DS"
student.details(s1)

s2=student("Pa",21)
# s2.details()
student.details(s2)

        