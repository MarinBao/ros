#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   road_deal.py
@Time    :   2022/04/21 17:22:07
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

from distutils.filelist import findall
import re
from common_use import *
import json
import os.path as path


def road_deal(road_infos):
    road_Info={"road":[]}

    for data in road_infos:
        edge_1={"curve":{"segment":{"line_segment":{"points":[]}}}}
        edge_2={"curve":{"segment":{"line_segment":{"points":[]}}}}
        boundary={"outer_polygon":[edge_1,edge_2]}
        section={"id":"","lane_id":"","boundary":boundary}
        road={"name":"","id":"","section":section}


        road["name"]="road"
        road["id"]=re.search(r"id:\"(.*?)\"}",data).group(1)
        road["section"]["id"]=re.search(r"id:\"(.*?)\"}",data[data.find("section"):data.find("lane_id{")]).group(1)
        road["section"]["lane_id"]=re.findall(r"id:\"(.*?)\"}",data[data.find("}lane_id{"):data.find("}boundary{")+1])
        road["section"]["boundary"]["outer_polygon"][0]["curve"]["segment"]["line_segment"]["points"]=\
        common_get_points(re.findall(r"point{(.*?)}",data.split("}edge{")[0]))
        s,start_position,heading,length=get_segment_s_info(data.split("}edge{")[0])
        road["section"]["boundary"]["outer_polygon"][0]["curve"]["segment"]["s"]=s
        road["section"]["boundary"]["outer_polygon"][0]["curve"]["segment"]["start_position"]=start_position
        road["section"]["boundary"]["outer_polygon"][0]["curve"]["segment"]["heading"]=heading
        road["section"]["boundary"]["outer_polygon"][0]["curve"]["segment"]["length"]=length
        road["section"]["boundary"]["outer_polygon"][0]["type"]=re.search(r"type:(\w*)",data.split("}edge{")[0]).group(1)


        road["section"]["boundary"]["outer_polygon"][1]["curve"]["segment"]["line_segment"]["points"]=\
        common_get_points(re.findall(r"point{(.*?)}",data.split("}edge{")[1]))
        s,start_position,heading,length=get_segment_s_info(data.split("}edge{")[1])
        road["section"]["boundary"]["outer_polygon"][1]["curve"]["segment"]["s"]=s
        road["section"]["boundary"]["outer_polygon"][1]["curve"]["segment"]["start_position"]=start_position
        road["section"]["boundary"]["outer_polygon"][1]["curve"]["segment"]["heading"]=heading
        road["section"]["boundary"]["outer_polygon"][1]["curve"]["segment"]["length"]=length
        road["section"]["boundary"]["outer_polygon"][1]["type"]=re.search(r"type:(\w*)",data.split("}edge{")[1]).group(1)

        sutplus_data=data[data.find("junction_id{"):]
        road["section"]["junction"]=re.findall(r"id:\"(.*?)\"}",sutplus_data)
        road["section"]["type"]=re.search(r"type:(\w*)",sutplus_data).group(1)

        if len(road["section"]["junction"])>1:
            print("junction>1",road["id"])

        road_Info["road"].append(road)
    with open("Data/road.json","w",encoding="utf-8") as f:
        json.dump(road_Info,f)
