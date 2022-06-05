import json
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'mysql' #use 127.0.0.1 when not in another container
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Passw0rd!'
app.config['MYSQL_DB'] = 'peoples'
#app.config['MYSQL_PORT'] = 3338 - only used when connecting on host

mysql = MySQL(app)  

def peeps():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT name, age FROM peeps')
    results = [{name: age} for (name, age) in cursor]

    return json.dumps(results)

def insertperson(data):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO peeps (name,age) VALUES (%s,%s);",(data['name'], data['age']))
        mysql.connection.commit()
        return 'INSERT OK'
    except Exception as e:
        return "Problem inserting into db: " + str(e)
        

@app.route('/persons', methods = ['GET'])
def index():
    return peeps()

@app.route('/persons', methods = ['POST'])
def insert():
    return insertperson(request.json)

if __name__ == '__main__':
    app.run(host='0.0.0.0')