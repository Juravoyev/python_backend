# 1. While siklidan foydalanib print qiling:
# 1
# 22
# 333
# 4444
# 55555

# son = 1
# while son<=5:
#     print(str(son)*son)
#     son+=1

# 2. While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.
# input: 555   output: 15
# input: 8125   output: 16

# print("Sondagi raqamlar yig'indisini topadigan dastur.")
# son = int(input("Sonni kiriting: "))
# yigindi = 0
# while son > 0:
#     yigindi += son % 10
#     son //=10
# print("Raqamlar yigindisi:",yigindi)

# 3. While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing

# toq = 1
# yigindi = 0
# while toq < 100:
#     yigindi +=toq
#     toq +=2
# print("1 dan 100 gacha toq sonlar yig'indisi:",yigindi)

# 4. While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing

# ruyxat = [1,2,3,4,5,6,7,8,9]
# n = 0
# while n<8:
#     if ruyxat[n]<ruyxat[n+1]:
#         max = ruyxat[n]
#     else:
#         max = ruyxat[n+1]
#     n +=1
# print(max)

# 5. Taxmin qilish o'yini

# import random
# son = random.randint(1,100)
# print("Tahmin qilish uyini (1 dan 100 gacha).")
# while True:
#     tahmin = int(input("Tahminingiz:"))
#     if tahmin > son:
#         print("Juda baland!")
#     elif tahmin == son:
#         print("Tabriklaymiz topdingiz!!!")
#         break
#     else:
#         print("Juda past!")



