import imp
import os
import time
from unittest.loader import VALID_MODULE_NAME 
import pandas as pd
import linecache
import string
import warnings
warnings.filterwarnings("ignore")#忽略所有的警告，继续执行，主要是为了屏蔽pd.append要换为pd.concat的警告
filepath = r'E:\2022.5.3.30nmxiaochuzhendong\1/'#使用的临时文件的bash的路径
#filename = r'C:\Users\Administrator\Desktop\Bash\重新计算的30nm的应力数据的chunk输出\2022.5.9/stress300-1350.txt'#使用的输入文件的路径和名称
name = 'stress300-300.txt'
filename = filepath + name

#设置导入的文件的帧数和对应的step数，这里是从1370000开始然后到1410000结束吗、，中间每个数据的间隔是100step
kaishi = 100
jieshu = 2000000
timestep = 100
chunkshumu = 20
tixidaxiao = 150

#outputfile = r'E:/2022.4.6.1410.stress.chunk/stress.txt'#使用的输出路径目前暂时未使用，需要输出不同的路径的时候可以去掉注释并使用
##——————————————————————————————————


##——————————————————————————————————
##计算指定的chunk区域的体积是多少最先
def chunk_stress(filename,kaishi,jieshu,timestep,chunkshumu,tixidaxiao):
    schunk_daxiao = tixidaxiao/chunkshumu
    volume_list = []
    for i in range(0,chunkshumu,1):
        shangjie = (i+1)*schunk_daxiao
        xiejie = (i)*schunk_daxiao
        pi = 3.1415926
        volume = 4*pi*(((shangjie)**3)-(xiejie**3))/3
        volume_list.append(volume)#得到的是一个列表，每次把输出的volume值输入到列表的末尾
    volume_list_data = pd.DataFrame(data =volume_list)#把刚刚得到的列表转化为dataframe
    print(volume_list)
    ##————————————————————————————————
    ##定义函数——名称为：去除文件头，比如文件的头3行或头9行比较麻烦处理，文件比较多，可以使用该函数
    ##输入为文件名称和，需要去掉的行数
    def delete_filehead(filename, hangshu):
        with open(filename, 'r', encoding = 'utf-8') as d:
                contents = d.readlines()#遍历所有的文件，除了代码输出文件以外的所有文件的每一行
        with open(filename,'w',encoding = 'utf-8') as file:
            file.write(''.join(contents[hangshu:]))
    ##定义函数——名称为：加，除，乘
    def add(a,b,c):
        return a + b + c

    def sub(a,b):
        return a/b

    def mag(a,b):
        return a*b

    ##————————————————————————————————
    ##设置一个名为timedata的数据作为全局变量 
    time_data = globals()
    ##把命名为timedata【timestep1370000】…………的字典对应的dataframe的格式进行声明
    for i in range(kaishi,jieshu,timestep):
        time_data['timestep'+str(i)] = pd.DataFrame(columns=['Chunk', 'Coord1','Ncount','c_peratom[1]', 'c_peratom[2]', 'c_peratom[3]'])

    #rawshuju = pd.read_table(filename,header=None)

    ##_________________________________________
    ##定义一个应力输出的数据库格式#修改chunk树木之后，这里也是需要组改变的一个地方————————————————————————不可忽略
    yingli_shuchu =pd.DataFrame([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],columns=['chunk'])
    #11,12,13,14,15,16,17,18,19,20

    print(yingli_shuchu)

    ##__________________________________________
    ##打开文件stress.txt   
    with open(filename, 'r') as file:
        for i in range(kaishi,jieshu,timestep):
            line = file.readline()#用于跳过每次读取数据时的文件头使用
            bashfile = open(filepath + 'new' + '.txt','w')#创建一个bash文件，用于在存取数据时进行过渡
            bashfilename = filepath + 'new' + '.txt'#该bash文件的路径和文件名需要定义以调用
            for t in range(0,chunkshumu,1):#跳过每次读取数据时的头一行后，循环十次，读取其中的内容
                line = file.readline()
                line = line[2:-1]#去除头两个字符和倒数第一个字符
                fh = open(bashfilename, 'w')#打开bashfile并且把刚刚读到内存里的数据写出来到bash里面
                fh.write(line)
                fh.close()
                #这时定义一个对应着bashfile的临时的数据库，用于存取和过渡里面保存的信息，并按照其格式使用通配符进行匹配和读取
                df = pd.read_table(bashfilename,sep='\s+',names=['Chunk', 'Coord1','Ncount','c_peratom[1]', 'c_peratom[2]', 'c_peratom[3]'])
                #这时调用全局变量的数据库，并把刚刚存在临时的数据库中的信息，写到这个全局变量对应的字典里面去
                time_data['timestep'+str(i)] = time_data['timestep'+str(i)].append(df)
                #这时把timedata这个字典的数据转化成dataframe
                time_data1 = pd.DataFrame(time_data['timestep'+str(i)])
                #使用加法运算把三列数据加起来并保存在sumstress列
                time_data1['sumstress'] = time_data1.apply(lambda x: add(x['c_peratom[1]'],x['c_peratom[2]'],x['c_peratom[3]']), axis=1)
                #把合起来的值除以三并保存在substress列
                time_data1['substress'] = time_data1.apply(lambda x: sub(x['sumstress'], 3), axis=1)
            #新建一个名为volumelist1的空列，用于存储体积数据
            time_data1['volume_list1'] = ''
            #把之前创建的volumelist的列表写入到这里的timedata的dataframe的对应的volumelist1这一列中
            time_data1['volume_list1'] = volume_list
            #将算出来的除以三的应力再除以对应的体积列表中的体积
            time_data1['fuyingli'] = time_data1.apply(lambda x: sub(x['substress'], x['volume_list1']), axis=1)
            #进行正负反转的计算
            time_data1['zhengyingli'] = time_data1.apply(lambda x: sub(x['fuyingli'], -1), axis=1)
            #将所有原子的平均，乘以原子总数，得到整个体系的实际值
            time_data1['zhenshiyingli'] = time_data1.apply(lambda x: mag(x['zhengyingli'], x['Ncount']), axis=1)
            #输出所有的timedata中的数据到csv文件中
            #time_data1.to_csv(filepath + '{}.csv'.format(i))
            #定义一系列列表，并把timedata1中的真实盈利导出为列表格式保存在其中
            yingli_shuchu['{}'.format(i)] = time_data1['zhenshiyingli'].values.tolist()
            #显示目前运行到的步骤
            print(i)
        #输出所有的分块数据
        yingli_shuchu.to_csv(filepath + name+'.csv')
        #将得到的dataframe中的数据进行转置
        yingli_zhuanzhi = pd.DataFrame(yingli_shuchu.values.T,index = yingli_shuchu.columns,columns=yingli_shuchu.index)
        #输出所有的转置后的分块数据
        yingli_zhuanzhi.to_csv(filepath + name+'转制'+'.csv')
        print(yingli_shuchu)  

#files = os.listdir(filepath)
#files.sort()
#files.sort(key = lambda x: float(x[10:-4]))#按照数字大小排序         
#for file in files:
    #filen = filepath + '/' +file

chunk_stress(filename,kaishi,jieshu,timestep,chunkshumu,tixidaxiao)

   
   


