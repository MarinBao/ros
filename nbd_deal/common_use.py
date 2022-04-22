
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   common_use.py
@Time    :   2022/04/19 16:53:30
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

import re 


def common_get_points(points):#chaunru   xyz  list
    point_out=[]
    for point in points:
        # print("1")
        x_str=re.search(r"x:(.*?)y",point).group(1)
        x_str=float(x_str)
        y_str=re.search(r"y:(.*?)z",point).group(1)
        y_str=float(y_str)
        # z_str=re.search(r"z:(.*?)",point).group(1)
        # z_str=float(z_str)+0.0
        point_out.append({"x":x_str,"y":y_str,"z":0.0})
    return point_out


def common_get_id(data):
    id_str=re.findall(r"id:(.*?)}",data)[0]
    id_str=re.findall(r"\"(.*?)\"",id_str)[0]
    # id_str.replace('"',"")
    return id_str



def get_segment_s_info(surplus_data):
    s=float(re.search(r"}s:(.*?)start_position",surplus_data).group(1))
    start_position=common_get_points(re.findall(r"start_position{(.*?)}heading",surplus_data))[0]
    heading=float(re.search(r"}heading:(.*?)length",surplus_data).group(1))
    length=float(re.search(r"length:(.*?)}",surplus_data).group(1))
    return s,start_position,heading,length