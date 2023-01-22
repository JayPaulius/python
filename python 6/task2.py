# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

list1 = [1, 2, 3, 5, 1, 5, 3, 10]
list2 = list(filter(lambda x: list1.count(x) == 1, list1))
list3 = [i for i in list1 if list1.count(i) == 1]
list4 = list(set(list1))
print(list2)
print(list3)
print(list4)