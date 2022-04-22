#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   junction_deal.py
@Time    :   2022/04/19 20:36:53
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

import re
from common_use import *
import json
import os.path as path

def get_polygon(data):
    points=re.findall(r"point{(.*?)0.0}",data)     #提取所有点特征  point{x,y,z}
    points=common_get_points(points)        #提取
    return({"points":points})

def junction_deal(junctions):
    junction_datas={"junction":[]}
    for data in junctions:
        junction_data={"name":"","id":"","polygon":{}}
        junction_data["name"]="junction"
        junction_data["id"]=common_get_id(data)
        # print("crosswalk_data[id]",type(crosswalk_data["id"]))
        junction_data["polygon"]=get_polygon(data)
        

        junction_datas["junction"].append(junction_data)

    # crosswalk_datas


    if not path.exists("Data/junction.json"):
        with open("Data/junction.json","w",encoding="utf-8") as f:
            json.dump(junction_datas,f)