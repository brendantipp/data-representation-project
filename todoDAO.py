#this is todpdoa.py
#deals with msqlconnector
#convert formats
import csv

import mysql.connector

from datetime import datetime
#now = datetime.now()

class todoDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",

        database="projectdb"
        )
        print ("Connection Made")
    

### create new record

    def create(self,task):
        cursor = self.db.cursor()
        sql="insert into todo (DateAdded,Title, Description, Category, Priority, Status) values (now(),%s,%s,%s,%s,%s)"
        
        values = [
            #task['DateAdded'],
            task['Title'],
            task['Description'],
            task['Category'],
            task['Priority'],
            task['Status'],
            
        ]

        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

## function to update records

    def update(self,values):
        cursor = self.db.cursor()
        
        sql="update todo set Title = %s, Description =%s, Category= %s, Priority= %s, Status = %s where ID = %s"
        
           
        cursor.execute(sql,values)
        self.db.commit()


## function to return all records

    def getAll(self):
        cursor = self.db.cursor()
        ##look at formatting date return
        sql="select * from todo"
        cursor.execute(sql)
        results = cursor.fetchall()
        #return results
        returnArray = []
        #print(results)
        ##look at converting to json later
        #sanity check
        for result in results:
           # print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def getAll_email(self):
        
        file = open("emails.csv")
        #file = open("aMessage.json")
        csvreader = csv.reader(file)
        next(csvreader)
        #header = next(csvreader)
        #print(header)
        rows = []
        for row in csvreader:
            #rows.append(row)
            rows.append(self.convertToDictionary2(row))
        return rows
        #file.close()


#function to find a task by id

    def findByID(self,ID):
        cursor = self.db.cursor()
        sql="select * from todo where ID = %s"
        values = [ID]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)
        #return {}


#function to delete

    def delete(self,ID):
        cursor = self.db.cursor()
        sql="delete from todo where ID = %s"
        values = [ID]
        cursor.execute(sql, values)
        #cursor.execute(sql)
        self.db.commit()
        print("delete done")
        #return


    def delete2(self,ID):
        cursor = self.db.cursor()
        sql="delete from todo where ID = %s"
        values = [ID]

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")



#function to covert to dictionary

    def convertToDictionary(self, result):
        colnames=['ID','DateAdded','Title','Description','Category','Priority', 'Status']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

    def convertToDictionary2(self, result):
        colnames=['ID','DateReceived','From','Subject','Email_Snippet']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
  
todoDAO = todoDAO()