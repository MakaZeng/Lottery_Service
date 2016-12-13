#encoding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import Dao.MysqlDBManager as DBM
import MysqlDBConfig as DBC
import random
import time
import Util.DateUtil as DU
import DatabaseCreator as CREATOR
import UserController as UserController


class Yuce(object):
    def __init__(self):
        super(Yuce, self).__init__()

    def startYuce(self):

        CREATOR.CreateTablePersonIfNotEXist()
        CREATOR.CreateTableBeatListIfNotEXist()

        sql = "select {0} from {1} order by {0} DESC limit 1".format(DBC.HISQI,DBC.HISTAB)
        result = DBM.maka_do_sql(sql)
        qishu = result[0][0]

        persons = [100,101,102,103,104,105,106,107,108,109]
        names = ["菜鸟计划","山神计划","盖伦计划","宝贝计划","二狗计划","老马计划","必赢计划","莎莎计划","李仙人计划","白小姐计划"]

        self.calculateHistoryYuce()
        for person in persons:
            self.getTouzhuForPerson(person,names[person - 100],qishu)

    def calculateHistoryYuce(self):
        print '===============>进行历史数据结算<=================='
        sql = "select {0},{1},{2},{3},{4},{5} from {6} where {7} = 0;".format(DBC.BLID,DBC.BLROAD,DBC.BLNUMBER,DBC.BLMONEY,DBC.BLPERSON,DBC.BLQI,DBC.BLTAB,DBC.BLSTATUS)
        result = DBM.maka_do_sql(sql)
        if not result:
            print '^^^^^^^^^^^^^^^^^^^^结算完成^^^^^^^^^^^^^^^^^^^^^^^^^'
            return
        for line in result:
            road = int(line[1])
            numbers = line[2]
            beat = line[3]
            id = line[0]
            person = line[4]
            qishu = line[5]
            sql = "select * from {0} where {1} = '{2}';".format(DBC.HISTAB,DBC.HISQI,qishu)
            result = DBM.maka_do_sql(sql)
            result = result[0]
            his = [result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11]]
            target = his[road-1]
            isIn = 2
            for n in numbers.split(','):
                if n==target:
                    isIn = 1
            sql = "update {2} set status = {0} where id = {1};".format(isIn,id,DBC.BLTAB)
            DBM.maka_do_sql(sql)
            print sql
        print '^^^^^^^^^^^^^^^^^^^^结算完成^^^^^^^^^^^^^^^^^^^^^^^^^'


    def getTouzhuForPerson(self,person,name,qishu):
        sql = "select * from {0} where {1} = {2};".format(DBC.PSTAB,DBC.PSID,person)
        result = DBM.maka_do_sql(sql)
        if not result:
            result = UserController.inertPersonWith(person, name, name)
            print '~~~~~~~~~~~~~~~~~~ 插入用户 ~~~~~~~~~~~~~~~~~~~~~~'
        else:
            tuple = result[0]
            touzhu = self.getRandom()

            currentTime = long(time.time())
            currentTime = DU.time_to_date(currentTime)

            numbers = touzhu['numbers']
            numbers = ','.join(numbers)

            sql = "insert into {0} ({1},{2},{3},{4},{5},{6},{7}) values ('{8}','{9}','{10}','{11}',{12},{13},{14})" \
            .format(DBC.BLTAB,DBC.BLQI,DBC.BLTIME,DBC.BLROAD,DBC.BLNUMBER,DBC.BLMONEY,DBC.BLSTATUS,DBC.BLPERSON, \
            qishu,currentTime,str(touzhu['road']),numbers,touzhu['beat'],0,person)
            DBM.maka_do_sql(sql)
            print '用户预测完成------------------------------------'


    def getRandom(self):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        roads = [1, 2, 3, 4, 5]
        beats = [100, 200, 500, 1000, 2000]
        random.shuffle(numbers)
        random.shuffle(roads)
        random.shuffle(beats)
        random.seed(time.time())
        return {'numbers':numbers[0:random.randint(3,5)],'road':roads[0],'beat':beats[0]}
