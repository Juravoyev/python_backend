# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def deposit(self,deposit):
#         self.balance = self.balance + deposit
#         print(f"Balansizga {deposit} so'm qushildi.Balansingiz {self.balance}.\n")
#     def withdraw(self,withdraw):
#         self.balance -= withdraw
#         print(f"Balansizga {withdraw} so'm yechildi.Balansingiz {self.balance}.\n")
#     def check_balance(self):
#         print(f"Balansingiz {self.balance}.\n")
# account = BankAccount(100_000)
# account.deposit(150_000)
# account.withdraw(50_000)
# account.check_balance()

# class Rectangle:
#     def __init__(self,lenght,width):
#         self.lenght = lenght
#         self.width = width
#     def area(self):
#         print(f"S={self.lenght*self.width}")
#     def perimetr(self):
#         print(f"P={2*(self.lenght+self.width)}")
#     def is_squre(self):
#         if self.lenght == self.width:
#             print("Kvadrat")
#         else:
#             print("Kvadrat emas")
# abcd = Rectangle(3,4)
# abcd.area()
# abcd.perimetr()
# abcd.is_squre()

# class Student:
#     def __init__(self,name,age,grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#     def add_grade(self,grade):
#         self.grades.append(grade)
#     def calculate_average(self):
#         result = 0
#         count = 0
#         for i in self.grades:
#             result += i
#             count += 1
#         return f"O'rtacha baho:{result/count}."
#     def print_summary(self):
#         print(f"Ismi:{self.name}, yoshi:{self.age},\nBaholar:{self.grades}, O'rta bahosi:{self.calculate_average()}")
# shams = Student("Shams",18,[4])
# shams.add_grade(5)
# shams.add_grade(5)
# print(shams.calculate_average())
# shams.print_summary()


# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         print(f"S={math.pi*self.radius**2}")
#     def circumference(self):
#         print(f"l={2*math.pi*self.radius}")
#     def diametr(self):
#         print(f"d={self.radius*2}")
# davra = Circle(5)
# davra.diametr()
# davra.area()
# davra.circumference()

# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#         self.current_page = 1
#     def open(self,page):
#         self.current_page = page
#         print(f"{self.title} kitobi {self.current_page} sahifadan ochildi.")
#     def turn_page(self):
#         self.current_page += 1
#         print(f"Sahifa o'zgartirildi.Hozir{self.current_page} da turibdi.")
#     def restart(self):
#         self.current_page = 1
#         print(f"Kitob sahifasi:{self.current_page}")
# atom_odatlar = Book("Atom odatlar","Jeyms Klir")
# atom_odatlar.open(35)
# atom_odatlar.turn_page()
# atom_odatlar.turn_page()
# atom_odatlar.restart()

# class Dog:
#     total_dogs = 5
#     @classmethod
#     def get_total_dogs(cls):
#         return cls.total_dogs

# class Computer:
#     total_computers = 3
#     computers_list = ["hp","asus","acer"]
#     @classmethod
#     def add_computer(cls,comp):
#         cls.computers_list.append(comp)
#         cls.total_computers +=1
# lenovo = Computer
# lenovo.add_computer("lenovo")
# print(lenovo.computers_list)
# print(lenovo.total_computers)

# class Employee:
#     total_employees = 0
#     employees_list = []
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.hire_employee()
#     def hire_employee(self):
#         Employee.employees_list.append(self)
#         Employee.total_employees += 1
#     @classmethod
#     def get_total_employees(cls):
#         return cls.total_employees
#     @classmethod
#     def list_employees(cls):
#         for emp in cls.employees_list:
#             print(f"Ism: {emp.name}, Lavozim: {emp.position}")
# e1 = Employee("Ali", "Dasturchi")
# e2 = Employee("Laylo", "Analitik")
# e3 = Employee("Jasur", "Dizayner")
# print("Umumiy xodimlar soni:", Employee.get_total_employees())
# print("\nXodimlar ro'yxati:")
# Employee.list_employees()

# class Television:
#     def __init__(self,name):
#         self.name = name
#         Television.average_screen_size += 2
#     average_screen_size = 34
#     @classmethod
#     def update_average_screen_size(cls):
#         print(cls.average_screen_size)

# class Course:
#     total_courses = 0
#     courses_list = []
#     @classmethod
#     def add_course(cls,name):
#         cls.courses_list.append(name)
#         cls.total_courses += 1
#     @classmethod
#     def print(cls):
#         print(cls.total_courses,cls.courses_list)

# class Math:
#     @staticmethod
#     def multiply(x,y):
#         return x*y

# class Temperature:
#     @staticmethod
#     def celsius_to_fahrenheit(cls):
#         return (cls*(9/5))+32
# print(Temperature.celsius_to_fahrenheit(25))

# class Distance:
#     @staticmethod
#     def miles_to_kilometers(mil):
#         return mil*1_000_000

# class Utility:
#     @staticmethod
#     def is_even(x):
#         if x % 2 == 0:
#             return "Ha"
#         else:
#             return "Yo'q"
# print(Utility.is_even(24))

# class Time:
#     @staticmethod
#     def seconds_to_minutes(sec):
#         sec_ = sec % 60
#         return f"{sec//60} min, {sec_} s."
# print(Time.seconds_to_minutes(150))





