from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

print("CU")

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = '172.23.0.2'
app.config['MYSQL_DB'] = 'smarttbot'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    
    cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20))''')

    return 'Done!'

