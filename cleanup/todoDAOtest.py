from todoDAO import todoDAO



task = {

'Title':"NEW XMAS FILM TEST",
'Description':'NEED WINE',
'Category':"College",
'Priority':"High",
'Status':"Open",
'ID':79,

}





task3 = {



'Title':"Third Task",
'Description':'Drinking',
'Category':"Home",
'Priority':"High",
'Status':"Open",

}

task4 = {


   'ID':79,
   'Status':"Open",
}


task5 = {

'ID':1,


}


#testing the create a new task
#returnvalue =todoDAO.create(task)

#testing the get all 
#returnValue = todoDAO.getAll()
#print(returnValue)

#testing find by id 
#returnValue = todoDAO.findByID(79)
#print(returnValue)


#testing update
#print(task)
returnValue = todoDAO.update(task)
print(returnValue)

#testing delete
#returnValue = todoDAO.delete(task5['ID'])
#print(returnValue)