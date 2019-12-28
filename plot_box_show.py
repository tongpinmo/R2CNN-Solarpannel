import numpy as np
import natsort
import shutil
from PIL import Image
import os
import cv2
#-----------------------------------plot bbox of whole images file
filepath = './bbox.txt'
imgpath = '/mnt/a409/SIBITU/SIBITU_Dataset/SIBITU_AI/Cluster/01/DJI_0307_R.JPG'

img_name = os.path.basename(imgpath)

if os.path.exists('cv2_box/'):
  shutil.rmtree('cv2_box/')

os.mkdir('cv2_box/')

with open(filepath,'r') as f:
    f = f.readlines()
    for line in f:
        line = line.strip().split(' ')
        print('line: ',line)

#------------------------------------cv2---center-------------
    
        x_1 = int(float(line[0]))
        print('x_center: ',x_1)
        y_1 = int(float(line[1]))

        x_2 = int(float(line[2]))
        y_2 = int(float(line[3]))

        x_3 = int(float(line[4]))
        y_3 = int(float(line[5]))

        x_4 = int(float(line[6]))
        y_4 = int(float(line[7]))

        radius = 2
        point_color = (0,0,255)

        img = cv2.imread(imgpath)  # cv2.imread()-----numpy.ndarry

        cv2.circle(img, (x_1,y_1), radius, point_color, thickness=2)
        cv2.circle(img, (x_2, y_2), radius, point_color, thickness=2)
        cv2.circle(img, (x_3, y_3), radius, point_color, thickness=2)
        cv2.circle(img, (x_4, y_4), radius, point_color, thickness=2)
    cv2.imwrite(os.path.join('cv2_box/' + img_name + '.jpg'), img)
    

#------------------------------------cv2-Rectangle images-------------------

    #     point_color = (0,0,255)
    #
    #     img = cv2.imread(imgpath)  # cv2.imread()-----numpy.ndarry
    #     x_left = int(float(line[0]))
    #     y_left = int(float(line[1]))
    #     x_right = int(float(line[4]))
    #     y_right = int(float(line[5]))
    #     print('x_left:',x_left)
    #     print('y_left:',y_left)
    #     print('x_right:',x_right)
    #     print('y_right:',y_right)
    #
    #     cv2.rectangle(img,(x_left,y_left),(x_right,y_right),point_color,thickness=2)
    # cv2.imwrite(os.path.join('cv2_box/'+ img_name +'.jpg'),img)


