from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(iter, flag=0):
    """Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
    взятых из трёх списков (по одному из каждого):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    """
    joke_list = []
    str_joke = ''
    _add = 0
    if flag:
        if iter > 5:    #больше 5 итерация в данном случае невозможно
            iter = 5
        i = 0
        for i in range(iter):
            str_n = choice(nouns)
            str_adv = choice(adverbs)
            str_adj = choice(adjectives)
            str_joke = str_n + ' ' + str_adv + ' ' + str_adj
            nouns.remove(str_n)
            adverbs.remove(str_adv)
            adjectives.remove(str_adj)
            joke_list.append(str_joke)
            str_joke = ''
        print(joke_list)
    else:
        i = 0
        for i in range(iter):
            str_joke = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
            joke_list.append(str_joke)
            str_joke = ''
        print(joke_list)


get_jokes(7)    #с повторами
get_jokes(5, 1)      #без повторов
# print(help(get_jokes))