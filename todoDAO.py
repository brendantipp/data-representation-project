#this is doa.py


#deals with msqlconnector

#covert formats


import mysql.connector
from datetime import datetime
#now = datetime.now()

class TodoDAO:
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

    def create(self, task):
        cursor = self.db.cursor()
        sql="insert into todo (DateAdded,Title, Category, Description, Priority, Status) values (now(),%s,%s,%s,%s,%s)"
        values = [
            #task['DateAdded'],
            task['Title'],
            task['Category'],
            task['Description'],
            task['Priority'],
            task['Status']
            ]

        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

## return all records

    def getAll(self):
        cursor = self.db.cursor()
        ##look at formatting date return
        sql="select * from todo"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        ##look at converting to json later
        #sanity check
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

#function to find a task by id

    def findByID(self, TASKID):
        cursor = self.db.cursor()
        sql="select * from todo where TASKID = %s"
        values = [TASKID]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)
        #return {}


#function to update

    def update(self, task):
        cursor = self.db.cursor()
        sql="update todo set Category= %s, Priority= %s, Status = %s  where TASKID = %s "
        values = [
            task['Category'],
            task['Priority'],
            task['Status'],
            task['TASKID']
            ]
        cursor.execute(sql, values)
        self.db.commit()
        return task




#function to delete

    def delete(self, TASKID):
        cursor = self.db.cursor()
        sql="delete from todo where TASKID = %s"
        values = [TASKID]
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
        return {}




#function to covert to dictionary

    def convertToDictionary(self, result):
        colnames=['TASKID','DateAdded','Title','Description','Category','Priority', 'Status','DeadlineDate']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    


todoDAO = TodoDAO()