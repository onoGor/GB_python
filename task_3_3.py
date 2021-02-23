

def thesaurus(*names):
    dict_names = {}
    for name in names:
        if name[0] not in dict_names.keys():
            dict_names.update({name[0]: [name]})
        else:
            dict_names[name[0]].append(name)
    return dict_names


let_name = thesaurus("Иван", "Мария", "Петр", "Илья", "Юрий", "Анна", "Полина", "Антон", "Максим", "Александр")
#словарь с сортировкой по ключам
for k in sorted(let_name.keys()):
    print(k, ':', let_name[k])
