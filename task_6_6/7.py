# dicts = {}
# with open('bakery.csv', 'a') as f:
#     for line in enumerate(f):
#         dicts.items()

all_file = []
item_number = 5
new_value = '123'
with open('bakery.csv', 'r', encoding='utf-8') as f:
    for line in f:
        all_file.append(line.strip())
if item_number - 1 > len(all_file):
    print("попытка изменения не существующей записи")
else:
    all_file[item_number-1] = new_value
    with open('bakery.csv', 'w', encoding='utf-8') as f:
        f.write("\n".join(all_file))

