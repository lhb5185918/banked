import time
import pymysql

db = pymysql.connect(host="124.70.94.252",
                     port=3306,
                     user="root",
                     password="123456",
                     database="tiaoshi"
                     )

ob = db.cursor(cursor=pymysql.cursors.DictCursor)


class financialCalculation:
    def money(self, food, buy, big, pin, life):
        time_res = time.strftime("%Y%m%d")
        time_year = time.strftime("%Y")
        mouth = time.strftime("%m")
        sql_insert = 'INSERT into  pay_record (timeid,year,mouth,food_pay,buy_pay,big_pay,pin_money,life_pay) VALUES ({},{},{},{},{},{},{},{});'.format(
            time_res, time_year, mouth, food, buy, big, pin, life)
        sqlRes = ob.execute(sql_insert)
        sql_result = 'select timeid from pay_record where timeid = {};'.format(time_res)
        sqlcarry = ob.execute(sql_result)
        sqlRESult = ob.fetchone()
        res = None
        if int(sqlRESult['timeid']) == int(time_res):
            res = '操作成功'
        else:
            res = '操作失败'
        db.commit()
        return res

    def mouthFinancial(self, mouth):  # 计算月总收入
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

    def yearFinancial(self, year):  # 计算年总收入
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




