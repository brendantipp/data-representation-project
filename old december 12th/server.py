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

#curl "http://127.0.0.1:5000/todo"
@app.route('/todo')
def getAll():
    #print("in getall")
    result = todoDAO.getAll()
    return jsonify(result)
    #return jsonify(todoDAO.getAll())



#curl "http://127.0.0.1:5000/todo/7"
@app.route('/todo/<int:TASKID>')
def findById(TASKID):
    foundtask = todoDAO.findByID(TASKID)

    return jsonify(foundtask)



#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Category\":\"ella\",\"Priority\":\"xHigh\",\"Status\":\"OPEN\"}" http://127.0.0.1:5000/todo/3


@app.route('/todo/<int:TASKID>', methods=['PUT'])
def update(TASKID):
    foundtask = todoDAO.findByID(TASKID)
    print("found book")
    if not foundtask:
       # print("error1")
        abort(404)
    
    if not request.json:
        #print("error2")
        abort(400)
    reqJson = request.json
    print(reqJson)

 
    if 'Category' in reqJson:
        foundtask['Category'] = reqJson['Category']
    if 'Priority' in reqJson:
        foundtask['Priority'] = reqJson['Priority']
    if 'Status' in reqJson:
        foundtask['Status'] = reqJson['Status']
    if 'TASKID' in reqJson:
        foundtask['TASKID'] = reqJson['TASKID']
        
    values = (foundtask['Category'],foundtask['Priority'],foundtask['Status'])
    todoDAO.update2(values,TASKID)
    return jsonify(foundtask)


### create

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"create task\",\"Category\":\"ella\",\"Description\":\"dfdfdf\",\"Priority\":\"xHigh\",\"Status\":\"OPEN\"}" http://127.0.0.1:5000/todo

@app.route('/todo', methods=['POST'])
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
        "Status": request.json['Status'],

    }


    values = (task['Title'],task['Category'],task['Description'],task['Priority'],task['Status'])
    #newId = todoDAO.create(values)
    #task['TASKID'] = newId
    #return jsonify(task)
    return jsonify(todoDAO.create(task))



@app.route('/todo/<int:id>' , methods=['DELETE'])
def delete(TASKID):
    todoDAO.delete(TASKID)
    return jsonify({"done":True})



if __name__ == '__main__' :
    app.run(debug= True)