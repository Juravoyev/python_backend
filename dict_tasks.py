# def str_counter(strs):
#     d = {}
#     for s in strs:
#         dic = dict([(len(s),s)])
#         d.update(dic)
#     return d
# print(str_counter(["shaftoli", "olma", "nok" ]))

# def merge_list(l1,l2):
#     d = {}
#     for i in l1:
#         for j in l2:
#             if l1.index(i)==l2.index(j):
#                 d.update(dict([(i,j)]))
#     return d
# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# print(merge_list(list_1, list_2))

# def counter_dict(nums):
#     d = {}
#     for num in nums:
#         d[num]=d.get(num,0)+1
#     return d
# list_nums = [2,1,1,1]
# print(counter_dict(list_nums))

# def max_ball_students(talabalar):
#     new_dict = {}
#     max_ball = 0
#     second_max_ball = 0
#     max_ball_name = ""
#     second_max_ball_name = ""
#     for k, v in talabalar.items():
#         if v > max_ball:
#             second_max_ball, second_max_ball_name = max_ball, max_ball_name
#             max_ball, max_ball_name = v, k
#         elif v > second_max_ball:
#             second_max_ball, second_max_ball_name = v, k
#     if max_ball_name:
#         new_dict[max_ball_name] = max_ball
#     if second_max_ball_name:
#         new_dict[second_max_ball_name] = second_max_ball
#     return new_dict
# print(max_ball_students({"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80}))
