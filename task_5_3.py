tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Яна',
    'Анна', 'Олег'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

name_tuple = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))
print(type(name_tuple))
for gen_iter in range(len(tutors)):
    print(next(name_tuple))

