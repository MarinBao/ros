#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   overlap_deal.py
@Time    :   2022/04/21 14:48:18
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''


import re
from common_use import *
import json
import os.path as path



def overlap_deal(overlap_infos):
    overlaps={"overlap":[]}
    a,b,c=1,2,3
    A,B,C=0,0,0
    # print(overlap_infos[2])
    for overlap in overlap_infos:
        overlap_inf={"name":"","id":"","object_1":{"id":""},"object_2":{"id":"","lane_overlap_info":{"start_s":0,"end_s":0}},"object_3":{"id":""},}
        overlap_inf["name"]="overlap"
        overlap_inf["id"]=re.search(r"id:\"(.*?)\"}",overlap).group(1)

        object_data=overlap[overlap.find("object"):].split("object")
        object_data.remove("")
        
        for i in range(len(object_data)):
            id=re.search(r"id:\"(.*?)\"}",object_data[i]).group(1)
            # print(id[0],id[1])
            if id[0]=="j":
                overlap_inf["object_1"]["id"]=id

            elif id[0]=="l":
                overlap_inf["object_2"]["id"]=id
                overlap_inf["object_2"]["lane_overlap_info"]["start_s"]=re.search("start_s:(.*?)end",object_data[i]).group(1)
                overlap_inf["object_2"]["lane_overlap_info"]["end_s"]=re.search("end_s:(.*?)}",object_data[i]).group(1)

            elif id[0]=="c":
                overlap_inf["object_3"]["id"]=id

        overlaps["overlap"].append(overlap_inf)

    
    with open("Data/overlap.json","w",encoding="utf-8") as f:
        json.dump(overlaps,f)

        #检查几个object
    #     a,b,c=1,2,3
    #     if len(re.findall(r"object",overlap))==a:
    #         A+=1
    #     if len(re.findall(r"object",overlap))==b:
    #         B+=1
    #     if len(re.findall(r"object",overlap))==c:
    #         C+=1
    # print("A",A,"B",B,"C",C)