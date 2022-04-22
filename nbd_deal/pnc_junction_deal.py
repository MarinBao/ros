#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pnc_junction_deal.py
@Time    :   2022/04/21 22:56:02
@Author  :   Bao Mingxi 
@Version :   1.0
@Contact :   baomx1314@163.com
'''


from distutils.filelist import findall
import re
from common_use import *
import json
import os.path as path



def pnc_junction_deal(pnc_junction_infos):


    pnc_junction_Info={"pnc_junction":[]}
    for data in pnc_junction_infos:
        pnc_junction={"name":"","id":"","polygon":{"points":[]},"overlap_id":[]}
        pnc_junction["name"]="pnc_junction"
        pnc_junction["id"]=re.search(r"id:\"(.*?)\"}",data).group(1)

        pnc_junction["polygon"]["points"]=common_get_points(re.findall(r"point{(.*?)}",data))
        
        try:
            pnc_junction["overlap_id"]=re.findall(r"id:\"(.*?)\"}",data[data.find("overlap_id"):])
        except:
            pass       
        
        pnc_junction_Info["pnc_junction"].append(pnc_junction)

    with open("Data/pnc_junction.json","w",encoding="utf-8") as f:
        json.dump(pnc_junction_Info,f)








