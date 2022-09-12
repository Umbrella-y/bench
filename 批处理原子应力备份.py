import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
filesave = 'C:/Users/Administrator/Desktop/2022.2.16.处理数据/'
filename = 'C:/Users/Administrator/Desktop/Bash/2022.3.9.14.44/'
print(filename)

def batch_rename(dir_path, suffix):
    files = os.listdir(dir_path)
    for i, file in enumerate(files):
        old_name = os.path.join(dir_path, file)
        new_name = os.path.join(dir_path, file.split(".")[-1] + suffix)
         #file.split(".")[-1]
        os.rename(old_name, new_name)

#batch_rename(filename, '.txt')
files = os.listdir(filename)#文件名是来自最初的文件夹里面的所有文件的顺序
su = pd.DataFrame()#切向力数据
qu = pd.DataFrame()#法向力数据

#files = os.walk(filename)
for file in files:
    #i=1
    name = str(file)
    name = filename + name
    print(name)
    df = pd.read_table(name,sep='\s+',names=['1','2','3','4','5','6','7','8','9','10','11','12'])
    data  = pd.DataFrame(df)
    print(data)
    su.loc[:,file] = df['5']
    qu.loc[:,file] = df['9']

print(su)
print(qu)
pingjun1 = pd.DataFrame()
pingjun2 = pd.DataFrame()

for i in range(0,25,1):
    xiajie = 10*i
    shangjie = 10*(i+1)
    pingjun1[i] = su.iloc[:,xiajie:shangjie].sum(axis=1)
    pingjun1[i] = pingjun1[i].div(10)

print (pingjun1)
pingjunname1 = 'pingjunname1'
pingjun1.to_csv(filesave + '{}.csv'.format(pingjunname1))

for i in range(0,25,1):
    xiajie = 10*i
    shangjie = 10*(i+1)
    pingjun2[i] = qu.iloc[:,xiajie:shangjie].sum(axis=1)
    pingjun2[i] = pingjun2[i].div(10)

#print (pingjun2)
pingjunname2 = 'pingjunname2'
pingjun2.to_csv(filesave + '{}.csv'.format(pingjunname2))
mingzi = 1
su.to_csv(filesave + '{}.csv'.format(mingzi))
mingzi = 2
qu.to_csv(filesave + '{}.csv'.format(mingzi))