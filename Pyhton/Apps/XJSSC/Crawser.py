#encoding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import Network.NetworkManager as NM
import Dao.MysqlDBManager as DBM

import MysqlDBConfig as CF
import DatabaseCreator as DBC
import sys
import time
import re
import json
import Util.DateUtil as DU
import demjson


crawser_url = "http://www.cp098.com/xjssc/getHistoryData?count=1&t=0.5354527991439386"

class Crawser(object):
    def __init__(self):
        super(Crawser, self).__init__()

    #判断是否需要抓取
    def judge_need_crawser(self):
        return 1

    def crawser_index(self):
        DBC.CreateTableHistoryIfNotEXist()
        if self.judge_need_crawser() == 1 :
            result = NM.web_getcontent(crawser_url)
            sss = json.loads(result)
            rows = sss['rows']
            row = rows[0]

            time = row['lotteryTime'][:16]
            numbers = str(row['n1']) + ',' + str(row['n2']) + ',' + str(row['n3']) + ',' + str(row['n4']) + ',' + str(
                row['n5'])
            qishu = row['termNum']

            sql = "INSERT INTO {0} ({1},{2},{3},{4},{5},{6},{7}) VALUES ( \
                                    '{8}','{9}',{10},{11},{12},{13},{14});".format( \
                CF.HISTAB, CF.HISQI, CF.HISTIME, CF.HISN1, CF.HISN2, CF.HISN3, CF.HISN4, CF.HISN5, \
                qishu, time, str(row['n1']), str(row['n2']), str(row['n3']), str(row['n4']), str(row['n5']))
            DBM.maka_do_sql(sql)