import sys
from PIL import Image
import os
import re
dir='pics/'
def coder(arg):
    fnames=[]
    letters = re.sub(r'[^а-яА-Я ]', r'',arg.lower(), re.U)
    #print(letters)
    for l in letters:
        fnames.append(dir+l+'.png' if l!=' ' else dir+'space.png')
    if ((len(letters) > 20) and (len(letters) % 20 > 0)):
        for i in range(20-len(letters)%20):
            fnames.append(dir+'space.png')

    images = [Image.open(x) for x in fnames]
    widths, heights = zip(*(i.size for i in images))

    total_width = min(sum(widths), 20*100)
    max_height = max(heights)* (len(letters) // 20+1)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    y_offset = 0
    counter = 0
    for im in images:
        new_im.paste(im, (x_offset,y_offset))
        x_offset += im.size[0]
        counter += 1
        if (counter % 20 == 0):
            y_offset += im.size[0]
            x_offset=0


    new_im.save(arg+'.jpg')

arg=input('Введите строку для зашифровки: ')
coder(arg)