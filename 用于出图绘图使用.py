from hashlib import new
from pdb import line_prefix
from tkinter.ttk import LabeledScale
import pandas as pd
import numpy as np
import os
import math
import matplotlib.pyplot as plt
from time import sleep  
from matplotlib.animation import FuncAnimation
import imageio
import shutil
import re
from scipy.interpolate import splprep,splev
from scipy.signal import savgol_filter
filepath = r'E:\2022.分层熔化论文\30nmAL直接IK的数据处理动图/'
filesave = r'E:\2022.分层熔化论文\30nmAL直接IK的数据处理动图/chutu/'
pinghua_filepath = r'E:\2022.分层熔化论文\30nmAL直接IK的数据处理动图\平滑出图1/'

def del_file(filepath):
    print("hello")
    listdir = os.listdir(filepath)  # 获取文件和子文件夹
    print(listdir)
    for dirname in listdir:
        dirname = filepath + "//" + dirname
        if os.path.isfile(dirname): # 是文件
            print(dirname)
            os.remove(dirname)      # 删除文件
        elif os.path.isdir(dirname):        # 是子文件夹
            print(dirname)
            dellist = os.listdir(dirname)
            for f in dellist:               # 遍历该子文件夹
                file_path = os.path.join(dirname, f)
                if os.path.isfile(file_path):       # 删除子文件夹下文件
                    os.remove(file_path)
                elif os.path.isdir(file_path):      # 强制删除子文件夹下的子文件夹
                    shutil.rmtree(file_path)

def chutu(qu,filesave):
    qulen = qu.shape[1]
    for i in range(0,qulen,1):
        plt.cla()
        x = qu.index
        y = qu.iloc[:,i]
        plt.xlim(0, 1600)
        plt.ylim(-3, 3)
        plt.plot(x,y)
        #plt.show()s
        plt.title('Step = '+'{}'.format(i))
        plt.savefig(filesave + '{}.jpg'.format(i))
    images3 = []
    filetus = os.listdir(filesave)
    filetus.sort(key=lambda x:int(x[:-4]))
    print(filetus)
    for filetu in filetus:
        name = str(filetu)
        name = filesave + name
        images3.append(imageio.imread(name))
    imageio.mimsave(filesave + '动图.gif', images3,duration=0.0166666)


def pinghuachutu(qu,filesave):
    qulen = qu.shape[1]
    for i in range(0,qulen,1):
        plt.cla()

        x = spline3(qu.index, qu.iloc[:,i],15000,4)[0]
        y = spline3(qu.index, qu.iloc[:,i],15000,4)[1]

        plt.xlim(0, 160)
        plt.ylim(-10, 10)
        plt.plot(x,y)
        plt.title('Step = '+'{}'.format(i))
        plt.savefig(filesave +'{}.jpg'.format(i))########################平滑后的结果
    images3 = []
    filetus = os.listdir(filesave)
    filetus.sort(key=lambda x:int(x[:-4]))
    print(filetus)
    for filetu in filetus:
        name = str(filetu)
        name = filesave + name
        images3.append(imageio.imread(name))
    imageio.mimsave(filesave + '平滑动图.gif', images3,duration=0.01)

def spline3(x, y, point, deg):##deg默认是3，point值表示的平滑曲线所使用的点的数量
    tck, u = splprep([x, y], k=deg, s=1) #曲线绘制方法2##——————————————deg的值从1到5，默认值为3，尽量避免使用偶数值其中S是平滑的权重！！！！！！！！！！！
    u = np.linspace(0, 1, num=point, endpoint=True) #显示范围比例
    spline = splev(u, tck)
    return spline[0], spline[1]


def savitzky_Golay(qu,filesave):
    qulen = qu.shape[1]
    for i in range(0,qulen,1):
        plt.cla()
        x = qu.index
        y = savgol_filter(qu.iloc[:,i],10,7)
        plt.figure(figsize=(10,2))
        plt.xlim(0, 160)
        plt.ylim(-1, 1)
        plt.plot(x,y)
        plt.title('Step = '+'{}'.format(i))
        
        plt.savefig(filesave +'{}.jpg'.format(i))########################平滑后的结果
    images3 = []
    filetus = os.listdir(filesave)
    filetus.sort(key=lambda x:int(x[:-4]))
    print(filetus)
    ####出GIF动图用的
    for filetu in filetus:
        name = str(filetu)
        name = filesave + name
        images3.append(imageio.imread(name))
    imageio.mimsave(filesave + '平滑动图.gif', images3,duration=0.015)

##___________________________________________________
filetruename = '1.csv'
filename = filepath + filetruename
df = pd.read_csv(filename)
#df.drop(df.columns[0], axis=1, inplace=True)#去掉第一行用的
##___________________________________________________
#df1 = pd.DataFrame(df.values.T,index = df.columns,columns=df.index)##转制所用的代码
#df1 = df1.astype('float64')
print(df)
##____________________________________________________


##____________________________________________________
del_file(filesave)
tupian = chutu(df,filesave)
##____________________________________________________
#del_file(pinghua_filepath)
#pinghuatupian = pinghuachutu(df,pinghua_filepath)
#savitzky_Golay_chutu = savitzky_Golay(df,pinghua_filepath)

