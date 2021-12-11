from todoDAO import todoDAO


task = {

'TASKID':1,
'Title':"First Task",
'Category':"College",
'Priority':"High",

}

returnvalue =todoDAO.create(task)
print(returnvalue)


