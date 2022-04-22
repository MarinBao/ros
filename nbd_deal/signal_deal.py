#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   signal_deal.py
@Time    :   2022/04/21 11:47:58
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''


import json
import re
import os
import os.path as path
from common_use import *


signal_inf={"name":"","id":"","subsignal":{"id":"","type":"","location":{"x":0,"y":0,"z":0}},
        "overlap_id":[],"type":"","stop_line":{"segment":{"line_segment":{"points":[]},"s":0,
        "start_position":{"x":0,"y":0,"z":0},"heading":0,"length":0}}
        }

def signal_deal(signal_infos):
    signal_Info={"signal":[]}
    for signal in signal_infos:
        signal_inf["name"]="signal"
        signal_inf["id"]=re.search(r"id:\"(.*?)\"}",signal).group(1)

        subsignal_data=signal[signal.find("subsignal{"):signal.find("}overlap_id{")+1]
        signal_inf["subsignal"]["id"]=re.search(r"id:\"(.*?)\"}",subsignal_data).group(1)
        signal_inf["subsignal"]["type"]=re.search(r"type:(\w*)location",subsignal_data).group(1)
        signal_inf["subsignal"]["location"]["x"]=float(re.search(r"x:(.*?)y",subsignal_data).group(1))
        signal_inf["subsignal"]["location"]["y"]=float(re.search(r"y:(.*?)z",subsignal_data).group(1))
        signal_inf["subsignal"]["location"]["z"]=float(re.search(r"z:(.*?)}",subsignal_data).group(1))

        surplus_data=signal[signal.find("overlap_id{"):]
        signal_inf["overlap_id"]=re.findall(r"{id:\"(.*?)\"}",surplus_data)
        signal_inf["type"]=re.search(r"type:(\w*)stop_line",surplus_data).group(1)

        points=re.findall(r"point{(.*?)}",surplus_data)
        signal_inf["stop_line"]["segment"]["line_segment"]=common_get_points(points)
        signal_inf["stop_line"]["segment"]["s"]=float(re.search("s:(.*?)start_position",surplus_data).group(1))
        signal_inf["stop_line"]["segment"]["heading"]=float(re.search("heading:(.*?)length",surplus_data).group(1))
        signal_inf["stop_line"]["segment"]["length"]=float(re.search("length:(.*?)}",surplus_data).group(1))
        start_position_info=surplus_data[surplus_data.find("start_position"):surplus_data.find("heading")]
        signal_inf["stop_line"]["segment"]["start_position"]["x"]=float(re.search("start_position{x:(.*?)y",surplus_data).group(1))
        signal_inf["stop_line"]["segment"]["start_position"]["y"]=float(re.search("y:(.*?)z",start_position_info).group(1))
        signal_inf["stop_line"]["segment"]["start_position"]["z"]=float(re.search("z:(.*?)}",start_position_info).group(1))
        signal_Info["signal"].append(signal_inf)
    if not path.exists("Data/signal.json"):
        with open("Data/signal.json","w",encoding="utf-8") as f:
            json.dump(signal_Info,f)