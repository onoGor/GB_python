def generator(n):
    for num in range(1, n + 1, 2):
        yield num


n = int(input("Введите количество генерируемых нечетных чисел \n"))
odd_to_n = generator(n)
print(*odd_to_n)
