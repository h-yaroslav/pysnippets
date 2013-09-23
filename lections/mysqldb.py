#!/usr/bin/python
import MySQLdb
try:
    conn = MySQLdb.connect(                                                                                                                                                         
        host='rv030.softservecom.com',                                                                                                                                      
        user='ygrabar', passwd='fh84Mysql', db='mysite_1_db')                                                                                                                          
    curs = conn.cursor(MySQLdb.cursors.DictCursor)                                                                                                                                  
    ##query = 'delete from polls_poll where id=5'                                                                                                                                       
    query = 'select * from polls_choice'                                                                                                                                       
    conn.query(query)
    rows = conn.store_result()
    print rows.num_rows()
    while True:
        i = rows.fetch_row()
        print "! ROWS:", i
        if not i:
            break
    curs.execute(query)                                                                                                                                                             
    rows = curs.fetchall()                                                                                                                                                          
    print "# ROWS:", rows
except Exception, e:
    print "!!!", str(e)
finally:
    curs.close()                                                                                                                                                                    
    conn.close()       
