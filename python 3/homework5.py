# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(num):
    list1 = [0, 1]
    for i in range(num - 1):
        list1.append(list1[i] - list1[i + 1])
    list1.reverse()
    for i in range(num - 1, num * 2 - 1):
        list1.append(list1[i] + list1[i + 1])
    return list1

def main():
    num = int(input("введите число: "))
    print(fibonacci(num))

main()

# num = int(input("введите число: "))
# list1 = []
# list2 = []
# check = False
# for i in range(0, num + 1):
#     if i == 0:
#         list1.append(0)
#     elif i == 1:
#         list1.append(1)
#     else:
#         list1.append((list1[i - 2] - list1[i - 1]))
# for i in range(0, num):
#     if i in [0, 1]:
#         list2.append(1)
#     else:
#         list2.append(list2[i - 1] + list2[i - 2])
# list1.reverse()
# print(list1 + list2)