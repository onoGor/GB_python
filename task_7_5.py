import os
import json
from collections import defaultdict
root_dir = 'some_data'
some_dict = defaultdict(tuple)
ext_tup = ()
for root, dir, files in os.walk(root_dir):
    for n in range(1, 6):
        count = len(([file for file in files if 10 ** (n-1) < os.path.getsize(os.path.join(root,file)) <= 10 ** n]))
        ext_tup = (count, list(set([file.split(".")[-1].lower() for file in files
                                    if 10 ** (n-1) < os.path.getsize(os.path.join(root, file)) <= 10 ** n])))
        some_dict[10 ** n] = ext_tup

file_dict = json.dumps(some_dict)
with open('some_data_summary.json', 'w', encoding='utf-8') as f:
    f.write(file_dict)
