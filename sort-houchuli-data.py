##数据分类--------------------------------------#
import os 
import warnings
import re
import shutil
def movefile(orifile,tardir):
    if os.path.isfile(orifile):#用于判断某一对象(需提供绝对路径)是否为文件
        shutil.copy(orifile, tardir)#shutil.copy函数放入原文件的路径文件全名  然后放入目标文件夹


filepath = r'E:\30nm实验数据汇总\2022.11.18.duoKjisuan\py后处理/'
print('cd {}'.format(filepath))
os.chdir('{}'.format(filepath))
os.system('mkdir jisuan total bash')
files = os.listdir(filepath)
for file in files:
    if re.findall(r'jisuan',file) and re.findall(r'转制',file):
        orifile = filepath + '/' + file
        dirfile = filepath +'/' + 'jisuan' +'/'
        movefile(orifile,dirfile)
    elif re.findall(r'total',file) and re.findall(r'转制',file):
        orifile = filepath + '/' + file
        dirfile = filepath +'/' + 'total' +'/'
        movefile(orifile,dirfile)
    else:
        orifile = filepath + '/' + file
        dirfile = filepath +'/' + 'bash' +'/'
        movefile(orifile,dirfile)
        bash = re.findall(r'/d+',file)
        print(bash)
