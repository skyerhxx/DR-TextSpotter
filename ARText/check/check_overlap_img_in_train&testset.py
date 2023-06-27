import os

train_list = os.listdir('train/train_gt')
test_list = os.listdir('test/test_gt')
flag = 1
for i in test_list:
    if i in train_list:
        flag = 0
        print(i)

if flag == 1:
    print('No overlap imgs in train and test set')