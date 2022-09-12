import os
import pandas as pd
import numpy as np
import math as math

filepath = r'E:/2022.1.17.shaojiejing/'
filename = r'duoqiu.txt'
pathsave = r'E:/2022.1.17shaojiejingpanduan/'
filewhole = filepath + filename
print("数据名")
print("\t")
print(filewhole)
files = os.listdir(filepath)
for file in files:
    print("\t" +file)
files.sort()
files.sort(key = lambda x: float(x[:-4]))#掐头去尾


newfilename = 'shaojiequxian.txt'
newfilename = pathsave + newfilename

# #_______________________________________去除文件头尾
# if filewhole:
#     with open(filename,'r', encoding='utf-8') as d:
#         contents = d.readlines()
#     with open(filename, 'w') as l:
#         #for line in contents:
#             #if "LAMMPS" in line:
#         l.write(''.join(contents[9:]))
#             #else:
#                 #continue
# #_________________________________________________________
# for file in files:
#     print("\t" +file)
for file in files:
        file = filepath + file
        with open(file, 'r', encoding='utf-8') as d:
            contents = d.readlines()
        with open(file, 'w') as d:
            d.write(''.join(contents[9:]))  # 打开存储于内存中的文件，然后对其进行遍历并删除文件当中的头9行!!!!!!!!!!!!!!!!!!!!!!!!!!!!!后面运行记得改回来d.write(''.join(contents[9:]))
print("模拟空间大小为：")
size = float(230)
#size = float(input())
print("设置有限元格子的大小:(推荐值为10，！！最小为7.22)")
cutoff = float(5)
#cutoff = float(input())
print("总原子数：")
total = int(50000)
#total = int(input())       
for file in files:
    data = np.loadtxt(filepath+file)
    df = pd.DataFrame(data, columns=['id', 'type', 'x', 'y', 'z'])


    print(df)
    print(df.loc[0])

    # print("模拟空间大小为：")
    # size = float(input())
    x1 = size
    x2 = size
    y1 = size
    y2 = size
    z1 = size
    z2 = size
    #————————————————————————————————————————对体系精细划分的时候使用的方法
    # print("输入x下界：")
    # x1 = float(input())
    # print("输入x上界：")
    # x2 = float(input())
    # print("输入y下界：")
    # y1 = float(input())
    # print("输入y上界：")
    # y2 = float(input())
    # print("输入z下界：")
    # z1 = float(input())
    # print("输入x上界：")
    # z2 = float(input())
    #________________________________________
    # print("设置有限元格子的大小:(推荐值为10，！！最小为7.22)")
    # cutoff = float(input())
    # print("总原子数：")
    # total = int(input())
    total = df.shape[0]
    print(total)
    # print ("确认请按任意键：")
    # confirm = input()
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

    minim = 3.61 #这是铜原子的晶格常数，最小划分也仅此
    nx = int(size/cutoff)
    ny = int(size/cutoff)
    nz = int(size/cutoff)
    print("划分后的格子数目：")
    print(nx,ny,nz)

    x = np.linspace(-x1,x2,nx)
    y = np.linspace(-y1,y2,ny)
    z = np.linspace(-z1,z2,nz)
    kjm = np.meshgrid(x,y,z)

    # xp = np.linspace(0,0,nx)
    # yp = np.linspace(0,0,ny)
    # zp = np.linspace(0,0,nz)
    # kkp = np.meshgrid(xp,yp,zp)
    chutu = pd.DataFrame(columns=['x','y','z','number','True'])
    #print(kjm)
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
    #print(my_dict)
    print("字典创建完成————————————————————————")

    #print("创建判定条件：")
    for i in range(0,geshu):
        dv['a'+str(i)] = float(kjm[0][i,i,i])
        #print("划分：")
        #print('a'+str(i))
    print("判定条件创建完成————————————————————")

    # print(a0)
    #print("未显示全部")
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
                lenth = len(my_dict['c'+str(i)+str(j)+str(k)])
                #print(len(my_dict['c'+str(i)+str(j)+str(k)]),end = '个原子，对应块：')
                b = {"x":i,"y":j,"z":k,"number":lenth}
                chutu = chutu.append(b,ignore_index=True)
                #print('c'+str(i)+str(j)+str(k))
                allatom = allatom + len(my_dict['c'+str(i)+str(j)+str(k)])

    print("请确认！！！————总原子数为：")
    print(allatom)
    ok_data = globals()
    for i in range(0,geshu-1):
        for j in range(0,geshu-1):
            for k in range(0,geshu-1):
                data3 = my_dict['c'+str(i)+str(j)+str(k)]
            
                ok_data['c'+str(i)+str(j)+str(k)] = pd.DataFrame(data3,columns=['id', 'type', 'x', 'y', 'z']) 
                #print(ok_data['c'+str(i)+str(j)+str(k)])

    #print(ok_data)
    print("所有的列表格式文件均转化成了对应的数据库文件，并以ok_data，c000的格式命名（以维度为准）")

    shaojie = 0


    for i in range(0,geshu-1):
        for j in range(0,geshu-1):
            for k in range(0,geshu-1):
                datacheck = []
                for t in ok_data['c'+str(i)+str(j)+str(k)].index:
                    #datacheck = []
                    #ok_data['c'+str(i)+str(j)+str(k)] = 
                    datacheck.append(ok_data['c'+str(i)+str(j)+str(k)].loc[t,'type'])
                    #print(ok_data['c'+str(i)+str(j)+str(k)].loc[t,'type'])
                    #print(datacheck)
                p = len(set(datacheck))
                if p > 1:
                    df = chutu.loc[chutu['x'] == i]
                    df = df.loc[chutu['y'] == j]
                    df = df.loc[chutu['z'] == k]
                    chutu.loc[df.loc[chutu['z'] == k].index,'True'] = 1
                    shaojie+=1
                    #print(shaojie)
                    #print("重复！！！！！！！！！！！！！！！！")
                else:
                    print(shaojie)

    print(shaojie)
    shaojie = str(shaojie)
    with open(newfilename,'a') as x:#在其后面添加数据
        x.write(shaojie)
        x.write(' ')
   #with
        step = str(file[:-4])#——————————————————————————————————————————————————————————————————根据文件头尾进行修改
        x.write(step)
        x.write('\n')
    chutu.to_csv(pathsave + '{}.csv'.format(step))
    #_________________判断是否存在相同元素的办法