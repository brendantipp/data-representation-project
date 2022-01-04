#this is server.py
#my restful API server
#maps urls to functions

#my required imports
from flask import Flask, jsonify, request, abort,render_template, session, url_for,redirect
from todoDAO import todoDAO
import messages


app = Flask(__name__, static_url_path='', static_folder='.')
#secret key for sessions
app.secret_key = 'someSecrtetasdrgsadfgsdfg3ko'

#https://pythonise.com/series/learning-flask/rendering-html-files-with-flask

#the following will open my index page on opening local host
@app.route('/')
def index():

    if not 'username' in session:
        return render_template("login.html")
    #this will take the user to the home page
    return render_template("index.html")

#login page
@app.route('/login')
def login():
    return render_template("login.html")

#process login page
@app.route('/processlogin')
def proccess_login():
    #check credentials if bad redirect to login page again
    #to be completed 
    #else
    session['username']="I dunno"
    #return redirect(url_for('home'))
    return render_template("index.html")

#process logout
@app.route('/logout')
def logout():
    session.pop('username',None)
    return render_template("login.html")

#process tasks page
#curl "http://127.0.0.1:5000/task"
@app.route('/task')
def getAll():
    if not 'username' in session:
        #abort(401)
        return render_template("login.html")
    else:
        #print("in getall")
        result = todoDAO.getAll()
        jsonify(result)
        return jsonify(result)

### this is for the gmail API
#curl "http://127.0.0.1:5000/gmail"
@app.route('/gmail')
def getAll2():
    if not 'username' in session:
        #abort(401)
        return render_template("login.html")
    else:
        #print("in getemails")
        result = todoDAO.getAll_email()
        return jsonify(result)
    
#process get task by ID
#curl "http://127.0.0.1:5000/task/37"
@app.route('/task/<int:ID>')
def findById(ID):
    if not 'username' in session:
        #abort(401)
        return render_template("login.html")
    else:
        foundtask = todoDAO.findByID(ID)
        return jsonify(foundtask)

#add a task
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


### create a new task
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

#delete a task
@app.route('/task/<int:ID>' , methods=['DELETE'])
def delete(ID):
    todoDAO.delete(ID)
    return jsonify({"done":True})

#main function
if __name__ == '__main__' :
    messages.main()
    app.run(debug= True)
    
    