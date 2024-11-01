# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2006
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Rory", 22)
student2 = Student("April", 14)
student3 = Student("Martha", 6)
student4 = Student("GG", 7)

#print(Student.num_students)

#print(student2.name)
#print(student2.age)
#print(student2.class_year)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

