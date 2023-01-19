# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

list1 = [1, 2, 3, 4, 6, 1, 7]
list2 = []
list2.append(list1[0])

for i, el in enumerate(list1):
    if el > list2[-1]:
        list2.append(el)
print(list2)


# for i in range(len(list1)):
#     if i != len(list1)-1:
#         if list1[i] < list1[i+1]:
#             list2.append(list1[i])
#         if list1[i] > list1[i+1]:
#             list2.append(list1[i])
#             print(list2)
#             list2.clear()
#     else:
#         list2.append(list1[i])
#         print(list2)
#         list2.clear()
