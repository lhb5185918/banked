# -*- coding=utf-8

from qcloud_cos import CosConfig

from qcloud_cos import CosS3Client

import sys

import os

import logging

from config.configset import secret_id,secret_key

#打印日志

logging.basicConfig(level=logging.INFO,stream=sys.stdout)

regoin = 'ap-beijing'


token = None

scheme = 'https'

config = CosConfig(Region=regoin,SecretId=secret_id,SecretKey=secret_key,Token=token,Scheme=scheme)
client = CosS3Client(config)

url = 'https://ourpicture-1304179902.cos.ap-beijing.myqcloud.com/'



pictres = client.list_objects(Bucket='ourpicture-1304179902')
filename = 'picture4'

# def getPicture(filename):
#     resSelect = client.list_buckets()['Bucket']
for i in pictres['Contents']:
    if filename ==i :
        url = 'https://ourpicture-1304179902.cos.ap-beijing.myqcloud.com/'+i+".jpg"
        print('ture')
    else: print('false')



