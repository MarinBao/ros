#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   crosswalk_deal.py
@Time    :   2022/04/19 19:34:34
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

from common_use import *
import re 
import matplotlib.pyplot as plt
import json
import os.path as path




def get_polygon(sigle_crosswalk):
    polygon=re.search(r"polygon(.*?)overlap_id",sigle_crosswalk).group(1)
    # print(polygon)
    points=re.findall(r"point{(.*?)0.0}",polygon)
    # print(points)
    # print(len(points))
    points=common_get_points(points)
    return({"points":points})

def get_overlap_id(sigle_crosswalk):
    overlap=re.findall(r"overlap_id{id:\"(.*?)\"}",sigle_crosswalk)
    # print(overlap)
    return overlap


def crosswalk_deal(crosswalks):
    crosswalk_datas={"crosswalk":[]}
    for data in crosswalks:
        crosswalk_data={"name":"","id":"","polygon":{},"overlap_id":[]}
        crosswalk_data["name"]="crosswalk"
        crosswalk_data["id"]=common_get_id(data)
        # print("crosswalk_data[id]",crosswalk_data["id"])
        crosswalk_data["polygon"]=get_polygon(data)
        crosswalk_data["overlap_id"]=get_overlap_id(data)

        crosswalk_datas["crosswalk"].append(crosswalk_data)
    # crosswalk_datas
    if not path.exists("Data/crosswalk.json"):
        with open("Data/crosswalk.json","w",encoding="utf-8") as f:
            json.dump(crosswalk_datas,f)









