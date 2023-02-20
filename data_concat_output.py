import os
import time
import numpy as np
import pandas as pd

filepath = r'E:\双球模拟数据整合\2022.9.16.2ball\2022.9.19.600K\calculated\文本数据'
df= pd.DataFrame()
files= os.listdir(filepath)
for file in files:
    file = filepath + '/' + file
    bash = pd.read_csv(file,sep= ' ',names = ['sintering','step'])#skiprows=9
    bash.sort_values(by=['step'],ascending=True,inplace=True)
   
    bash = bash.reset_index(drop=True)
    print(bash)
    df = pd.concat([df,bash],axis=1,ignore_index = True)
    print(df)
    #time.sleep(1)
df.to_csv(filepath + '/' + 'huizong.csv',index = False)
