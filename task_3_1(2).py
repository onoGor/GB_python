dict_num = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(num_word):
    num_new = num_word.lower()
    if num_new in dict_num:
        str1 = dict_num[num_new]
        if num_word[0].isupper():
            str1 = str1.capitalize()
            print(str1)
        else:
            print(dict_num[num_new])
    else:
        return None


print('zero--one--two--three--four--five--six--seven--eight--nine--ten')
_num = input('Напишите какое число от 0 до 10 вы хотите перевести \n')
num_translate(_num)