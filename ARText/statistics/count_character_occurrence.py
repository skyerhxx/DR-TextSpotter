#encoding=utf-8
import os
import json
from tqdm import tqdm

# dataset_type = 'test'
dataset_type = 'train'

list_ = []
dict_ = {}
cnt = 0
for i in tqdm(os.listdir(f'{dataset_type}/{dataset_type}_gt')):
    with open(f'{dataset_type}/{dataset_type}_gt/' + i,'r',encoding='utf-8')as f:
        item = json.load(f)
    for j in item['lines']:
        for c in j['transcription']:
            if c not in dict_.keys():
                dict_[c] = 0
            dict_[c] += 1
    cnt += 1
print(cnt)
dict_= sorted(dict_.items(), key=lambda d:d[1], reverse = True)
print(dict_)

#保存成json文件
# b = json.dumps(dict_, ensure_ascii=False)
# f2 = open('new_json.json', 'w',encoding='utf-8')
# f2.write(b)
# f2.close()
# print(len(dict_))  

