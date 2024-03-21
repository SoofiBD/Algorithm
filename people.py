class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, name):
        return f'Hello {name}'


p = People('John', 36)
print(p.greet('John'))

p2 = People('Jane', 29)
print(p2.name , p2.age)
p2.greet('Jane')

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello'+ self.name)

a = Animal('Dog', 3)
a.greet()

class Student():
        
    n_instances = 0 # n_instances is a class attribute.
    
    def __init__(self, sid, name, gender):
        self.sid = sid
        self.name = name # name is a self attribute.
        self.gender = gender
        self.type = 'learning'
        Student.n_instances += 1
        
    def say_name(self):
        print("My name is " + self.name)
        
    def report(self, score):
        self.say_name()
        print("My id is: " + self.sid)
        print("My score is: " + str(score))
        
    def num_instances(self):
        print(f'We have {Student.n_instances}-instance in total')


s1 = Student("001", "Burak" , "M")
s1.say_name()
print(s1.type)
print(s1.gender)

s1.num_instances()

# Generating students with a for loop.
data = [["001", "Susan", "F"],
        ["002", "Mike", "M"]]

students= []
for i in data:
    sid, name, gender = i[0],i[1],i[2]
    students.append(Student(sid, name, gender))
print(students)

# 1. Way
[print(i.say_name()) for i in students]
# 2. Way
for i in students:
    i.say_name()
