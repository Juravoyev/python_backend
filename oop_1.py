# # Oson1. "Oson1" nomli klass elon qiling. Bu klassda "a" integer o'zgaruvchi bor.
# # output_a() - bu funksiya klassdagi "a" ni qiymatini print qilsin.
# class Oson1:
#     a = 0
#     @classmethod
#     def output_a(cls):
#         print(cls.a)
# Oson1.output_a()

# # Oson2. "Oson2" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchilari bor.
# # summa() - bu funksiya klassdagi "a" va "b" ni yig'indisini print qilsin.
# class Oson2:
#     a = 4
#     b = 5
#     @classmethod
#     def summa(cls):
#         print(cls.a+cls.b)
# Oson2.summa()

# # Oson3. "Oson3" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchisi bor.
# # plus_minus() - bu funksiya klassdagi "a" ni musbat yoki manfiy ekanligini print qilsin.
# class Oson3:
#     a = -4
#     @classmethod
#     def plus_minus(cls):
#         if cls.a>=0:
#             print("Musbat")
#         else:
#             print("Manfiy")
# Oson3.plus_minus()

# # Oson4. "Oson4" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
# # odd_even() - bu funksiya klassdagi "a" ni to'g yoki juft ekanligini print qilib bersin.
# class Oson4:
#     a = 5
#     @classmethod
#     def odd_even(cls):
#         if cls.a%2==0:
#             print("Juft")
#         else:
#             print("Toq")
# Oson4.odd_even()

# # Oson5. "Oson5" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchisi bor.
# # daraja() - bu funksiya klassdagi "a" ni "b" chi darajasini print qilsin.
# class Oson5:
#     a = 2
#     b = 5
#     @classmethod
#     def daraja(cls):
#         print(cls.a**cls.b)
# Oson5.daraja()

# # 6. "MyClass6" nomli klass elon qililar. Bu klassda "words" list bo'sh o'zgaruvchisi bor.
# # add_word(word) - bu funksiya "words" ga element qo'shib qo'ysin.
# # remove(word) = bu funksiya "words" da "word" ni o'chirib tashlasin.
# class MyClass6:
#     def __init__(self):
#         self.words = []
#     def add_word(self,word):
#         self.words.append(word)
#     def remove(self, word):
#         self.words.remove(word)
#     def print(self):
#         print(self.words)
# ob = MyClass6()
# ob.add_word("olma")
# ob.add_word("nok")
# ob.add_word("banan")
# ob.remove("nok")
# ob.print()

# # 7. "MyClass7" nomli klass elon qiling. Bu klassda bo'sh "myDict" dictionary o'zgaruvchisi bor.
# # add_elem(key, val) - bu funksiya "myDict" "key" ni qiymatiga teng bo'lgan key bo'lmasa "val" ni add qilsin,
# # bor bolsa xech narsa qilmasin.
# # update_elem(key, val) - bu funksiya "myDict" shu "key" ni qiymatiga teng bolgan key bo'lsa "val" ni update qilsin,
# # yoq bolsa xech narsa qilmasin.
# class MyClass7:
#     myDict = {}
#     @classmethod
#     def add_elem(cls,key,val):
#         if key not in cls.myDict.keys():
#             cls.myDict[key] = val
#     @classmethod
#     def update_elem(cls,key,value):
#         if key in cls.myDict.keys():
#             cls.myDict[key] = value
#     @classmethod
#     def print_dict(cls):
#         print(cls.myDict)
#
# MyClass7.add_elem('ism', "Shams")
# MyClass7.update_elem('yosh', 18)
# MyClass7.add_elem('yosh', 20)
# MyClass7.update_elem('yosh', 18)
# MyClass7.print_dict()

# # 8. "MyClass8" nomli klass elon qililar. Bu klassdan "numbers" list o'zgaruvchisi bor.
# # compare_lists(new_list) - bu funksiya klassdagi "numbers" ni elementlar yig'indisi
# # "new_list" ni elementlar yig'indisidan katta aniqlab katta listni print qilsin.
# class MyClass8:
#     numbers = []
#     @classmethod
#     def compare_lists(cls,new_list):
#         summa_num = sum(cls.numbers)
#         summa_new = sum(new_list)
#         if summa_num>summa_new:
#             print(cls.numbers)
#         elif summa_new == summa_num:
#             print("BU listlar teng")
#         else:
#             print(new_list)
# MyClass8.numbers.extend([12,34,45,56,67,78,90])
# MyClass8.compare_lists([12,34,45,56,67,78,91])

# # 9. "MyClass9" nomli klass elon qililar. Bu klassdan "list1" va "list2" list o'zgaruvchilari bor.
# # list1_max() - bu funksiya klassdagi "list1" dan maximumni topib return qilsin.
# # list2_max() - bu funksiya klassdagi "list2" dan maximumni topib return qilsin.
# # sum_of_two_max() - bu funksiya klassdagi list1_max() va list2_max() foydalanib ikkita maximumni topib yig'indisini print qilsin.
# class MyClass9:
#     list1 = [1,2,3,4,5]
#     list2 = [6,7,8,9]
#     @classmethod
#     def list1_max(cls):
#         return max(cls.list1)
#     @classmethod
#     def list2_max(cls):
#         return max(cls.list2)
#     @classmethod
#     def sum_of_two_max(cls):
#         print(cls.list1_max()+cls.list2_max())
# MyClass9.sum_of_two_max()

# # 10. "MyClass10" nomli klass elon qililar. Bu klass "numbers" list o'zgaruvchilari bor.
# # divide(d) - bu funksiya klassadagi "numbers" list elementlarini "d" qoldiqsiz bo'linsa bitta list yig'sin funksiyani ichida.
# # va funksiya oxirida bolinadigonlarni listini return qilsin.
# class MyClass10:
#     numbers = []
#     @classmethod
#     def divide(cls,d):
#         list1 = []
#         for i in cls.numbers:
#             if i%d == 0:
#                 list1.append(i)
#         return list1
# MyClass10.numbers.extend([1,2,3,4,5,6,7,8,9])
# print(MyClass10.divide(2))