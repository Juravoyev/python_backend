# def deco(f):
#     def g(*args,**kwargs):
#         result = f(*args,**kwargs)
#         return result.upper()
#     return g
# @deco
# def kotta_qil(soz):
#     return soz
# print(kotta_qil("salom"))

# def deco(f):
#     def g(*args,**kwargs):
#          result = f(*args,**kwargs)
#          natija = result[::-1]
#          return natija
#     return g
# @deco
# def word(soz):
#     return soz
# print(word("hello"))
# import time

# def deco(f):
#     def g(*args, **kwargs):
#         begin = time.time()
#         result = f(*args, **kwargs)
#         end = time.time()
#         print(f"Ketgan vaqt: {end - begin:.6f} soniya")
#         return result
#     return g
#
# @deco
# def kvadrat(x):
#     return x**2

# print(kvadrat(2))

# def deco(f):
#     count = 0
#     def g(*args,**kwargs):
#         nonlocal count
#         result = f(*args,**kwargs)
#         count += 1
#         print(f"Chaqirildi:{count}")
#         print(f"{f.__name__} funksiyasi chaqirildi.")
#         return result
#     return g
# @deco
# def prrint():
#     return "Hello world"
# print(prrint())
# print(prrint())

n,count = 5,0
for _ in range(n):
    global n
    n -= 1
    count +=1
print(count)
