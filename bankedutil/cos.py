# -*- coding=utf-8

from qcloud_cos import CosConfig

from qcloud_cos import CosS3Client

import sys

import os

import logging

import requests

from config.configset import secret_id,secret_key



class getCos:

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    regoin = 'ap-beijing'

    token = None

    scheme = 'https'

    config = CosConfig(Region=regoin, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
    client = CosS3Client(config)

    def getPicture(self,filename):
        pictres = self.client.list_objects(Bucket='ourpicture-1304179902')

        for i in pictres['Contents']:
            if filename ==i['Key'] :
                url = 'https://ourpicture-1304179902.cos.ap-beijing.myqcloud.com/{}'.format(filename)
                return url

    def getWeatherPicture(self):
        url ='http://www.nmc.cn/rest/weather?stationid=54857&_=1677225812209'
        res  = requests.get(url =url)
        weather = res.json()['data']['real']['weather']['info']
        result = ''
        if weather == '晴':
            result = self.getPicture(filename='son')
        elif '雨'in weather:
            result = self.getPicture(filename='rain')

        return result



