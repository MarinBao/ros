#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   clear_area_deal.py
@Time    :   2022/04/21 15:58:14
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''


import re
from common_use import *
import json
import os.path as path


def clear_area_deal(clear_area_infos):
    clear_area_Info={"clear_area":[]}
    for data in clear_area_infos:
        clear_area={"name":"","id":"","overlap_id":[],"polygon":{"points":[]}}
        clear_area["name"]="clear_area"
        clear_area["id"]=re.search(r"id:\"(.*?)\"}",data).group(1)
        clear_area["polygon"]["points"]=common_get_points(re.findall(r"point{(.*?)}",data))

        clear_area_data=data[data.find("overlap_id{"):data.find("polygon{")]
        try:    
            clear_area["overlap_id"]=re.findall(r"id:\"(.*?)\"}",clear_area_data)
        except:
            pass
            
        clear_area_Info["clear_area"].append(clear_area)

    with open("Data/clear_area.json","w",encoding="utf-8") as f:
        json.dump(clear_area_Info,f)