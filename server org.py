#this is server.py

#maps urls to functionis

#keep as simple as possible

#similar to rest server week 8



from flask import Flask, jsonify, request, abort
from todoDAO import todoDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/todo"
@app.route('/todo')
def getAll():
    #print("in getall")
    results = todoDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/todo/2"
@app.route('/books/<int:id>')
def findById(TASKID):
    foundBook = todoDAO.findByID(TASKID)

    return jsonify(foundBook)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/todo

@app.route('/todo', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    book = {
        #"TASKID":nextId,
        "Title": request.json['Title'],
        "Category": request.json['Category'],
        "Description": request.json['Description'],
        "Priority": request.json['Priority'],
        "Status": request.json['Status'],

    }


    values =(book['Title'],book['Author'],book['Price'])
    newId = bookDAO.create(values)
    book['id'] = newId
    return jsonify(book)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(TASKID):
    foundtask = todoDAO.findByID(TASKID)
    if not foundtask:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    #if 'Price' in reqJson and type(reqJson['Price']) is not int:
        #abort(400)

    if 'Category' in reqJson:
        foundtask['Category'] = reqJson['Category']
    if 'Priority' in reqJson:
        foundtask['Priority'] = reqJson['Priority']
    if 'Status' in reqJson:
        foundtask['Status'] = reqJson['Status']
    
    
    values = (foundtask['Category'],foundtask['Priority'],foundtask['Status'])
    todoDAO.update(values)
    return jsonify(foundtask)
        

    

@app.route('/books/<int:TASKID>' , methods=['DELETE'])
def delete(TASKID):
    bookDAO.delete(TASKID)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)