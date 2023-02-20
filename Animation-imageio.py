import matplotlib.pyplot as plt
from time import sleep  
from matplotlib.animation import FuncAnimation
import imageio
import os
zosave = r'E:\30nm实验数据汇总\视频分析，振动\r-154/'
images3 = []
filetus = os.listdir(zosave)
filetus.sort(key=lambda x:int(x[-8:-4]))
print(filetus)
for filetu in filetus:
    name = str(filetu)
    name = zosave + name
    images3.append(imageio.imread(name))
imageio.mimsave(zosave + 'zo1.gif', images3,duration=0.016)