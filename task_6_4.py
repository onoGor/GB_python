if sum(1 for line in 'users.csv') < sum(1 for line in 'hobby.csv'):
    raise Exception('Exit code 1')
with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        for line in users:
            line = line.strip().replace(',',' ')
            hobby = hobbies.readline().strip()
            user_hobby = f'{line}: {hobby if hobby else None}\n'
            with open('users_hobby.txt', 'a', encoding='utf-8') as f:
                f.write(user_hobby)
        print('Записи успешно добавлены в файл users_hobby.txt')


