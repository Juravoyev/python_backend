# def user_data(first_name,last_name,age):
#     print(f"""
#     Ism : {first_name}
#     Familiya : {last_name}
#     Yosh : {age} """)
# name = input("Ismingiz: ")
# fam = input("Familiyangiz: ")
# age = int(input("Yoshingiz: "))
# user_data(name,fam,age)

# def find_max(a,b,c):
#     if a>b and a>c:
#         print(f"Eng katta son - A = {a}")
#     elif b>a and b>c:
#         print(f"Eng katta son - B = {b}")
#     elif c>a and c>b:
#         print(f"Eng katta son - C = {c}")
#     elif a==b and a>c:
#         print(f"Eng katta son - A va B = {b}")
#     elif b==c and b>a:
#         print(f"Eng katta son - B va C = {b}")
#     elif a==c and a>b:
#         print(f"Eng katta son - A va C = {a}")
#     else:
#         print(f"Eng katta son - A va B va C = {a}")
# find_max(9,9,9)

# def find_letter_count(word,letter):
#     return word.count(letter)
# print(find_letter_count('wordwarware','w'))

# def list_sum(mylist):
#     return f"Listning elementlar yig'indisi = {sum(mylist)}"
# print(list_sum([1,2,3,4,5,6,7,8,9]))

# def daraja(a,b):
#     print(f"{a}^{b}={a**b}")
# daraja(2,3)

# def daraja4(a,b,c,d):
#     print(f"{a}^{b}={a**b}\n"
#           f"{a}^{c}={a**c}\n"
#           f"{a}^{d}={a**d}")
# daraja4(2,3,4,5)

# def digit_count_and_sum(word):
#     digit_count = 0
#     digit_sum = 0
#     for char in word:
#         if char.isdigit():
#             digit_count +=1
#             digit_sum += int(char)
#     print(f"Raqamlar soni: {digit_count}\n"
#           f"Raqamlar yig'indisi: {digit_sum}.")
# digit_count_and_sum("2sdas2af4ewf5242")

# def add_right(a,b):
#     print(str(a)+str(b))
# add_right(34,32)

# def add_left(a,b):
#     print(str(b)+str(a))
# add_left(34,32)

# def work_with_list(a):
#     ma = min(a)
#     new_list = []
#     for i in a:
#         new_list.append(i*ma)
#     print(new_list)
# work_with_list([2,4,6,8])

# def big_sales(sales):
#     return max(sales, key=sales.get)
# print(big_sales({
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }))

# def min_max(numbers, max_num, min_num):
#     mx = max(numbers)
#     mn = min(numbers)
#     if max_num == mx:
#         print(f"{max_num} eng katta son.")
#     else:
#         print(f"{max_num} eng katta son emas.")
#     if min_num == mn:
#         print(f"{min_num} eng kichik son.")
#     else:
#         print(f"{min_num} eng kichik son emas.")
# min_max([1,2,3,4,5,6,7,8],8,2)


# products = [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ]
# def expensiveProduct(products):
#     max_price = 0
#     max_price_name = ""
#     for product in products:
#         if product["price"]>max_price:
#             max_price = product["price"]
#             max_price_name = product["name"]
#     return max_price_name
# print(expensiveProduct(products))