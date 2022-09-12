#批量处理多帧数据
#使用pd.dataframe
import imp
import os
import time
from tkinter.tix import FileSelectBox
from unittest.loader import VALID_MODULE_NAME 
import pandas as pd
import linecache
import string
import warnings
warnings.filterwarnings("ignore")#忽略所有的警告，继续执行，主要是为了屏蔽pd.append要换为pd.concat的警告
start = time.time()
##定义函数——名称为：去除文件头，比如文件的头3行或头9行比较麻烦处理，文件比较多，可以使用该函数
    ##输入为文件名称和，需要去掉的行
def delete_top(files):#删除每个txt文件的头2行
    files = os.listdir(files)#创建路径下所有文件的列表
    files.sort()#初始化排序文件
    files.sort(key = lambda x: float(x[:-4]))#按照数字大小排序
    for file in files:
        print("\t" + file)#打印输出排序结果
    for file in files:
        file = filepath + '/'+ file
        with open(file, 'r', encoding = 'utf-8') as d:
            contents = d.readlines()#遍历所有的文件，除了代码输出文件以外的所有文件的每一行
        with open(file,'w') as d:
            d.write(''.join(contents[2:]))#删除每个txt文件的头2行

def findI(files):#查找文件中是否还包含文件头
    str = "Selection"# ——————————————————————————————————————————————————————————————————————————这里是需要查找的文件头是什么
    files = os.listdir(files)#创建路径下所有文件的列表
    files.sort()#初始化排序文件
    files.sort(key = lambda x: float(x[:-4]))#按照数字大小排序
    for file in files:
        file = filepath + '/'+ file
        with open(file, 'r', encoding = 'utf-8') as d:
            contents = d.readlines()
            firstline = contents[0]
            flag = str in firstline
            if flag is True:
                return flag
                break

filepath = r'E:\2022.6.10.650Kshuangqiu\500直方图'

files = os.listdir(filepath)
print(len(files))
sumd = pd.DataFrame()

if findI(filepath) is True:
    delete_top(filepath)
else:
    pass


for file in files:
    file = filepath + '/'+ file
    df = pd.read_table(file,sep='\s+',names=['Chunk', 'Number'])
    #print(df)
    time.sleep(0.1)
    sumd = sumd.append(df['Number'])
sumd_zhuanzhi = pd.DataFrame(sumd.values.T,index = sumd.columns,columns=sumd.index)
sumd_zhuanzhi['sum'] = sumd_zhuanzhi.sum(axis=1)
print(sumd_zhuanzhi)
sumd_zhuanzhi.to_csv(filepath+ '/' +'转制'+'.csv')




elapsed = (time.time() - start)
print("消耗时间为：")
print(elapsed)
print("s")