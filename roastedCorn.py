
import random

def generate_random_numbers():
    numbers = []
    random.seed(50)
    for i in range(10):
        num = random.randint(1, 50)
        numbers.append(num)
    return numbers

def length_of_list(list):

    count = 0
    for item in list:
        count += 1

    return count
#
# list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
#
# even_sum = 0
# for i in range(len(list)):
#     if i % 2 == 0:
#         even_sum += list[i]
#
# print(even_sum)
#
# list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
#
# odd_sum = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         odd_sum += list[i]
#
# print(odd_sum)
#
# list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
#
# product = 1
# for i in range(len(list)):
#     if (i + 1) % 3 == 0:
#         product *= list[i]
#
# print(product)
#
# list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
#
# average = sum(list) / len(list)
#
# print(average)
#
# list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
#
# largest = list[0]
# for number in list:
#     if number > largest:
#         largest = number
#
# list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
#
# smallest = list[0]
# for num in list:
#     if num < smallest:
#         smallest = num
#
# print(smallest)
