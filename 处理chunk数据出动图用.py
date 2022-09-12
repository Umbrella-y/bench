import pandas as pd
import numpy as np
import os
from hashlib import new
from pdb import line_prefix
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import matplotlib.pyplot as plt
from time import sleep  
from matplotlib.animation import FuncAnimation
import imageio
from PIL import Image, ImageSequence
filesave = r'E:\2022.5.9.震动消除/出图/'
filename = r'E:\2022.4.29.xiaochuhouchongsuan\stress\3000-5000出图/'
print(filename)
filen = r'E:\2022.5.9.震动消除/2022.5.9.1.振动消除stress300-300.txt.csv'

def shuju_dantu(df,tusave):
    dflen = df.shape[1]
    for i in range(0,dflen):
        plt.cla()
        x = df.index
        y = df.iloc[:,i]
        plt.xlim(0, 20)
        plt.ylim(-12000, 12000)
        plt.xlabel('Chunk')
        plt.ylabel('Pressure (Bar)')
        plt.title('step' + '{}'.format(i) )
        plt.plot(x,y)
        #plt.show()
        plt.savefig(tusave + '{}.jpg'.format(i))

def compressGif(filename):
    gif = Image.open(filename)
    if not gif.is_animated:
        return False
    imageio.mimsave('compress-'+filename, [frame.convert('RGB') for frame in ImageSequence.Iterator(gif)], duration = gif.info['duration']/2000) 

def shuju_dongtu(tusave):
    images = []
    filetus = os.listdir(tusave)
    filetus.sort(key=lambda x:int(x[:-4]))
    print(filetus)
    for filetu in filetus:
        name = str(filetu)
        name = tusave + name
        images.append(imageio.imread(name))
    imageio.mimsave(tusave + 'chunk应力变化.gif', images,fps = 60 )



df = pd.read_csv(filen)
print(df)
giffile = filesave + 'chunk应力变化.gif'
print(giffile)
shuju_dantu(df,filesave)
shuju_dongtu(filesave)
#compressGif(giffile)