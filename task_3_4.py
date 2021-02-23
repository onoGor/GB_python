

def thesaurus_adv(*let_names):
    print(*let_names)
    dict_names = {}
    dict_letters = {}
    for name in let_names:
        names = name.split()[0]
        surnames = name.split()[1]
        if surnames[0] not in dict_letters.keys():
            dict_letters.update({surnames[0]: {}})
    for letter in dict_letters.keys():
        dict_names = {}
        for name in let_names:
            names = name.split()[0]
            surnames = name.split()[1]
            if surnames[0] == letter:
                if names[0] not in dict_names.keys():
                    dict_names.update({names[0]: [name]})
                else:
                    dict_names[names[0]].append(name)
        dict_letters.update({letter: dict_names})
    return dict_letters


let_name = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Полина Александрова", "Семен Апухтин")
#словарь с сортировкой по ключам
for k in sorted(let_name.keys()):
    print(k, ':', let_name[k])
