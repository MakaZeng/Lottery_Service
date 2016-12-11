#encoding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import Network.NetworkManager as NM
import Dao.MysqlDBManager as DBM
import time
import MysqlDBConfig as CF
from pyquery import PyQuery as pyq


startNumber = 0
databaseStartNumber = 0
databaseStartNumber = 0
startNumber = 591461


currentNumber = startNumber

while 1 :
    url = 'http://www.bwlc.net/bulletin/prevtrax.html?num={0}'.format(currentNumber)
    content = NM.getcontent(url)
    if len(content):
        jq = pyq(content)
        content = jq('.tb td').text()
        arr = content.split(' ')

        qishu = arr[0]
        row = arr[1].split(',')
        shijian = arr[2] + ' ' + arr[3] + ':00'

        sql = "INSERT INTO {0} ({1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}) VALUES ( \
                    '{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}');".format( \
            CF.HISTAB, CF.HISQI, CF.HISTIME, CF.HISN1, CF.HISN2, CF.HISN3, CF.HISN4, CF.HISN5, CF.HISN6, CF.HISN7,
            CF.HISN8,
            CF.HISN9, CF.HISN10, \
            qishu, shijian, str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
            str(row[6]), str(row[7]), str(row[8]), str(row[9]))
        DBM.maka_do_sql(sql)
        print sql
        time.sleep(1)
        currentNumber -= 1

    else:
        time.sleep(10)