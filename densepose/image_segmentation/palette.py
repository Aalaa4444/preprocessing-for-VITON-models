from PIL import Image
import numpy as np

img0 = Image.open('./output/0.png')
img1 = Image.open('sample.png')
width, height = img0.size

print(width, height)

palette11 = img1.getpalette()
img0.putpalette(palette11)

load0 = img0.load()

for i in range(width):
    for n in range(height):
        if(load0[i, n] == 4):
            load0[i, n] = 5
        elif(load0[i, n] == 5):
            load0[i, n] = 12
        elif(load0[i, n] == 11):
            load0[i, n] = 13
        elif(load0[i, n] == 12):
            load0[i, n] = 16
        elif(load0[i, n] == 13):
            load0[i, n] = 17

img0.save('./output/0.png')


# add neck by brown color 
small_face, big_face, real_face = [], [], []      # real = big - small
no_neck_img = Image.open('./output/1.png')        # pixel 13 means face
no_neck_load = no_neck_img.load()
for i in range(width):                          # width = 768
    for n in range(height):                     # height = 1024
        if no_neck_load[i, n] == 13:
            small_face.append([i, n])


for i in range(width):                          # width = 768
    for n in range(height):                     # height = 1024
        if load0[i, n] == 13:
            big_face.append([i, n])

for i in big_face:
    if i not in small_face:
        load0[i[0], i[1]] = 10


img0.save('./output/0.png')