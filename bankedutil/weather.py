import requests
import time
def wea():
    url = 'http://www.nmc.cn/rest/weather?stationid=54857&_=1661767501756'
    res = requests.get(url=url)

    weather  = res.json()['data']['real']['weather']['info']

    air = res.json()['data']['air']['text']

    tem=res.json()['data']['tempchart']

    wind = res.json()['data']['real']['wind']['power']


    for i in tem:
        if i['time']==time.strftime('%Y/%m/%d'):
            max_tem = i['max_temp']
            min_tem = i['min_temp']
            if '雨' in weather:
                result={'weather':weather,'air':air,'max_tem':max_tem,'min_tem':min_tem,'wind':wind}
            else:
                result = {'weather': weather, 'air': air, 'max_tem': max_tem, 'min_tem': min_tem,'wind':wind}
            return result


