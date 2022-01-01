#this is server.py

#maps urls to functionis

#keep as simple as possible

#similar to rest server week 8



from flask import Flask, jsonify, request, abort
from todoDAO import todoDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/task"
@app.route('/task')
def getAll():
    #print("in getall")
    result = todoDAO.getAll()
    return jsonify(result)
    #return jsonify(todoDAO.getAll())



#curl "http://127.0.0.1:5000/task/37"
@app.route('/task/<int:ID>')
def findById(ID):
    foundtask = todoDAO.findByID(ID)

    return jsonify(foundtask)



#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"BRENDAN ELLA\",\"Description\":\"UNITED\",\"Category\":\"ELLA\",\"Priority\":\"xHigh\",\"Status\":\"OPEN\"}" http://127.0.0.1:5000/task/79


@app.route('/task/<int:ID>', methods=['PUT'])
def update(ID):
    foundtask = todoDAO.findByID(ID)
    #print("found task")
    if not foundtask:
        #print("error1")
        abort(404)
    
    if not request.json:
        #print("error2")
        abort(400)
    reqJson = request.json
    
    if 'Title' in reqJson:
        foundtask['Title'] = reqJson['Title']
    if 'Description' in reqJson:
        foundtask['Description'] = reqJson['Description']
    if 'Category' in reqJson:
        foundtask['Category'] = reqJson['Category']
    if 'Priority' in reqJson:
        foundtask['Priority'] = reqJson['Priority']
    if 'Status' in reqJson:
        foundtask['Status'] = reqJson['Status']


    values = (foundtask['Title'],foundtask['Description'],foundtask['Category'],foundtask['Priority'],foundtask['Status'],foundtask['ID'])
    todoDAO.update(values)
    return jsonify(foundtask)
   
  


### create

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"create task\",\"Category\":\"tRIXIE\",\"Description\":\"dfdfdf\",\"Priority\":\"xHigh\",\"Status\":\"OPEN\"}" http://127.0.0.1:5000/task

@app.route('/task', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    task = {
        
        #"DateAdded":request.json['DateAdded'],
        "Title": request.json['Title'],
        "Category": request.json['Category'],
        "Description": request.json['Description'],
        "Priority": request.json['Priority'],
        "Status": request.json['Status']
        

    }


    #values = (task['Title'],task['Category'],task['Description'],task['Priority'],task['Status'])
    #newId = todoDAO.create(values)
    #task['ID'] = newId
    #return jsonify(task)
    return jsonify(todoDAO.create(task))



@app.route('/task/<int:ID>' , methods=['DELETE'])
def delete(ID):
    todoDAO.delete(ID)
    return jsonify({"done":True})



if __name__ == '__main__' :
    app.run(debug= True)