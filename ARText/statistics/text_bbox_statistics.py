#encoding=utf-8
import os
import json
from tqdm import tqdm
from collections import Counter


# dataset_type = 'test'
dataset_type = 'train'

list_ = []
dict_ = Counter()
cnt_all = 0
num_img = len(os.listdir(f'{dataset_type}/{dataset_type}_img'))
for i in tqdm(os.listdir(f'{dataset_type}/{dataset_type}_gt')):
    with open(f'{dataset_type}/{dataset_type}_gt/' + i,'r',encoding='utf-8')as f:
        item = json.load(f)
    num = 0
    for j in item['lines']:
        if j['ignore'] == 0:
            num += 1
            cnt_all += 1
    dict_[num] += 1
print('the number of valid text bbox(ignore=0) and its corresponding img number:')
print(dict_)
print(f'the number of valid text bbox in {num_img} imgs')
print(cnt_all)
print(f'the average number of valid text bbox in {num_img} imgs')
print(cnt_all / num_img)
