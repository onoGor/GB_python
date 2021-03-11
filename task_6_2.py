log_file = 'nginx_logs.txt'
spam_log = {}
with open(log_file, 'r', encoding='utf-8') as f:
    lines = (line.split()[0] for line in f)
    for i in lines:
        if i in spam_log:
            spam_log[i] += 1
        else:
            spam_log[i] = 1
spamer = sorted(spam_log, key=spam_log.get, reverse=True)
print(f'Внимание! С IP-адреса {spamer[0]} пришло {spam_log[spamer[0]]} запросов.\nПодозрение на спам')