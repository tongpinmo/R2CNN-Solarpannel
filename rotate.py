#!/usr/bin/python
import xml.etree.cElementTree as ET
import numpy as np
import math

def read_xml_gtbox_and_label(xml_path):
    """
    :param xml_path: the path of voc xml
    :return: a list contains gtboxes and labels, shape is [num_of_gtboxes, 9],
           and has [x1, y1, x2, y2, x3, y3, x4, y4, label] in a per row
    """

    tree = ET.parse(xml_path)
    root = tree.getroot()
    img_width = None
    img_height = None
    box_list = []
    for child_of_root in root:
        # if child_of_root.tag == 'filename':
        #     assert child_of_root.text == xml_path.split('/')[-1].split('.')[0] \
        #                                  + FLAGS.img_format, 'xml_name and img_name cannot match'

#         if child_of_root.tag == 'size':
#             for child_item in child_of_root:
#                 if child_item.tag == 'width':
#                     img_width = int(child_item.text)
#                 if child_item.tag == 'height':
#                     img_height = int(child_item.text)

        if child_of_root.tag == 'object':
            label = None
            for child_item in child_of_root:
                if child_item.tag == 'name':
                    label = child_item.text
                if child_item.tag == 'robndbox':
                    tmp_box = []
                    for node in child_item:
                        tmp_box.append(float(node.text))
                    assert label is not None, 'label is none, error'
                    tmp_box.append(label)
                    # box_list.append(tmp_box)

#     gtbox_label = np.array(box_list, dtype=np.int32)

    return tmp_box


def calculate_rotated_xy(x1,y1,x2,y2,theta):
    # x = (x1-x2)cos(theta) - (y1-y2)sin(theta) + x2
    # y = (y1-y2)cos(theta) + (x1-x2)sin(theta) + y2
    
    rotated_x = (x1-x2)* math.cos(theta) - (y1-y2)*math.sin(theta) + x2
    rotated_y = (y1-y2)* math.cos(theta) + (x1-x2)*math.sin(theta) + y2
    
    return rotated_x, rotated_y

def get_rotated_xy(box_list):
    x = box_list[0]
    print('x: ',x)
    y = box_list[1]
    print('y: ',y)

    w = box_list[2]
    print('w: ',w)
    h = box_list[3]
    angle = box_list[4]
    label = box_list[5]
    
    #x,y,w,h,theta ->  x_i, y_i ( i = 1,2,3,4)
    x1_, y1_ = x-w/2, y-h/2
    x2_, y2_ = x+w/2, y-h/2
    x3_, y3_ = x+w/2, y+h/2
    x4_, y4_ = x-w/2, y+h/2
    
    x1, y1 = calculate_rotated_xy(x1_, y1_, x, y, angle)
    x2, y2 = calculate_rotated_xy(x2_, y2_, x, y, angle)
    x3, y3 = calculate_rotated_xy(x3_, y3_, x, y, angle)
    x4, y4 = calculate_rotated_xy(x4_, y4_, x, y, angle)


    return [x1,y1,x2,y2,x3,y3,x4,y4,label]


if __name__ == '__main__':
    xml_path = '/mnt/a409/SIBITU/SIBITU_Dataset/SIBITU_AI/label/Cluster/DJI_0307_R.xml'

    box_list = read_xml_gtbox_and_label(xml_path)
    
    print('box_list:',box_list)
    
    xy_label = get_rotated_xy(box_list)

    print('xy_label:',xy_label)

    with open('./bbox.txt','w') as tf:
        for item in xy_label:
            print('item: ',item)
            tf.write(str(item))
            tf.write(' ')

            
