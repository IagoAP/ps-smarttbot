import atexit
import requests
import time

from apscheduler.scheduler import Scheduler
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

cron = Scheduler(daemon=True)
cron.start()

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = '172.23.0.2'
app.config['MYSQL_DB'] = 'smart'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    
    cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20))''')

    return 'Done!'

@cron.interval_schedule(minutes=1)
def job_function():

    start = time.time()
    opened = 0
    closed = 0
    big = 0
    small = 0


    while (time.time() - start) < 60:
        r = requests.get(url = 'https://poloniex.com/public?command=returnTicker') 
        data = r.json()['BTC_XMR']
        data = {unicode(k).encode('ascii'): unicode(v).encode('ascii') for k, v in data.iteritems()}
        if opened == 0:
            opened = data['last']
            small = data['lowestAsk']
        if big < data['highestBid']:
            big = data['highestBid']
        if small > data['lowestAsk']:
            small = data['lowestAsk']
    closed = data['last']

    print(opened, closed, big, small)


atexit.register(lambda: cron.shutdown(wait=False))
