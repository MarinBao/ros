#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   parking_space_deal.py
@Time    :   2022/04/21 22:30:58
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

from distutils.filelist import findall
import re
from common_use import *
import json
import os.path as path



def parking_space_deal(parking_space_infos):
    parking_space_Info={"parking_space":[]}
    for data in parking_space_infos:
        parking_space={"name":"","id":"","polygon":{"points":[]},"overlap_id":"","heading":0}
        parking_space["name"]="parking_space"
        parking_space["id"]=re.search(r"id:\"(.*?)\"}",data).group(1)

        parking_space["polygon"]["points"]=common_get_points(re.findall(r"point{(.*?)}",data))
        
        try:
            parking_space["overlap_id"]=re.search(r"id:\"(.*?)\"}",data[data.find("polygon"):]).group(1)
        except:
            pass       
        parking_space["heading"]=float(re.search(r"heading:(.*?)}",data[data.find("polygon"):]).group(1))
        parking_space_Info["parking_space"].append(parking_space)

    with open("Data/parking_space.json","w",encoding="utf-8") as f:
        json.dump(parking_space_Info,f)


