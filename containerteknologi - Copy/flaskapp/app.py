
from pydoc import doc
from time import sleep
from typing import List, Dict
import json
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'peoples'

mysql = MySQL(app)  
 
#Creating a connection cursor
cursor = mysql.connection.cursor()

def peeps():
    cursor.execute('SELECT * FROM peeps')
    results = [{name: age} for (name, age) in cursor]

    return json.dumps(results)

def insertperson(data):
    try:
        cursor.execute("INSERT INTO peeps (name,age) VALUES (%s,%s)",(data['name'], data['age']))
        mysql.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False

@app.route('/persons', methods = ['GET'])
def index():
    return peeps()

@app.route('/persons', methods = ['POST'])
def insert():
    if insertperson(request.json):
        return "Insert OK"
    else:
        return "Insert FAILED"

if __name__ == '__main__':
    app.run(host='0.0.0.0')