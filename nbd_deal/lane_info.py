#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lane_info.py
@Time    :   2022/04/20 12:24:04
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''

'''
lane 的具体信息
'''
central_curve={"segment":{"line_segment":{"points":[]},"s":0,"start_position":{},"heading":0,"length":0}}
left_boundary={"curve":{"segment":{"line_segment":{"points":[]},"s":0,"start_position":{},"heading":0,"length":0}},"length":0,"virtual":"","boundary_type":{"s":0,"types":""}}
right_boundary={"curve":{"segment":{"line_segment":{"points":[]},"s":0,"start_position":{},"heading":0,"length":0}},"length":0,"virtual":"","boundary_type":{"s":0,"types":""}}

lane={"name":"","id":"",
    "centrol_curve":central_curve,
    "left_boundary":left_boundary,
    "right_boundary":right_boundary,
    "length":0,
    "speed_limit":0,
    "overlap_id":[],
    "predecessor_id":[],
    "successor_id":"",
    "left_neighbor_forward_lane_id":[],
    "right_neighbor_forward_lane_id":"",
    "type":"",
    "turn":"",
    "left_neighbor_reverse_lane_id":"",
    "junction_id":"",
    "direction":"",
    "left_sample":[],
    "right_sample":[],
    "left_road_sample":[],
    "right_road_sample":[],
    }