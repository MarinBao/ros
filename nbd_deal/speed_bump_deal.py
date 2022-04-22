#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   speed_bump_deal.py
@Time    :   2022/04/21 16:33:14
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

import re
from turtle import speed
from common_use import *
import json
import os.path as path

def get_segment_surplus_info(surplus_data):
    s=float(re.search(r"}s:(.*?)start_position",surplus_data).group(1))
    start_position=common_get_points(re.findall(r"start_position{(.*?)}heading",surplus_data))[0]
    heading=float(re.search(r"}heading:(.*?)length",surplus_data).group(1))
    length=float(re.search(r"length:(.*?)}",surplus_data).group(1))
    return s,start_position,heading,length


def speed_bump_deal(speed_bump_infos):
    speed_bump_Info={"speed_bump":[]}
    for data in speed_bump_infos:
        speed_bump={"name":"","id":"","overlap_id":[],"position":{"segment":{"line_segment":{"points":[]},
                    "s":0,"start_position":[],"heading":0,"length":0}}}
        speed_bump["name"]="speed_bump"
        speed_bump["id"]=re.search(r"id:\"(.*?)\"}",data).group(1)
        speed_bump["overlap_id"]=re.findall(r"id:\"(.*?)\"}",data[data.find("overlap_id{"):])
        # print(data[data.find("overlap_id{"):])
        speed_bump["position"]["segment"]["line_segment"]["points"]=common_get_points(re.findall(r"point{(.*?)}",data[data.find("line_segment{"):]))


        s,start_position,heading,length=get_segment_surplus_info(data[data.find("line_segment{"):])
        speed_bump["position"]["segment"]["s"]=s
        speed_bump["position"]["segment"]["start_position"]=start_position
        speed_bump["position"]["segment"]["heading"]=heading
        speed_bump["position"]["segment"]["length"]=length

        speed_bump_Info["speed_bump"].append(speed_bump)

    with open("Data/speed_bump.json","w",encoding="utf-8") as f:
        json.dump(speed_bump_Info,f)