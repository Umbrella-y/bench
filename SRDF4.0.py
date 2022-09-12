#!/usr/bin/env python
# coding: utf-8
#代码还存在小bug——————————————————————————————————————by Charlo Song
# 对于表面原子的RDF进行计算的程序，SRDF2.01
# 计算不采用传统的方式
# #——————————————————————————————————————#
# 1、计算前请在Ovito中按照'id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'的排列顺序导出dump文件并重命名为txt格式
# 2、文件编号按照*.txt的格式进行命名和排布
# 3、进入exe文件后输入体系直径大小，单位为埃
# 4、输入截断半径，单位为埃。
# 5、输入总原子数（待计算体系的原子总数的取整值，比输入原子数目多即可）
# 6、等待计算结果，结束。
# 8、结束后数据请自行除以密度并进行归一化处理，输出图像仅供确认和预览！！！！！！！

# default设置
# 60
# binsize0.2
# cutoff7.2

# 不然就会算错！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
# number随意

#——————————————————————————————————————#
from re import I
import sys
import time
import os
import pandas as pd
import numpy as np
import math as math
import warnings
warnings.filterwarnings("ignore")

print("这是针对球状纳米级别颗粒的表面原子进行RDF计算的程序，表面RDF命名为Surface Radial Distribution Function（SRDF）")
print("请使用Ovito导出的dump文件进行计算。")
print("请确保您的所有的原子信息是按照要求进行排布的")
print("'id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'")
print("不能多项，不能缺项，务必注意！！！！！！！！！！！")
print("###————————SRDF-3.0版本——————###")
print("按照要求，输入文件夹路径，输入输出文件夹路径，模拟体系大小，绘图binsize大小，截断距离，总原子数等数据！！！！！！！！！")
print("默认的设置为！（针对于铜元素！）")
print("输入路径：默认\n输出路径：默认\n模拟体系大小：默认\n绘图binsize大小：0.2或0.1\n截断距离：7.2（为了算表面）\总原子数：默认")
print("________________________________________________________________________________________________________________")
print("P.S.并行的还没有弄出来，想要算的快一点那就多开几个exe吧哈哈")
print("确认请按任意键")
#stra = input()
start = time.time()

#输入的所有的信息现在放在了文件头一次性的全部输入进来
print("请输入文件路径名：")
filepath = str(input())#——————————————————————————————————————————————————————————————————去掉了I/O
print(filepath)

print("请输入——保存——文件路径名：")
#filepath = str(input())#——————————————————————————————————————————————————————————————————去掉了I/O
filesave = str(input())
print(filesave)

# print("请输入文件名：（带后缀）")
# #filename = str(input())#——————————————————————————————————————————————————————————————————去掉了I/O#################################这里肯定是要改的，改为遍历其下的所有的文件
# filename = '1.txt'


print("模拟体系大小为：")
diameter = float(input())#——————————————————————————————————————————————————————————————————去掉了I/O#################################这里肯定是要改的，改为遍历其下的所有的文件
radium = diameter/2
print(diameter)

print("请设置绘图用最小binsize大小：")#——————————————————————————————————————————————————————————————————去掉了I/O#################################这里肯定是要改的，改为遍历其下的所有的文件
tusize = float(input())
print(tusize)

print("设置计算截断距离:(推荐值为7.2！！为了算表面！！最小截断半径3.61)")#——————————————————————————————————————————————————————————————————去掉了I/O#################################这里肯定是要改的，改为遍历其下的所有的文件
cutoff = float(input())
print(cutoff)

print("设置总原子数：")#——————————————————————————————————————————————————————————————————去掉了I/O#################################这里肯定是要改的，改为遍历其下的所有的文件
total = int(input())
print(total)

print("设置归一距离（默认为10）：")#——————————————————————————————————————————————————————————————————去掉了I/O#################################这里肯定是要改的，改为遍历其下的所有的文件
guiyidian = float(input())
print(guiyidian)
guiyidian = guiyidian/0.2
guiyidian = int(guiyidian)
#filen = filepath + '/' + filename
#filepath = 'D:/py_venv/venv1/file for process/chuli2/'
#filename = '600K.txt'
#filen = filepath + filename
#print("数据名")
#print("\t")
#print(filen)
def add(a,b,c):
    return a + b + c

def sub(a,b):
    return a/b

def mag(a,b):
    return a*b

def delete_top(files):#删除每个txt文件的头9行
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
            d.write(''.join(contents[9:]))#删除每个txt文件的头9行

def findI(files):#查找文件中是否还包含文件头
    str = "ITEM:"
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


def progress_bar(i,istep):#进度条的实现方式，用int型作为输入的变量作为计数
    print("\r", end="")
    print("Progress: {}:{}".format(i+1,istep), "▋" * (i // 100), end="")
    sys.stdout.flush()
    #time.sleep(0.001)




if findI(filepath) is True:
    delete_top(filepath)
else:
    pass

def SRDF(filen,filesave,diameter,tusize,cutoff,total,file,guiyidian):
    data = np.loadtxt(filen)
    df = pd.DataFrame(data, columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'])
    print(df)


    print("半径为：")
    print(radium)

    xmax = df.loc[:,"x"].max()
    xmin = df.loc[:,"x"].min()
    print("x最大最小值：————————————————————")
    print(xmax)
    print(xmin)
    ymax = df.loc[:,"y"].max()
    ymin = df.loc[:,"y"].min()
    print("y最大最小值：————————————————————")
    print(ymax)
    print(ymin)
    zmax = df.loc[:,"z"].max()
    zmin = df.loc[:,"z"].min()
    print("z最大最小值：————————————————————")
    print(zmax)
    print(zmin)
    print(("截断距离为："))
    print(cutoff)
    print("请再次确认体系直径、半径、截断距离等参数：")
    print("模拟体系大小为：")
    print(diameter)
    print("半径为：")
    print(radium)
    print(("截断距离为："))
    print(cutoff)
    print("总原子数为：")
    print(total)

    time.sleep(0.1)

    #——————————————————————————————————————————————————————————————————————————————————————划分网格的阶段————————————————————————————————————————————————————————————————————————
    size = 3.61 #这是铜原子的晶格常数，最小划分也仅此
    nx = int( diameter/cutoff)
    ny = int( diameter/cutoff)
    nz = int( diameter/cutoff)
    print("划分后的格子数目：")
    print(nx,ny,nz)

    x = np.linspace(-radium,radium,nx)
    y = np.linspace(-radium,radium,ny)
    z = np.linspace(-radium,radium,nz)
    kjm = np.meshgrid(x,y,z)

    #print(kjm)
    # print(kj[0].shape)
    # print(kj[0][0, 0, 0])
    print("建立网格矩阵，用于存储数据")
    kj = np.zeros((nx-1,ny-1,nz-1,total))
    #print(kj.shape)
    #print(type(kj),kj)

    print("创建数个个随划分变化的变量字典：")
    geshu = int(nx)
    dv = globals()
    my_dict = dict()
    # dfx = pd.DataFrame()
    # dfy = pd.DataFrame()
    # dfz = pd.DataFrame()
    for i in range(0,geshu-1):
        progress_bar(i,geshu-1)
        for j in range(0,geshu-1):
            for k in range(0,geshu-1):
                dv['c' + str(i)] = float(kjm[0][i,j,k])
                my_dict['c' + str(i)+str(j)+str(k)] = list()
    print("字典创建完成————————————————————————")

    print("创建判定条件：")
    for i in range(0,geshu):
        progress_bar(i,geshu)
        dv['a'+str(i)] = float(kjm[0][i,i,i])
        # print("划分：")
        # print('a'+str(i))
    print("判定条件创建完成————————————————————")

    print("确保之前的字典已经清空，开始遍历x轴")
    for d in df.index:
        for i in range(0,geshu-1):#对各个轴的数据进行划分
            x1= dv['a'+str(i)]
            x2= dv['a'+str(i+1)]
            if df.loc[d,'x'] >= x2 or df.loc[d,'x'] <x1:
                continue
            else:
                for j in range(0,geshu-1):
                    y1= dv['a'+str(j)]
                    y2= dv['a'+str(j+1)]
                    if df.loc[d,'y'] >= y2 or df.loc[d,'y'] <y1:
                        continue
                    else:
                        for k in range(0,geshu-1):
                            z1= dv['a'+str(k)]
                            z2= dv['a'+str(k+1)] 
                            if df.loc[d,'z'] >= z2 or df.loc[d,'z'] <z1:
                                continue
                            else:
                                my_dict['c'+str(i)+str(j)+str(k)].append(list(df.loc[d]))


                    #print(my_dict['c'+str(i)+str(0)+str(0)])
    print("整体遍历完成")
    allatom = 0 
    for i in range(0,geshu-1):
        progress_bar(i,geshu-1)
        for j in range(0,geshu-1):
            for k in range(0,geshu-1):

                #print(len(my_dict['c'+str(i)+str(j)+str(k)]),end = '个原子，对应块：')
                #print('c'+str(i)+str(j)+str(k))
                allatom = allatom + len(my_dict['c'+str(i)+str(j)+str(k)])

    print("请确认！！！————总原子数为：")
    print(allatom)
    ok_data = globals()
    for i in range(0,geshu-1):
        progress_bar(i,geshu-1)
        for j in range(0,geshu-1):
            for k in range(0,geshu-1):
                data3 = my_dict['c'+str(i)+str(j)+str(k)]
            
                ok_data['c'+str(i)+str(j)+str(k)] = pd.DataFrame(data3,columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy']) 
    
    print("所有的列表格式文件均转化成了对应的数据库文件，并以ok_data，c000的格式命名（以维度为准）")
    #_____________________________________________________________________________#去除单独检索的模块改为全体遍历
    print("进行全体遍历！！————————————")
    df.reset_index(drop=True)
    for satom_id in df.index:
        progress_bar(satom_id,df.index.values[-1])
        for i in range(0,geshu-1):#对各个轴的数据进行划分
            
            x1= dv['a'+str(i)]
            x2= dv['a'+str(i+1)]
            #print(type(df.loc[satom_id,'x'] >= x2))
            #print(df.loc[satom_id,'x'])
            #_____________________________________________________________________________
            if (df.loc[satom_id,'x'] >= x2) | (df.loc[satom_id,'x'] <x1):
                #print("TRUE1")
                continue
            else:
                for j in range(0,geshu-1):
                    y1= dv['a'+str(j)]
                    y2= dv['a'+str(j+1)]
                    if (df.loc[satom_id,'y'] >= y2) | (df.loc[satom_id,'y'] <y1):
                        #print("TRUE2")
                        continue
                    else:
                        for k in range(0,geshu-1):
                            z1= dv['a'+str(k)]
                            z2= dv['a'+str(k+1)] 
                            if (df.loc[satom_id,'z'] >= z2) | (df.loc[satom_id,'z'] <z1):
                                #print("TRUE3")
                                continue
                            else:
                                # print("待查询id为：")
                                # print(satom_id)
                                # print("查询到对应的id所在的格子为：")
                                # print('c'+str(i)+str(j)+str(k))
                                #print(ok_data['c'+str(i)+str(j)+str(k)])
                                #创建原子分块数据库
                                dv['d' + str(satom_id)] = pd.DataFrame(columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'])
                                #——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
                                if i in [0,geshu-1] or  j in [0,geshu-1] or k in [0,geshu-1]:
                                    dv['d' + str(satom_id)] = ok_data['c'+str(i)+str(j)+str(k)]
                                else:
                                #——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
                                    for x in range(i-1,i+1):
                                        for y in range(j-1,j+1):
                                            for z in range(k-1,k+1):
                                                dv['d' + str(satom_id)] = dv['d' + str(satom_id)].append(ok_data['c'+str(i)+str(j)+str(k)])

                                dv['d' + str(satom_id)] = dv['d' + str(satom_id)].reset_index(drop=True)
                                dv['d' + str(satom_id)] = dv['d' + str(satom_id)].drop_duplicates(subset=['id'],keep='first',inplace=False)
                                # print('d' + str(satom_id))

    juli = pd.DataFrame(columns=['id','x','y','z','dis'])
    print("开始对所有原子之间的距离进行计算！！！！！！！！！！！！！！！————————————")
    dv['d' + str(satom_id)].reset_index(drop=True)
    for satom_id in df.index:
        progress_bar(satom_id,df.index.values[-1])
        if 'd' + str(satom_id) in dv :
            dv['d' + str(satom_id)]['dis'] = ''
            for l in dv['d' + str(satom_id)].index:
                
                dv['d' + str(satom_id)].loc[l,'dis'] = math.sqrt((df.loc[satom_id,'x']-dv['d' + str(satom_id)].loc[l,'x']) ** 2 + (df.loc[satom_id,'y']- dv['d' + str(satom_id)].loc[l,'y']) ** 2 + (df.loc[satom_id,'z']-dv['d' + str(satom_id)].loc[l,'z']) ** 2)

    #平均处理，若需要则进行，不需要就不要用

    binsize = int(radium/tusize)
    jieguo = pd.DataFrame(columns=[i for i in range(0,binsize-1)])
    for r in range(0,total):
        jieguo.loc[r,'sid'] = r
    step = 0 
    print("开始对所有原子的SRDF值进行平均处理！！！！！！！！！！！！！！！————————————")
    for satom_id in df.index:
        progress_bar(satom_id,df.index.values[-1])
        if 'd' + str(satom_id) in dv :
            dv['d' + str(satom_id)].reset_index(drop=True)
            step = 1 
            for l in dv['d' + str(satom_id)].index:
                #print(l)
                a = 0 
                b = tusize
                for i in range(0,binsize-1):
                    
                    if (dv['d' + str(satom_id)].loc[l,'dis'] >a) and (dv['d' + str(satom_id)].loc[l,'dis'] <=b):
                        if pd.isna(jieguo.loc[satom_id, i]) is True:
                            jieguo.loc[satom_id, i] = 0
                        else:
                            #print(type(jieguo.loc[satom_id, i]))
                            jieguo.loc[satom_id, i] += 0.1*i

                        a +=tusize
                        b +=tusize
                    else:
                        a+=tusize
                        b+=tusize
                        continue
            step +=1
    jieguo = jieguo.fillna(0)
    jieguo.loc["liehe"] =jieguo.apply(lambda x:x.sum())
    #这里插入对归一点的使用，借此可以直接得到峰值，无需重复计算
    jieguo = jieguo.append(pd.Series(name = 'guiyizhi'))
    jieguo['max'] = jieguo.loc[:,[guiyidian-3,guiyidian-2,guiyidian-1,guiyidian,guiyidian+1,guiyidian+2,guiyidian+3]].max(axis=1)
    guiyishuzhi = jieguo.loc['liehe','max']
    liehehang = total
    #guiyishuzhi = float(jieguo.iloc[liehehang,guiyidian])#归一点需要寻找到峰值之后再进行归一
    jieguo.loc['guiyizhi'] = jieguo.loc['guiyizhi'].fillna(guiyishuzhi)
    jieguo.loc["average as 1"] = jieguo.apply(lambda x: sub(x.loc["liehe"],x.loc["guiyizhi"]))
    #至此，输出所有经过归一的数据，并可借此直接得到峰值
    jieguo1 = jieguo.drop('sid',1)
    #print(jieguo1)
    jieguo1.to_csv(filesave +'/'+ '{}.csv'.format(file))


files = os.listdir(filepath)#创建路径下所有文件的列表
files.sort()#初始化排序文件
files.sort(key = lambda x: float(x[:-4]))#按照数字大小排序
for file in files:
    filen = filepath + '/' + file
    SRDF(filen,filesave,diameter,tusize,cutoff,total,file,guiyidian)


elapsed = (time.time() - start)
print("消耗时间为：")
print(elapsed)
print("s")