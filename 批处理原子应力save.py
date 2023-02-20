import pandas as pd
import numpy as np
import os
import math
import matplotlib.pyplot as plt
from time import sleep  
from matplotlib.animation import FuncAnimation
import imageio
import re

shuchupath= r'E:\30nm实验数据汇总\2022.11.10.900K-1250Kstress\1500/'
filesave = shuchupath + 'bash/' #输出表格
tusave = shuchupath + 'su/' #输出
qusave = shuchupath + 'qu/'#输出
zosave = shuchupath + 'zo/'#输出
filename = r'E:\30nm实验数据汇总\2022.11.10.900K-1250Kstress\1500\stress/'#文件输入
zhuansave = shuchupath + 'zhuan/'#输出

    #获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
def makefile(path):
    if not os.path.exists(path):
        os.makedirs(path)
makefile(filesave)
makefile(tusave)
makefile(qusave)
makefile(zosave)
makefile(filename)
makefile(zhuansave)
print(filename)

def dantu(xi,lablehigh,xlo,xhi,path):
    xilen = xi.shape[1]
    for i in range(0,xilen):
        plt.cla()
        x = xi.index
        y = xi.iloc[:,i]
        plt.xlim(xlo, xhi)
        plt.ylim(-lablehigh, lablehigh)
        plt.plot(x,y)
        #plt.show()
        plt.savefig(path + '{}.jpg'.format(i))

def batch_rename(dir_path, suffix):
    files = os.listdir(dir_path)
    for i, file in enumerate(files):
        old_name = os.path.join(dir_path, file)
        new_name = os.path.join(dir_path, file.split(".")[-1] + suffix)
         #file.split(".")[-1]
        os.rename(old_name, new_name)

def zhuanzifu(str):
    a = re.findall(r'\d+',str) #在字符串中找到正则表达式所匹配的所有数字，a是一个list
    str =a[-1]
    print (str)
    return str

#将列表中的数据按照列进行平均并输出
def liepingjuncsv(df,savepath,name):
    lieshu = df.shape[1]
    lie = int(lieshu/10)
    print(lie)
    pingjunx = pd.DataFrame()
    for i in range(0,lie,1):
        xiajie = 10*i
        shangjie = 10*(i+1)
        pingjunx[i] = df.iloc[:,xiajie:shangjie].sum(axis=1)
        pingjunx[i] = pingjunx[i].div(10)
        pingjunx1 = '经过列平均'
        pingjunx.to_csv(savepath + name +'{}.csv'.format(pingjunx1))
    return pingjunx  

def liepingjuncsvrr(df,savepath,name):
    lieshu = df.shape[1]
    lie = int(lieshu/10)
    print(lie)
    pingjunx = pd.DataFrame()
    for i in range(0,lie,1):
        xiajie = 10*i
        shangjie = 10*(i+1)
        pingjunx[i] = df.iloc[:,xiajie:shangjie].sum(axis=1)
        pingjunx[i] = pingjunx[i].div(10)
        pingjunx1 = '经过列平均rr'
        pingjunx.to_csv(savepath + name +'{}.csv'.format(pingjunx1))
    return pingjunx  

def liepingjuncsv100ping(df,savepath):
    lieshu = df.shape[1]
    lie = int(lieshu/100)
    print(lie)
    pingjunx100 = pd.DataFrame()
    for i in range(0,lie,1):
        xiajie = 100*i
        shangjie = 100*(i+1)
        pingjunx100[i] = df.iloc[:,xiajie:shangjie].sum(axis=1)
        pingjunx100[i] = pingjunx100[i].div(100)
        pingjunx1001 = '经过列平均100后的'
        pingjunx100.to_csv(savepath + '{}.csv'.format(pingjunx1001))
    return pingjunx100  

# 删除文件夹下的文件&&保留但清空子文件夹
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
#batch_rename(filename, '.txt')
files = os.listdir(filename)#文件名是来自最初的文件夹里面的所有文件的顺序
su = pd.DataFrame()#切向力数据
qu = pd.DataFrame()#法向力数据

#files = os.walk(filename)
for file in files:
    files.sort()#初始化排序文件
    files.sort(key = lambda x: float(x[16:]))#按照数字大小排序

    i = '123'
    name = str(file)
    name = filename + name
    print(name)
    df = pd.read_table(name,sep='\s+',names=['1','2','3','4','5','6','7','8','9','10','11','12'])
    data  = pd.DataFrame(df)
    #print(data)
    print(str(file))
    file = zhuanzifu(str(file))
    su.loc[:,file] = df['5']
    qu.loc[:,file] = df['9']
    

print(su)
print(qu)
pingjun1 = pd.DataFrame()
pingjun2 = pd.DataFrame()

for i in range(0,13,1):
    xiajie = 10*i
    shangjie = 10*(i+1)
    pingjun1[i] = su.iloc[:,xiajie:shangjie].sum(axis=1)
    pingjun1[i] = pingjun1[i].div(10)

#print (pingjun1)
pingjunname1 = 'pingjunname1'
pingjun1.to_csv(filesave + '{}.csv'.format(pingjunname1))

for i in range(0,13,1):
    xiajie = 10*i
    shangjie = 10*(i+1)
    pingjun2[i] = qu.iloc[:,xiajie:shangjie].sum(axis=1)
    pingjun2[i] = pingjun2[i].div(10)

#print (pingjun2)
pingjunname2 = 'pingjunname2'
pingjun2.to_csv(filesave + '{}.csv'.format(pingjunname2))
mingzi1 = 1
su.to_csv(filesave + 'RR.csv'.format(mingzi1))
mingzi2 = 2
qu.to_csv(filesave + 'PhiPhi.csv'.format(mingzi2))
#__________________________________________________________________________________
sulen = su.shape[1]
qulen = qu.shape[1]

lablehigh = 2.5
xlo = 0
xhi = 132


su_zhuanzhi = pd.DataFrame(su.values.T,index = su.columns,columns=su.index)
qu_zhuanzhi = pd.DataFrame(qu.values.T,index = qu.columns,columns=qu.index)
#su_zhuanzhi = su_zhuanzhi.drop(index = 1,axis=1)
del_file(zhuansave)
#dantu(su_zhuanzhi,lablehigh,xlo,xhi,zhuansave)
zhuanzhiname = '未经过平均的转制'
su_zhuanzhi.to_csv(filesave + 'RR{}.csv'.format(zhuanzhiname))
qu_zhuanzhi.to_csv(filesave + '切向'+'PP{}.csv'.format(zhuanzhiname))

qupingjunzhuanzhi = liepingjuncsv(qu_zhuanzhi,filesave,'zz')#得到平均后的转制矩阵
supingjunzhuanzhi = liepingjuncsvrr(su_zhuanzhi,filesave,'zz')

nozhuanzhiname = '没有平均过没有转置'
qupingjunnozhuanzhi = pd.DataFrame(qupingjunzhuanzhi.values.T,index = qupingjunzhuanzhi.columns,columns=qupingjunzhuanzhi.index)
supingjunnozhuanzhi = pd.DataFrame(supingjunzhuanzhi.values.T,index = supingjunzhuanzhi.columns,columns=supingjunzhuanzhi.index)

qupingjunnozz = qupingjunnozhuanzhi.to_csv(filesave +'nozhuanzhi'+ 'PP{}.csv'.format(nozhuanzhiname))
supingjunnozz = supingjunnozhuanzhi.to_csv(filesave + 'nozhuanzhi'+'RR{}.csv'.format(nozhuanzhiname))
# qupingjun1 = liepingjuncsv(qu,filesave,'nozz')#得到平均后的矩阵
# supingjun2 = liepingjuncsvrr(su,filesave,'nozz')

#pingjunzhuanzhi = liepingjuncsv(su_zhuanzhi,filesave)#得到平均后的转制矩阵
#liepingjuncsv(qupingjunzhuanzhi,filesave)
pingjunzhuanzhi100 = liepingjuncsv100ping(su_zhuanzhi,filesave)
#dantu(pingjunzhuanzhi,lablehigh,xlo,xhi,zhuansave)


#——————————————————————————————————————————————————————————————————————————————————5hang
del_file(tusave)
for i in range(0,sulen):
    plt.cla()
    x = su.index
    y = su.iloc[:,i]
    plt.xlim(0, 1700)
    plt.ylim(-lablehigh, lablehigh)
    plt.plot(x,y)
    #plt.show()
    plt.savefig(tusave + '{}.jpg'.format(i))


images = []
filetus = os.listdir(tusave)
filetus.sort(key=lambda x:int(x[:-4]))
print(filetus)
for filetu in filetus:
    name = str(filetu)
    name = tusave + name
    images.append(imageio.imread(name))
imageio.mimsave(tusave + 'su1.gif', images,duration=0.05)
#_____________________________________________________________________9hang
del_file(qusave)
for i in range(0,qulen):
    plt.cla()
    x = qu.index
    y = qu.iloc[:,i]
    plt.xlim(0, 1700)
    plt.ylim(-lablehigh, lablehigh)
    plt.plot(x,y)
    #plt.show()
    plt.savefig(qusave + '{}.jpg'.format(i))


images1 = []
filetus = os.listdir(qusave)
filetus.sort(key=lambda x:int(x[:-4]))
print(filetus)
for filetu in filetus:
    name = str(filetu)
    name = qusave + name
    images1.append(imageio.imread(name))
imageio.mimsave(qusave + 'qu1.gif', images1,duration=0.05)

#_____________________________________________________________________hebing
del_file(zosave)
for i in range(0,qulen):
    plt.cla()
    x = qu.index
    y1 = su.iloc[:,i]
    y2 = qu.iloc[:,i]
    plt.xlim(0, 1700)
    plt.ylim(-lablehigh, lablehigh)
    plt.title('Step = '+'{}'.format(i))
    plt.plot(x, y1, color='green', label='R')
    plt.plot(x, y2, color='red', label='Phi',alpha = 0.7)
    plt.legend()
    #plt.show()
    plt.savefig(zosave + '{}.jpg'.format(i))


images3 = []
filetus = os.listdir(zosave)
filetus.sort(key=lambda x:int(x[:-4]))
print(filetus)
for filetu in filetus:
    name = str(filetu)
    name = zosave + name
    images3.append(imageio.imread(name))
imageio.mimsave(zosave + 'zo1.gif', images3,duration=0.05)