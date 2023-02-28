import time
import pymysql

db = pymysql.connect(host="124.70.94.252",
                     port=3306,
                     user="root",
                     password="123456",
                     database="tiaoshi"
                     )

ob = db.cursor(cursor=pymysql.cursors.DictCursor)



def fanhui(mouth):#计算月总收入
    sql_select = 'select * from pay_record where mouth = {} ;'.format(mouth)
    ob.execute(sql_select)
    res = ob.fetchall()
    total = 0
    for i in res:
        food = i['food_pay']
        buy_pay = i['buy_pay']
        big_pay = i['big_pay']
        pin_money = i['pin_money']
        life_pay = i['life_pay']
        total += food + buy_pay + big_pay + pin_money + life_pay
    return total


print(fanhui(2))





def fanhui1(year):#计算年总收入
    sql_select = 'select * from pay_record where year = {} ;'.format(year)
    ob.execute(sql_select)
    res = ob.fetchall()
    total = 0
    for i in res:
        food = i['food_pay']
        buy_pay = i['buy_pay']
        big_pay = i['big_pay']
        pin_money = i['pin_money']
        life_pay = i['life_pay']
        total += food + buy_pay + big_pay + pin_money + life_pay
    return total

print(fanhui1(2023))