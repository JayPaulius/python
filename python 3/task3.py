# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1


my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу", "йцукен"]
print(my_list)
text = input()
ind = 0
pos = -1

for i in range(len(my_list)):
    if text in my_list[i]:
        ind += 1
        if ind == 2:
            pos = i
print(pos)


# def find_index_coin(new_list, text, num=2):
#     count = 0
#     for i in range(len(new_list)):
#         if text in my_list[i]:
#             count += 1
#         if count == num:
#             return i
#     return -1

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# print(find_index_coin(my_list, 'qwe'))

# list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# print(list)
# ind = 0
# text = input()
# if text in list:
#     ind = list.index(text)
#     if text in list[ind+1:]:
#         ind = list.index(text, ind+1)
#         print(ind)
#     else:
#         print(-1)   
# else:
#     print('в списке нет указанной строки')