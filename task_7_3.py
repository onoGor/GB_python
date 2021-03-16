from os import path, listdir, walk
import shutil

root_dir = 'my_project'
for root, dirs, files in walk(root_dir):
    if 'templates' in dirs and root != root_dir:
        for dir_temp in listdir(path.join(root, 'templates')):
            try:
                shutil.copytree(path.join(root, 'templates', dir_temp), path.join(root_dir, 'templates', dir_temp))
                print('Шаблоны %s успешно создан' % path.join(root_dir, 'templates', dir_temp))
            except OSError:
                print('Шаблоны %s уже были созданы ранее' % path.join(root_dir, 'templates', dir_temp))




