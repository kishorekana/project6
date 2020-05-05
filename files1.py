# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:47:32 2018

@author: Cherukuri Amul
"""
#Task:1(Writing data into file using iteration)
#list=['\n car1,\t','lamborghini \n','car2,\t','mclaren \n']
#f=open("F:/python/files1.csv",'a')
#for i in list:
#    f.write(i)
#f.close()
#-------------------------------------------------------
#task:2(Writing data into file using input method)
#a=input("Insert an element")
#f=open("F:/python/files1234.csv",'w')
#f.write(a)
#f.close()
#------------------------------------------------------------------

#Task:3(accessing the xlxs file(openpyxl))
#from openpyxl import Workbook
#wb = Workbook()
#ws = wb.active
#ws['A1'] = 42
#
#
#wb.save("‪info.xlsx")


#from openpyxl import load_workbook
#wb = load_workbook(filename = '‪info.xlsx')
#
#print(wb)
#----------------------------------------------------------------



#task:4(loading data from flat file into list and then loading that data into database by skipping one element)

#import mysql.connector
#import csv
#mydb=mysql.connector.connect(user='root',host='localhost',password='amul7155',db='db1')
#csv_data=csv.reader(open('C:/Users/Cherukuri Amul/Desktop/Book1.csv'))
#cursor=mydb.cursor()
#list=[]
#for i in csv_data:
#    list.append(i)
#print(list)
##lists=['1','dlp','kphb'],['2','raj','kphb']
#for j in list:
##    print(j)
#    if j[0]!='101':
#        print(j)
#        (id,name,email)=j
#        sql="insert into students(id,name,email) values ('%s','%s','%s')"%\
#            (id,name,email)
#        cursor.execute(sql)
#cursor.execute("select * from students")
#print(cursor.fetchall())
#mydb.commit()
#mydb.close()






#---------------------------------------------------------------------------
#task:5(flat file into database)

#---------every thing is atken as string when taken in csv format--------
##import mysql.connector
import csv
mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='db1')
csv_data=csv.reader(open('‪F:\python\emp1.csv'))
print(type(csv_data))
cursor=mydb.cursor()
for line in csv_data:
    if(emp_id!=2):
        
        (emp_id,emp_name,emp_email)=line #---stored procedure attributes should be given-------
        print(type(line))
        print(emp_id,emp_name,emp_email)
        sql="insert into employees1(emp_id,emp_name,emp_email) values ('%s','%s','%s')"%\
             (emp_id,emp_name,emp_email) #----first attributes are table attributes and second attributes are stored procedure attributes---
    cursor.execute(sql)
cursor.execute("select * from employees")
print(cursor.fetchall())
mydb.commit()


