#  Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

nums = list(map(int, input('введите числа через пробел ').split()))
print(nums)
print(min(nums), max(nums))



# min = nums[0]
# max = nums[0]
# for i in nums:
#     if i < min:
#         min = i
#     if i > max:
#         max = i

# text = '12 3 45 6 78 91 23 4 56 7 8 9 '
# num = ''
# list1 = []
# for i in range(len(text)):
#     if text[i] != ' ':
#         num += text[i]
#     if  num != '' and text[i] == ' ' or i == len(text) - 1 and text[i] != ' ':
#         list1.append(int(num))
#         num = ''
# min = list1[0]
# max = list1[0]
# for i in list1:
#     if i < min:
#         min = i
#     if i > max:
#         max = i
# print(text)
# print(min, max)