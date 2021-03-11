def main(argv):
    program, *args = argv
    users = args[0]
    hobby = args[1]
    user_hobby = args[2]
    if sum(1 for line in users) < sum(1 for line in hobby):
        raise Exception('Exit code 1')
    with open(users, encoding='utf-8') as u_file:
        with open(hobby, encoding='utf-8') as h_file:
            for user in u_file:
                user = user.strip().replace(',', ' ')
                hobby = h_file.readline().strip()
                u_hobby = f'{user}: {hobby if hobby else None}\n'
                with open(user_hobby, 'a', encoding='utf-8') as f:
                    f.write(u_hobby)
            print('Записи успешно добавлены в файл users_hobby.txt')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))

