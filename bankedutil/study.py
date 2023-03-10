import time
import pymysql

db = pymysql.connect(host="124.70.94.252",
                     port=3306,
                     user="root",
                     password="123456",
                     database="tiaoshi"
                     )

ob = db.cursor(cursor=pymysql.cursors.DictCursor)

class studySq:

    def motion(self):
