'''https://gitjournal.tech/sozdanie-i-udalenie-direktorij-s-pomoshhju-python/'''

starter = {
    'my_project': {
        'settings': {},
        'mainapp': {},
        'adminapp': {},
        'authapp': {},
     }
}


def create_starter(start, path):
    try:
        for item in start.keys():
            if not os.path.exists(item):
                os.mkdir(os.path.join(path, item))
            create_starter(start[item], os.path.join(path, item))
    except OSError:
        print("Создать директорию %s не удалось" % path)

if __name__ == '__main__':
    import os
    path = os.getcwd()
    create_starter(starter, path)
