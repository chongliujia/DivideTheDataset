# -*- coding:utf-8 -*-

import torch
import torchvision.datasets as dset

dataset = dset.ImageFolder('Your-Dataset-File/')
dataset.classes
dataset.class_to_idx

data = []
for file in dataset.imgs:
    data.append(file)

print(len(data))

""" 下面就是对数据集进行比例划分 
训练集:测试集:有效集 = 6:2:2
"""
train_size = int(0.6 * len(data))
test_size  = int(0.2 * len(data))
val_size   = int(0.2 * len(data))


print("train_size:{}".format(train_size))
print("test_size:{}".format(test_size))
print("val_size:{}".format(val_size))

train_dataset, test_dataset, val_dataset = torch.utils.data.random_split(data, [train_size, test_size, val_size])

#将训练集标记存入txt文件中
train_imgList_line = []

for line in train_dataset:
    train_imgList_line.append(line[0])
    train_imgList_line.append(line[1])

with open('train.txt', 'wt') as f:
    i = 0
    for line in train_imgList_line:
        if i == train_size:
            break

        if i % 2 == 0:
            f.write(str(line) + ' ')
        else:
            f.write(str(line) + '\n')
        i = i + 1

#将测试集标记存入txt文件中
test_imgList_line = []

for line in test_dataset:
    test_imgList_line.append(line[0])
    test_imgList_line.append(line[1])

with open('test.txt', 'wt') as f:
    i = 0
    for line in test_imgList_line:
        if i == test_size:
            break

        if i % 2 == 0:
            f.write(str(line) + ' ')
        else:
            f.write(str(line) + '\n')
        i = i + 1



#将有效集标记存入txt文件中
val_imgList_line = []

for line in val_dataset:
    val_imgList_line.append(line[0])
    val_imgList_line.append(line[1])

with open('val.txt', 'wt') as f:
    j = 0
    for line in val_imgList_line:
        if j == val_size:
            break

        if j % 2 == 0:
            f.write(str(line) + ' ')
        else:
            f.write(str(line) + '\n')
        j = j + 1