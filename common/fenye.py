# -*- coding: utf-8 -*-
# @Date    : 2017-07-02 19:12:04
# @Author  : lileilei
def list_qiepian(list,split):
    if len(list)<=split:
        return list
    me=len(list)//split
    New_list=[]
    for i in range(me):
        New_list.append(list[(i)*split:(i+1)*split])
    if len(list[me*split:])>0:
        New_list.append(list[me*split:])
    return New_list

