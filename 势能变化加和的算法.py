import os

#使用代码之前需要把所有的路径中的\改成/

path = r'E:/2022.3.21.不同速度/chuli/'#path of peatom
pathsave = r'E:/2022.3.21.不同速度/'
newfilename = 'energy of a single one15nm.txt'
newfilename = pathsave + newfilename
n = open(newfilename,'w')
pathpop = path.split('/')
pathpopcount = len(pathpop)
pathpopcount = pathpopcount - 1
print(str(pathpopcount))

files = os.listdir(path)#打开路径下文件
files.sort()#对文件初始化排序
files.sort(key = lambda x: float(x[:-4]))#掐头去尾，按Step排列文件进入内存——————————————————————————————————————————————————————————根据文件名称进行修改

for file in files :
    print("\t"+file)#将排序结果展示到主屏幕

for file in files:
        if 'one' in file:
            continue
        if '加和' in file:
            continue

        file = path + file
        with open(file, 'r', encoding='utf-8') as d:
            contents = d.readlines()
        with open(file, 'w') as d:
            d.write(''.join(contents[9:]))  # 打开存储于内存中的文件，然后对其进行遍历并删除文件当中的头9行

for file in files:
    s = 0
    c = 0
    if 'sum' in file:
        continue
    if '数据' in file:
        continue
    file = path + file
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file,'w') as w:
        for line in lines:
            c += 1
            line = float(line)
            s = s + line
    file_str = str(file)

    checkfile = file_str.split('/')
    #for l in checkfile:
        #print(l,end = '')
    print(file_str)
    file_str = ''.join(checkfile[pathpopcount:])
    print(file_str)
    file = str(file_str)
    print(file)
    c=str(c)
    s = str(s)
    with open(newfilename,'a') as x:#在其后面添加数据
        x.write(s)
        
        x.write(' ')

        x.write(c)
        x.write(' ')
   #with
        step = str(file[:-4])#——————————————————————————————————————————————————————————————————根据文件头尾进行修改
        x.write(step)
        x.write('\n')
        print (s)
        print(step)
        print('结束写过程')
    print('结束一阶段')
print('结束过程')