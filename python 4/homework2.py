# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def check_number(n):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return n
    else:
        return 0

def prime_numbers(n):
    prime_nums = []
    for i in range(2, n + 1):
        if check_number(i) != 0:
            prime_nums.append(check_number(i))
    return prime_nums

def factorization_number(n, prime_nums):
    num_factors = []
    j = 0
    while n > 1:
        if n % prime_nums[j] == 0:
            num_factors.append(prime_nums[j])
            n /= prime_nums[j]
        else:
            j += 1
    return num_factors

def main():
    num = int(input('введите число > 1: '))
    while num <= 1: num = int(input('введите число > 1: '))
    num_factors = []
    if num == check_number(num):
        print(f'число {num} - простое')
    else:
        num_factors = (factorization_number(num, prime_numbers(num)))
        print(" * ".join(map(str,num_factors)) + ' = ' + str(num))
        print('простые множители: ' + ', '.join(map(str, set(num_factors))))

main()