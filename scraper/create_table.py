#Create table into postgres DB
import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='Abc1234$', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS DEMO2")

#Creating table as per requirement
sql ='''CREATE TABLE DEMO2(
   NAME VARCHAR(255),
   PRICE VARCHAR(35),
   DISCOUNT VARCHAR(25),
   LINK VARCHAR(255),
   DATE_EXTRACT DATE
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()