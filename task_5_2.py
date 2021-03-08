n = int(input("Введите количество генерируемых нечетных чисел \n"))
nums_gen = (num for num in range(1, n + 1, 2))
for i in range(n // 2 + n % 2):
    print(next(nums_gen))