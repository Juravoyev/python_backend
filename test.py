# def closures(f, g):
#     def sm(*args, **kwargs):
#         return f(g(*args, **kwargs))
#
#     return sm
#
#
# km_to_m = lambda x: x * 1000
# m_to_sm = lambda y: y * 100
# a = closures(m_to_sm,km_to_m)
# print(a(12))

# talabalar = {}
#
# while True:
#     ism = input("Ismingizni kiriting (yoki 'stop' tugatish uchun): ")
#     if ism.lower() == "stop":
#         break
#     yosh = int(input("Yoshingizni kiriting: "))
#     fakultet = input("Fakultetingizni kiriting: ")
#
#     talabalar[ism] = {
#         "yosh": yosh,
#         "fakultet": fakultet
#     }
#
# for key,value in talabalar.items():
#     print(f"{key}  {value['yosh']}  {value['fakultet']}")
mydict  = {'ism':"Shams", 'age':18,',manzil':"Toshkent"}
print(mydict.keys())
print(mydict.keys())
if mydict.keys() == 'age':
    mydict['age'] = 20
print(mydict)