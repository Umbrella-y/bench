#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
import time
import os
import pandas as pd
import numpy as np
import math as math

start = time.clock()
filepath = 'D:/py_venv/venv1/file for process/'
filename = '1200K.txt'
filen = filepath + filename
print("数据名")
print("\t")
print(filen)
data = np.loadtxt(filen)
df = pd.DataFrame(data, columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'])
print(df)
print(df.loc[0])


# In[2]:


print("模拟体系大小为：")
diameter = float(input())
radium = diameter/2
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


# In[3]:


print("设置计算截断距离:(推荐值为10，！！最小截断半径3.61)")
cutoff = float(input())
print("总原子数：")
total = int(input())
print(total)
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
print ("确认请按任意键：")
con = input()


# In[4]:


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

print(kjm)
# print(kj[0].shape)
# print(kj[0][0, 0, 0])
print("建立网格矩阵，用于存储数据")
kj = np.zeros((nx-1,ny-1,nz-1,total))
print(kj.shape)
print(type(kj),kj)


# In[5]:


print("创建数个个随划分变化的变量字典：")
geshu = int(nx)
dv = globals()
my_dict = dict()
# dfx = pd.DataFrame()
# dfy = pd.DataFrame()
# dfz = pd.DataFrame()
for i in range(0,geshu-1):
    for j in range(0,geshu-1):
        for k in range(0,geshu-1):
            dv['c' + str(i)] = float(kjm[0][i,j,k])
            my_dict['c' + str(i)+str(j)+str(k)] = list()
print(my_dict)
print("字典创建完成————————————————————————")

print("创建判定条件：")
for i in range(0,geshu):
    dv['a'+str(i)] = float(kjm[0][i,i,i])
    print("划分：")
    print('a'+str(i))
print("判定条件创建完成————————————————————")

print(a0)
print("未显示全部")

# for i in df.index:
#     for t in range(0,geshu)
#         if df.loc(i,[x]) >= float('c' + str(t)) and df.loc(i,[x]) <= float('c' + str(t+1)):
#             if df.loc(i,[y]) >= float('c' + str(t)) and df.loc(i,[y]) <= float('c' + str(t+1)):
#                 if df.loc(i,[z]) >= float('c' + str(t)) and df.loc(i,[z]) <= float('c' + str(t+1)):

#         else：
#         continue


# In[6]:


# data = np.loadtxt(r'/home/aistudio/work/600K.txt')
# df = pd.DataFrame(data, columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'])
#运行到此之前一定要重新运行前述代码，清空之前的内存里的字典，不要让其影响后续的工作！！！！！！————————————————————————————
print("确保之前的字典已经清空，开始遍历x轴")
for d in df.index:
    #print("遍历到第：")
    #print(d)
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
    for j in range(0,geshu-1):
        for k in range(0,geshu-1):
            print(len(my_dict['c'+str(i)+str(j)+str(k)]),end = '个原子，对应块：')
            print('c'+str(i)+str(j)+str(k))
            allatom = allatom + len(my_dict['c'+str(i)+str(j)+str(k)])

print("请确认！！！————总原子数为：")
print(allatom)


# for i in range(0,geshu-1):
#     print(len(my_dict['c'+str(i)+str(0)+str(0)]))
    #print(len(my_dict['c100']))
#print(my_dict['c000'])


# In[7]:


#将上一步生成的字典文件中的列表转变为数据库格式便于读写
# data = np.loadtxt(r'/home/aistudio/work/600K.txt')
# df = pd.DataFrame(data, columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'])
# my_dict['c'+str(i)+str(j)+str(k)].append(list(df.loc[d]))
ok_data = globals()
for i in range(0,geshu-1):
    for j in range(0,geshu-1):
        for k in range(0,geshu-1):
           data3 = my_dict['c'+str(i)+str(j)+str(k)]
           
           ok_data['c'+str(i)+str(j)+str(k)] = pd.DataFrame(data3,columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy']) 
           print(ok_data['c'+str(i)+str(j)+str(k)])

#print(ok_data)
print("所有的列表格式文件均转化成了对应的数据库文件，并以ok_data，c000的格式命名（以维度为准）")
def progress_bar():
  for i in range(1, 101):
    print("\r", end="")
    print("Progress: {}%: ".format(i), "▋" * (i // 2), end="")
    sys.stdout.flush()
    time.sleep(0.01)
 
if __name__ == '__main__':
  progress_bar()

# In[ ]:





# In[8]:


# 开始查找原子————————————
#两套输入方案，一套是点对点查找，一套是完全遍历
print("请输入待查询ID，或输入a进行全体遍历（输入0会导致程序崩溃，请勿操作）")

input_atom_id = input()
while input_atom_id not in ['a']:
    input_atom_id = int(input_atom_id)#！！！！！！！！！！！！！！！！！这个东西不要动！！！！！！！！！！！！！！！！！！！动了就错
    print("变量格式转换完成")
    break

##print(type(input_atom_id))
#print(df['id'])
####if input_atom_id is not in df.loc['id']:

    
# df_juli = pd.DataFrame(columns=['id', 'type', 'x', 'y', 'z','Coordination Numbers','Potential Energy','Kinetic Energy'])
# df_juli['kong']= ''

# for i in range(0,total):
#     df_juli.loc[i,'kong'] = i
#print(df)
#####if input_atom_id not in ['a']:

if input_atom_id in df.loc[:,'id']:
    print(input_atom_id in df['id'])
    satom_id = df.loc[df['id'] == input_atom_id].index

    #print(type(satom_id),type(df.loc[df['id'] == input_atom_id].index))
    #print(satom_id)
    #print(df.loc[satom_id])
    for i in range(0,geshu-1):#对各个轴的数据进行划分
        x1= dv['a'+str(i)]
        x2= dv['a'+str(i+1)]
        #print(type(df.loc[satom_id,'x'] >= x2))
        #print(df.loc[satom_id,'x'])
        if (df.loc[satom_id,'x'].values[0] >= x2) | (df.loc[satom_id,'x'].values[0] <x1):
            #print("TRUE1")
            continue
        else:
            for j in range(0,geshu-1):
                y1= dv['a'+str(j)]
                y2= dv['a'+str(j+1)]
                if (df.loc[satom_id,'y'].values[0] >= y2) | (df.loc[satom_id,'y'].values[0] <y1):
                    #print("TRUE2")
                    continue
                else:
                    for k in range(0,geshu-1):
                        z1= dv['a'+str(k)]
                        z2= dv['a'+str(k+1)] 
                        if (df.loc[satom_id,'z'].values[0] >= z2) | (df.loc[satom_id,'z'].values[0] <z1):
                            #print("TRUE3")
                            continue
                        else:
                            print("待查询id为：")
                            print(input_atom_id)
                            print("查询到对应的id所在的格子为：")
                            print('c'+str(i)+str(j)+str(k))
                            #创建距离数据库
                            df_juli= ok_data['c'+str(i)+str(j)+str(k)]#单个数据库的编号
if __name__ == '__main__':
  progress_bar()        


if input_atom_id in ['a']:
    print("进行全体遍历！！————————————")
    df.reset_index(drop=True)
    for satom_id in df.index:

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
                                print("待查询id为：")
                                print(satom_id)
                                print("查询到对应的id所在的格子为：")
                                print('c'+str(i)+str(j)+str(k))
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
                                print('d' + str(satom_id))
if __name__ == '__main__':
  progress_bar()



# In[9]:


#建立原子分块库完成，开始计算距离——————————
juli = pd.DataFrame(columns=['id','x','y','z','dis'])

if input_atom_id in df['id']:
    satom_id = df.loc[df['id'] == input_atom_id].index
    for l in df_juli.index:
        juli.loc[l,'id'] = df_juli.loc[l,'id']
        juli.loc[l,'x']  = df_juli.loc[l,'x']
        juli.loc[l,'y']  = df_juli.loc[l,'y']
        juli.loc[l,'z']  = df_juli.loc[l,'z']
        juli.loc[l,'dis'] = math.sqrt((df.loc[satom_id,'x']-df_juli.loc[l,'x']) ** 2 + (df.loc[satom_id,'y']-df_juli.loc[l,'y']) ** 2 + (df.loc[satom_id,'z']-df_juli.loc[l,'z']) ** 2)

print("单原子距离数据库计算完成————————")
print(juli)

print(df[325:330])
if __name__ == '__main__':
  progress_bar()

# In[10]:

#print(dv)

if input_atom_id in ['a']:
    dv['d' + str(satom_id)].reset_index(drop=True)
    for satom_id in df.index:
        print("_____________________________________")
        if 'd' + str(satom_id) in dv :
            dv['d' + str(satom_id)]['dis'] = ''
            for l in dv['d' + str(satom_id)].index:
                #print(dv['d' + str(satom_id)].loc[l,'x'])
                print(l)
                dv['d' + str(satom_id)].loc[l,'dis'] = math.sqrt((df.loc[satom_id,'x']-dv['d' + str(satom_id)].loc[l,'x']) ** 2 + (df.loc[satom_id,'y']- dv['d' + str(satom_id)].loc[l,'y']) ** 2 + (df.loc[satom_id,'z']-dv['d' + str(satom_id)].loc[l,'z']) ** 2)

    #print('d' + str(satom_id))
#print(df.loc[510])
#print(d510)
if __name__ == '__main__':
  progress_bar()

# In[11]:


#平均处理，若需要则进行，不需要就不要用
if input_atom_id in ['a']:
    binsize = int(radium/0.2)
    jieguo = pd.DataFrame(columns=[i for i in range(0,binsize-1)])
    for r in range(0,total):
        jieguo.loc[r,'sid'] = r
    step = 0 
    for satom_id in df.index:
        if 'd' + str(satom_id) in dv :
            dv['d' + str(satom_id)].reset_index(drop=True)
            step = 1 
            for l in dv['d' + str(satom_id)].index:
                print(l)
                a = 0 
                b = 0.2
                for i in range(0,binsize-1):
                    
                    if (dv['d' + str(satom_id)].loc[l,'dis'] >a) and (dv['d' + str(satom_id)].loc[l,'dis'] <=b):
                        if pd.isna(jieguo.loc[satom_id, i]) is True:
                            jieguo.loc[satom_id, i] = 0
                        else:
                            #print(type(jieguo.loc[satom_id, i]))
                            jieguo.loc[satom_id, i] += 1

                        a +=0.2
                        b +=0.2
                    else:
                        a+=0.2
                        b+=0.2
                        continue
            print(step)
            step +=1
    jieguo = jieguo.fillna(0)
    jieguo.loc["列总和"] =jieguo.apply(lambda x:x.sum())
    jieguo1 = jieguo.drop('sid',1)
    #print(jieguo1)
    jieguo1.to_csv(filen + '{}.csv'.format(filename))
if __name__ == '__main__':
  progress_bar()        


# In[12]:

if input_atom_id in ['a']:
    import matplotlib.pyplot as plt

    x = np.linspace(0,radium,num = int(radium/0.2)-1)
    x = x[:, np.newaxis]
    y = jieguo1.loc["列总和"]
    y = y[:, np.newaxis]
    elapsed = (time.clock() - start)
    print("消耗时间为：")
    print(elapsed)

    plt.plot(x,y)
    #plt.plot(x)
    plt.show()
    print("仅供预览，作图请用绘图软件")
    if __name__ == '__main__':
        progress_bar()
    print("运行结束")