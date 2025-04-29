# def prime_generator():
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
#
# primes = prime_generator()
# for _ in range(6):
#     print(next(primes))
import itertools

# def password_generator(input_string):
#     for pwd in itertools.permutations(input_string):
#         yield "".join(pwd)
#
# input_string = "absd"
# passwords = password_generator(input_string)
# for _ in range(6):
#     print(next(passwords))

# def fibonachi_generator():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
#
# result = fibonachi_generator()
# for _ in range(10):
#     print(next(result))

# import itertools
# def generator_list(lst,m):
#     for i in itertools.combinations(lst,m):
#         yield ",".join(map(str,i))
#
# my_list = [1,2,3,4]
# n=2
# result = generator_list(my_list,n)
# for group in result:
#     print(group)