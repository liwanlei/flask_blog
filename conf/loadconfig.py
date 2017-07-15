# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 20:30:38
# @Author  : lileilei
import os
def lod_config():
    '''加载配置'''
    mode=os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            from .config import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from .config import testconfig
            return testconfig
        else:
            from .config import devconfig
            return devconfig
    except ImportError as e:
        print('加载配置失败原因:%s'%e)