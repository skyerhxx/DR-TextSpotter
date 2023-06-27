import os
import mmcv
from tqdm import tqdm

test_list = []
for i in tqdm(os.listdir('test/test_gt')):
    content = mmcv.load(f"test/test_gt/{i}")
    for char in content['chars']:
        test_list.append(char['transcription'])
test_list = list(set(test_list))

train_list = []
for i in tqdm(os.listdir('train/train_gt')):
    content = mmcv.load(f"train/train_gt/{i}")
    for char in content['chars']:
        train_list.append(char['transcription'])
train_list = list(set(train_list))

#这里如果看len(train_list)和len(test_list)都比statics中统计的要少1，是因为没有统计'#'
diff = [item for item in test_list if item not in train_list]
if diff == []:
    print('All characters in testset have occured in trainset.')