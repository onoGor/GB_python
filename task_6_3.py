from itertools import zip_longest
with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        list_result = zip_longest((' '.join(user.split(',')) for user in users), hobby, fillvalue=None)
        dict_result = {str(el[0]).strip(): el[1] for el in list_result}
        with open('dict_result.csv', 'w', encoding='utf-8') as f:
            if 'None' in dict_result.keys():
                print('Exception code - 1')
            else:
                for key, value in dict_result.items():
                    if value == None:
                        f.writelines(f'\n{key} - {value}')
                    else:
                        f.writelines(f'{key} - {value}')
