import datetime
import mysql.connector
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# connecting to MySQL using connector/python
cnx = mysql.connector.connect(user='root',password='root',database='world')


# query data from mysql database
cursor = cnx.cursor(buffered=True)

query = ("SELECT Name, Population as pop FROM city "
         "WHERE CountryCode = 'CHN' ")

# code = 'CHN'

cursor.execute(query)

print 'Name \t Population'
for (Name, Population) in cursor:
    print '%s \t\t %d' % (Name, Population)


cursor.close()
cnx.close()
