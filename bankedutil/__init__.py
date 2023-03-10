import time
import pymysql

db = pymysql.connect(host="124.70.94.252",
                     port=3306,
                     user="root",
                     password="123456",
                     database="tiaoshi"
                     )

ob = db.cursor(cursor=pymysql.cursors.DictCursor)


time_res = time.strftime("%Y%m%d")
time_year = time.strftime("%Y")
mouth     = time.strftime("%m")
sql_insert = 'INSERT into  pay_record (timeid,year,mouth,food_pay,buy_pay,big_pay,pin_money,life_pay) VALUES ({},{},{},{},{},{},{},{});'.format(time_res,time_year,mouth,1,1,1,1,1)
sqlRes = ob.execute(sql_insert)
sql_result = 'select timeid from pay_record where timeid = {};'.format(time_res)
sqlcarry = ob.execute(sql_result)
sqlRESult = ob.fetchone()
print(sqlRESult)
db.commit()
print(sqlRESult['timeid'])
print(type(int(sqlRESult['timeid'])))

