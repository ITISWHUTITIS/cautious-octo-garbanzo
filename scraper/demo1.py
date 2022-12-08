#Copy data into postgres DB table (demo2)
import psycopg2


#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='yourpassword', port='5432')


conn.autocommit = True
cursor = conn.cursor()


sql = '''COPY demo2(name,price,\
discount,link,date_extract)
FROM 'C:/Users/64437/Desktop/ADE/PYTHON/results.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql)

sql2 = '''select * from demo2;'''
cursor.execute(sql2)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()

#(r'C:\Users\64437\Desktop\ADE\PYTHON\results.csv')
