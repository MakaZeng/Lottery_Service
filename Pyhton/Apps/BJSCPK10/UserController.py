#encoding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import Dao.MysqlDBConfig as DBC
import Dao.MysqlDBManager as DBM

def inertPersonWith(personID,name,device):
    sql = "insert into {0}({1},{2},{3},{4},{5},{6},{7}) values ({8},'{9}','{10}','{11}',{12},{13},'{14}')".format( \
        DBC.PSTAB,DBC.PSID,DBC.PSNAME,DBC.PSDEVICE,DBC.PSHEAD,DBC.PSLEVEL,DBC.PSMONEY,DBC.PSSTATUS, \
        personID,name,device,0,0,0,0)
    return DBM.maka_do_sql(sql)
