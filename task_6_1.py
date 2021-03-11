list_res = []
tup = ()
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        content = line.split()
        tup = (content[0], content[5].replace('"', ''), content[6])
        list_res.append(tup)
        print(list_res)