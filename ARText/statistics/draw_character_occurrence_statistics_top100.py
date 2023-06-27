#encoding=utf-8
#在linux下执行的话可能需要设置一下字体；windows下可以顺利执行
import os
import shutil 
import json
import matplotlib.pyplot as plt
import numpy as np


# dataset_type = 'test'
dataset_type = 'train'
dict_ = {}
data = []
labels = []
with open(f'../statistics/character_occurrence_statistics-{dataset_type}set.json','r',encoding='utf-8')as f:
    a = json.load(f)
cnt = 0
for i in range(1,100):
    if '\u4e00' <= a[i][0] <= '\u9fff':
        labels.append(a[i][0])
        data.append(a[i][1])
        print(a[i][0],a[i][1])
        cnt += 1
    if cnt == 30:
        break 
    
plt.figure(figsize=(20, 20)) 
colors = ["#4E79A7",  "#A0CBE8",  "#F28E2B",  "#FFBE7D",  "#59A14F",  "#8CD17D",  "#B6992D",  "#F1CE63",  "#499894",  "#86BCB6",  "#E15759",  "#E19D9A"]
plt.rcParams['font.sans-serif']='KaiTi'
plt.ylabel('Occurrence number')
plt.bar(range(len(data)), data, tick_label=labels, color = colors)
plt.savefig(f'character_occurrence_statistics_top100-{dataset_type}set.jpg')
        

        








