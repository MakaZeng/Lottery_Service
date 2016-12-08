import MySQLdb

Host = 'localhost'
Port = 3306
Name = 'root'
Password = 'root'
Database = 'lottery'


def maka_do_sql(sql):
    try:
        conn = MySQLdb.connect(host=Host, user=Name, passwd=Password, port=Port, charset='utf8')
        cur = conn.cursor()
        conn.select_db(Database)
        result = cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result
    except MySQLdb.Error, e:
        print "maka_do_sql mysql Error %d: %s" % (e.args[0], e.args[1])