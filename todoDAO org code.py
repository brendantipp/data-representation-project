#this is doa.py


#deals with msqlconnector

#covert formats


import mysql.connector


class TodoDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",

        database="projectdb"
        )
        print ("Connection Made")
    



    def create(self, task):
        cursor = self.db.cursor()
        sql="insert into todo (TASKID, Title) task (%s,%s)"
        cursor.execute(sql, task)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from todo"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from todo where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update todo set TASKID= %s, Title=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()


    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from todo where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','name','age']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    


todoDAO = TodoDAO()