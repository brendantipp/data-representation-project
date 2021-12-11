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
        password="root",

        database="projectdb"
        )
        print ("Connection Made")
    



    def create(self, task):
        cursor = self.db.cursor()
        sql="insert into todo (Title, Category, Description, Priority, Status) values (%s,%s,%s,%s,%s)"
        values = [
            task['Title'],
            task['Category'],
            task['Description'],
            task['Priority'],
            task['Status']
            ]

        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    


todoDAO = TodoDAO()