import Dao.MysqlDBManager as DBM
import MysqlDBConfig as DBC

def CreateTableHistoryIfNotEXist():
    createSql = "CREATE TABLE IF NOT EXISTS {0} ( \
    {1} VARCHAR(45) NOT NULL, \
    {2} DATETIME NULL, \
    {3} VARCHAR(45) NOT NULL, \
    {4} VARCHAR(45) NOT NULL, \
    {5} VARCHAR(45) NOT NULL, \
    {6} VARCHAR(45) NOT NULL, \
    {7} VARCHAR(45) NOT NULL, \
    {8} VARCHAR(45) NOT NULL, \
    {9} VARCHAR(45) NOT NULL, \
    {10} VARCHAR(45) NOT NULL, \
    {11} VARCHAR(45) NOT NULL, \
    {12} VARCHAR(45) NOT NULL, \
    PRIMARY KEY ({1}), \
    UNIQUE INDEX `{1}_UNIQUE` (`{1}` ASC)) \
    ENGINE = InnoDB \
    DEFAULT CHARACTER SET = utf8 \
    COLLATE = utf8_bin;".format(DBC.HISTAB,DBC.HISQI,DBC.HISTIME,DBC.HISN1,DBC.HISN2,DBC.HISN3,DBC.HISN4,DBC.HISN5,DBC.HISN6,DBC.HISN7,DBC.HISN8,DBC.HISN9,DBC.HISN10)
    DBM.maka_do_sql(createSql)

def CreateTableTongjiIfNotEXist():
    createSql = "CREATE TABLE IF NOT EXISTS {0} ( \
    {1} VARCHAR(45) NOT NULL, \
    {2} TEXT NOT NULL, \
    PRIMARY KEY ({1}), \
    UNIQUE INDEX `{1}_UNIQUE` (`{1}` ASC)) \
    ENGINE = InnoDB \
    DEFAULT CHARACTER SET = utf8 \
    COLLATE = utf8_bin;".format(DBC.TJTAB,DBC.TJQI,DBC.TJRS)
    DBM.maka_do_sql(createSql)

def CreateTablePersonIfNotEXist():
    createSql = "CREATE TABLE IF NOT EXISTS {0} ( \
    {1} BIGINT(10) NOT NULL AUTO_INCREMENT, \
    {2} VARCHAR(512) NOT NULL, \
    {3} VARCHAR(45) NOT NULL, \
    {4} VARCHAR(512) NOT NULL, \
    {5} VARCHAR(512) NOT NULL, \
    {6} BIGINT(10) NOT NULL, \
    {7} BIGINT(10) NOT NULL, \
    PRIMARY KEY ({1}), \
    UNIQUE INDEX `{1}_UNIQUE` (`{1}` ASC)) \
    ENGINE = InnoDB \
    DEFAULT CHARACTER SET = utf8 \
    COLLATE = utf8_bin;".format(DBC.PSTAB,DBC.PSID,DBC.PSDEVICE,DBC.PSSTATUS,DBC.PSHEAD,DBC.PSNAME,DBC.PSMONEY,DBC.PSLEVEL)
    DBM.maka_do_sql(createSql)

def CreateTableBeatListIfNotEXist():
    createSql = "CREATE TABLE IF NOT EXISTS {0} ( \
    {1} BIGINT(10) NOT NULL AUTO_INCREMENT, \
    {2} VARCHAR(45) NOT NULL, \
    {3} DATETIME NOT NULL, \
    {4} VARCHAR(45) NOT NULL, \
    {5} VARCHAR(45) NOT NULL, \
    {6} BIGINT(10) NOT NULL, \
    {7} INT NOT NULL, \
    {8} BIGINT(10) NOT NULL, \
    PRIMARY KEY ({1}), \
    UNIQUE INDEX `{1}_UNIQUE` (`{1}` ASC)) \
    ENGINE = InnoDB \
    DEFAULT CHARACTER SET = utf8 \
    COLLATE = utf8_bin;".format(DBC.BLTAB,DBC.BLID,DBC.BLQI,DBC.BLTIME,DBC.BLROAD,DBC.BLNUMBER,DBC.BLMONEY,DBC.BLSTATUS,DBC.BLPERSON)
    DBM.maka_do_sql(createSql)
