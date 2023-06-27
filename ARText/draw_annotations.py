import os
import numpy as np
import json
import cv2
import matplotlib.pyplot as plt
import math
from PIL import Image, ImageDraw, ImageFont
import os.path as osp

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


dataset_type = 'train'
# dataset_type = 'test'


if not os.path.exists(f'draw_rect_{dataset_type}'):
    os.mkdir(f'draw_rect_{dataset_type}')
for i in os.listdir(f'../{dataset_type}/{dataset_type}_gt'):
    # i = '33266.json'
    print(i)
    name = i[:-5]
    
    image_path = osp.join(f'../{dataset_type}/{dataset_type}_img', name + '.jpg')
    json_path = osp.join(f'../{dataset_type}/{dataset_type}_gt', name + '.json')
    img_numpy = cv_imread(image_path)

    with open(json_path,encoding='utf-8') as f:
        gt = json.load(f)

    for x in gt["chars"]:
        points = x["points"]
        pts = np.array(points, np.int32).reshape(4, 2)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img_numpy,[pts],True,(0,0,255), 2)
        AddText = img_numpy.copy()
        cv2.putText(AddText, x['transcription'], (200, 100), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
        cv2.rectangle(img_numpy, (points[0], points[1]), (points[0]+20, points[1]+20),
                                  (255, 255, 255), thickness=-1)
        img_numpy = cv2ImgAddText(img_numpy, x['transcription'], left=points[0], top=points[1], textColor=(255, 0, 0), textSize=20)
    for x in gt["lines"]:
        if x['transcription'] == '###':
            continue
        points = x["points"]
        pts = np.array(points, np.int32).reshape(4, 2)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img_numpy,[pts],True,(0, 255, 255), 2)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    cv2.imencode('.jpg', np.array(img_numpy))[1].tofile(f'./draw_rect_{dataset_type}/'+name+'.jpg')
    plt.close()


