#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lane_deal.py
@Time    :   2022/04/19 21:31:33
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

import re
from common_use import *
import json
import os.path as path
from lane_info import *
import os

def get_segment_surplus_info(surplus_data):
    s=float(re.search(r"}s:(.*?)start_position",surplus_data).group(1))
    start_position=common_get_points(re.findall(r"start_position{(.*?)}heading",surplus_data))
    heading=float(re.search(r"}heading:(.*?)length",surplus_data).group(1))
    length=float(re.search(r"length:(.*?)}",surplus_data).group(1))
    return s,start_position,heading,length

def get_boundary_surplus_info(surplus_data):
    surplus_data=surplus_data[surplus_data.find("}length"):]   #剩余全部信息
    length=float(re.search(r"length:(.*?)virtual",surplus_data).group(1))
    virtual=re.search(r"virtual:(.*?)boundary_type",surplus_data).group(1)

    # print(surplus_data)
    data=re.search(r"boundary_type{(.*?)}",surplus_data).group(1)
    # print(data)
    s=float(re.search(r"s:(.*?)types",data).group(1))
    types=re.search(r"types:(\w*)",data).group(1)
    # print("1",types)
    
    return length,virtual,s,types


def lane_central_curve_deal(central_curve_data):  #传入sigle所有的central_curve信息
    # central_points=re.findall(r"point{(.*?)}",central_curve_data[central_curve_data.find("line_segment"):central_curve_data.find("start_position")])
    central_points=re.findall(r"point{(.*?)}",central_curve_data)
    central_curve["segment"]["line_segment"]["points"]=common_get_points(central_points)
    s,start_position,heading,length=get_segment_surplus_info(central_curve_data)
    central_curve["segment"]["s"]=s
    central_curve["segment"]["start_position"]=start_position
    central_curve["segment"]["heading"]=heading
    central_curve["segment"]["length"]=length
    return central_curve


def lane_left_boudary_deal(boundary_data):
    boundary_points=re.findall(r"point{(.*?)}",boundary_data)
    left_boundary["curve"]["segment"]["line_segment"]["points"]=common_get_points(boundary_points)
    s,start_position,heading,length=get_segment_surplus_info(boundary_data)
    left_boundary["curve"]["segment"]["s"]=s
    left_boundary["curve"]["segment"]["start_position"]=start_position
    left_boundary["curve"]["segment"]["heading"]=heading
    left_boundary["curve"]["segment"]["length"]=length

    length,virtual,s,types=get_boundary_surplus_info(boundary_data)
    left_boundary["length"]=length
    left_boundary["virtual"]=virtual
    left_boundary["boundary_type"]["s"]=s
    left_boundary["boundary_type"]["types"]=types

    return left_boundary

def lane_right_boudary_deal(boundary_data):
    boundary_points=re.findall(r"point{(.*?)}",boundary_data)
    right_boundary["curve"]["segment"]["line_segment"]["points"]=common_get_points(boundary_points)
    s,start_position,heading,length=get_segment_surplus_info(boundary_data)
    right_boundary["curve"]["segment"]["s"]=s
    right_boundary["curve"]["segment"]["start_position"]=start_position
    right_boundary["curve"]["segment"]["heading"]=heading
    right_boundary["curve"]["segment"]["length"]=length

    length,virtual,s,types=get_boundary_surplus_info(boundary_data)
    right_boundary["length"]=length
    right_boundary["virtual"]=virtual
    right_boundary["boundary_type"]["s"]=s
    right_boundary["boundary_type"]["types"]=types

    return right_boundary



'''
input data
get list id
'''
def get_related_ids(data):
    id_out=[]
    id=re.findall(r"id:\"(.*?)\"}",data)
    for i in id:
        id_out.append(i)
    return id_out



def get_left_sample(data_surplus):
    sample_out=[]
    
    sample_data=re.findall(r"left_sample{(.*?)}",data_surplus)
    for sd in sample_data:
        sample={"s":0.0,"width":0.0}
        sample["s"]=float(re.search(r"s:([0-9]*\.[0-9]*)",sd).group(1))
        sample["width"]=float(re.search(r"width:([0-9]*\.[0-9]*)",sd).group(1))
        sample_out.append(sample)
    return sample_out

def get_right_sample(data_surplus):
    sample_out=[]
    
    sample_data=re.findall(r"right_sample{(.*?)}",data_surplus)
    for sd in sample_data:
        sample={"s":0.0,"width":0.0}
        sample["s"]=float(re.search(r"s:([0-9]*\.[0-9]*)",sd).group(1))
        sample["width"]=float(re.search(r"width:([0-9]*\.[0-9]*)",sd).group(1))
        sample_out.append(sample)
    return sample_out

def get_left_road_sample(data_surplus):
    sample_out=[]
    
    sample_data=re.findall(r"left_road_sample{(.*?)}",data_surplus)
    for sd in sample_data:
        sample={"s":0.0,"width":0.0}
        sample["s"]=float(re.search(r"s:([0-9]*\.[0-9]*)",sd).group(1))
        sample["width"]=float(re.search(r"width:([0-9]*\.[0-9]*)",sd).group(1))
        sample_out.append(sample)
    return sample_out

def get_right_road_sample(data_surplus):
    sample_out=[]
    
    sample_data=re.findall(r"right_road_sample{(.*?)}",data_surplus)
    for sd in sample_data:
        sample={"s":0.0,"width":0.0}
        sample["s"]=float(re.search(r"s:([0-9]*\.[0-9]*)",sd).group(1))
        sample["width"]=float(re.search(r"width:([0-9]*\.[0-9]*)",sd).group(1))
        sample_out.append(sample)
    return sample_out



def lane_deal(lanes):  #传入lanes 列表 
    i=0
    if not path.exists("Data/lane"):
        os.makedirs("Data/lane") 
        for data in lanes:
            i+=1
            lane["name"]="lane"
            lane["id"]=common_get_id(data)
            # print(lane["id"])
            lane["centrol_curve"]=lane_central_curve_deal(data[data.find("central_curve"):data.find("left_boundary")-1])
            # print("1",data.find("central_curve"))
            
            lane["left_boundary"]=lane_left_boudary_deal(data[data.find("left_boundary"):data.find("right_boundary")-1])
            lane["right_boundary"]=lane_right_boudary_deal(data[data.find("right_boundary"):data.find("speed_limit")-1])  
            
            
            data_surplus=data[data.find("speed_limit")-40:]
            lane["length"]=float(re.search(r"length:([0-9]*\.[0-9]*)speed_limit",data_surplus).group(1))
            lane["speed_limit"]=float(re.search(r"speed_limit:([0-9]*\.[0-9]*)",data_surplus).group(1))
            lane["overlap_id"]=get_related_ids(data_surplus[data_surplus.find("overlap_id"):data_surplus.find("predecessor_id")])
            lane["predecessor_id"]=re.findall(r"predecessor_id{id:\"(.*?)\"}",data_surplus)
            lane["successor_id"]=re.findall(r"successor_id{id:\"(.*?)\"}",data_surplus)
            
            if i==2:
                # print("3",data[data.find("left_boundary"):data.find("right_boundary")-1])
                # print("2",data[data.find("central_curve"):data.find("left_boundary")-1])
                print(data_surplus[data_surplus.find("overlap_id"):data_surplus.find("predecessor_id")])
                print("3\n",get_related_ids(data_surplus[data_surplus.find("overlap_id"):data_surplus.find("predecessor_id")]))
            

            lane["left_neighbor_forward_lane_id"]=re.search(r"left_neighbor_forward_lane_id{id:\"(.*?)\"}",data_surplus).group(1)
            lane["right_neighbor_forward_lane_id"]=re.search(r"right_neighbor_forward_lane_id{id:\"(.*?)\"}",data_surplus).group(1)
            lane["type"]=re.search(r"type:(.*?)turn",data_surplus).group(1)
            lane["turn"]=re.search(r"turn:(.*?TURN)",data_surplus).group(1)
            lane["left_neighbor_reverse_lane_id"]=re.findall(r"left_neighbor_reverse_lane_id{id:\"(.*?)\"}",data_surplus)
            # print(re.search(r"junction_id{(id:.*?)left_sample",data_surplus).group(1))

            lane["junction_id"]=re.search(r"junction_id{id:\"(.*?)\"}",data_surplus).group(1)
            lane["direction"]=re.search(r"direction:(.*?)left_road_sample",data_surplus).group(1)
            lane["left_sample"]=get_left_sample(data_surplus)
            lane["right_sample"]=get_right_sample(data_surplus)
            lane["left_road_sample"]=get_left_road_sample(data_surplus)
            lane["right_road_sample"]=get_right_road_sample(data_surplus)

            
            
            with open("Data/lane/lane_"+str(lane["id"])+".json","w") as f:
                json.dump(lane,f)
    
