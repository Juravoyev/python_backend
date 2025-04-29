# #1
# class Texnika:
#     def __init__(self, brand, model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(f"Brand:{self.brand},\nmodel:{self.model}\ntype:{self.type}")
#
#
# class Notebooks(Texnika):
#     def __init__(self, brand, model, type, video_card, ram, display):
#         super().__init__(brand, model, type)
#         self.video_card = video_card
#         self.ram = ram
#         self.display = display
#
#     def more_info(self):
#         print(f"""Brand:{self.brand},
#         model:{self.model}
#         type:{self.type}
#         video_card:{self.video_card}
#         ram:{self.ram}
#         display:{self.display}""")
#
#
# class Televisions(Texnika):
#     def __init__(self, brand, model, type, size, display):
#         super().__init__(brand, model, type)
#         self.size = size
#         self.display = display
#
#     def more_info(self):
#         print(f"""Brand:{self.brand},
#                 model:{self.model}
#                 type:{self.type}
#                 size:{self.size}
#                 display:{self.display}""")
#
#
# class Smartphones(Texnika):
#     def __init__(self, brand, model, type, size, sim_count):
#         super().__init__(brand, model, type)
#         self.size = size
#         self.sim_count = sim_count
#
#     def more_info(self):
#         print(f"""
#                         Brand:{self.brand},
#                         model:{self.model}
#                         type:{self.type}
#                         size:{self.size}
#                         sim_count:{self.sim_count}""")

#2
# class University:
#     def __init__(self,university):
#         self.university = university
#     def info(self):
#         print(f"University:{self.university}")
# class Staff(University):
#     def __init__(self,university,first_name,last_name,age):
#         super().__init__(university)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def staff_info(self):
#         print(f"""
# University:{self.university}
# First_name:{self.first_name}
# Last_name:{self.last_name}
# Age:{self.age}
# """)
# class Student(Staff):
#     def __init__(self, university, first_name, last_name,age, group):
#         super().__init__(university,first_name,last_name,age)
#         self.group = group
#     def more_info(self):
#         print(f"""
#         University:{self.university}
#         First_name:{self.first_name}
#         Last_name:{self.last_name}
#         Age:{self.age}
#         Group:{self.group}
#         """)
# class Teacher(Staff):
#     def __init__(self, university, first_name, last_name,age, position,subject):
#         super().__init__(university,first_name,last_name,age)
#         self.position = position
#         self.subject = subject
#     def more_info(self):
#         print(f"""
#         University:{self.university}
#         First_name:{self.first_name}
#         Last_name:{self.last_name}
#         Position:{self.position}
#         Subject:{self.subject}
#         """)
# class OtherStaff(Staff):
#     def __init__(self, university, first_name, last_name,age, position):
#         super().__init__(university,first_name,last_name,age)
#         self.position = position
#     def more_info(self):
#         print(f"""
#         University:{self.university}
#         First_name:{self.first_name}
#         Last_name:{self.last_name}
#         Position:{self.position}
#         """)
# class Object(University):
#     def __init__(self,university,name):
#         super().__init__(university)
#         self.name = name
#     def object_info(self):
#         print(f"""
# Universitet:{self.university}
# Name:{self.name}
# """)
# class Computer(Object):
#     def __init__(self,university,name,soni,tizimi,holati):
#         super().__init__(university,name)
#         self.soni = soni
#         self.tizimi = tizimi
#         self.holati = holati
#     def object_more_info(self):
#         print(f"""
# Universitet:{self.university}
# Name:{self.name}
# Soni:{self.soni}
# Tizimi:{self.tizimi}
# Holati:{self.holati}""")
# class Mebel(Object):
#     def __init__(self,university,name,soni,turi,holati):
#         super().__init__(university,name)
#         self.soni = soni
#         self.turi = turi
#         self.holati = holati
#     def object_more_info(self):
#         print(f"""
# Universitet:{self.university}
# Name:{self.name}
# Soni:{self.soni}
# Tizimi:{self.turi}
# Holati:{self.holati}""")
