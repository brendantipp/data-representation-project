from todoDAO import todoDAO



task = {



'Title':"First Task",
'Description':'Get project done',
'Category':"College",
'Priority':"High",
'Status':"Open"

}


task2 = {

'TASKID':2,
'Category':"Home",
'Priority':"XLow",
'Status':"Closed"

}



task3 = {



'Title':"Third Task",
'Description':'Drinking',
'Category':"Home",
'Priority':"High",
'Status':"Open",

}

task4 = {


    'TASKID':2,
   'Status':"Open",
}


task5 = {

'TASKID':2,


}


#testing the create a new task
#returnvalue =todoDAO.create(task)

#testing the get all 
#returnValue = todoDAO.getAll()
#print(returnValue)

#testing find by id 
#returnValue = todoDAO.findByID(task4['TASKID'])
#print(returnValue)


#testing update
#returnValue = todoDAO.update(task2)
#print(returnValue)



#testing delete
returnValue = todoDAO.delete(task5['TASKID'])
print(returnValue)