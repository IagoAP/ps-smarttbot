import atexit
import requests
import time

from apscheduler.scheduler import Scheduler
from flask import Flask
from flask_mysqldb import MySQL
from decimal import Decimal

app = Flask(__name__)

cron = Scheduler(daemon=True)
cron.start()

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = '172.33.0.101'
app.config['MYSQL_DB'] = 'smarttbot'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

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
       if opened == 0:
           opened = Decimal(data['last'])
           small = Decimal(data['lowestAsk'])
       if big < Decimal(data['highestBid']):
           big = Decimal(data['highestBid'])
       if small > Decimal(data['lowestAsk']):
           small = Decimal(data['lowestAsk'])
    closed = Decimal(data['last'])

    print(opened, closed, big, small)


atexit.register(lambda: cron.shutdown(wait=False))
