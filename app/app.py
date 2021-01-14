import atexit
import requests
import time
import datetime

from apscheduler.scheduler import Scheduler
from flask import Flask, request, jsonify
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

@app.route('/', methods=["POST"])
def index():
    cur = mysql.connection.cursor()
    sql = '''SELECT * FROM candles'''
    content = request.get_json(silent=True)

    if content is not None:
        if 'moeda' in content:
            sql = sql + " WHERE moeda = '" + str(content['moeda']) + "'"

    cur.execute(sql)
    results = cur.fetchall()
    return jsonify(results)

@cron.interval_schedule(minutes=1, max_instances=2)
def job_function1():
    coin = 'BTC_XMR'
    interval = 1
    create_candle(coin, interval)

@cron.interval_schedule(minutes=5, max_instances=2)
def job_function5():
    coin = 'BTC_XMR'
    interval = 5
    create_candle(coin, interval)

@cron.interval_schedule(minutes=10, max_instances=2)
def job_function10():
    coin = 'BTC_XMR'
    interval = 10
    create_candle(coin, interval)  

def create_candle(coin, interval):
    now = datetime.datetime.utcnow()
    start = time.time()
    opened = 0
    closed = 0
    big = 0
    small = 0

    if coin == 'BTC_XMR':
        name = 'Bitcoin'


    while (time.time() - start) < (interval * 60):
       r = requests.get(url = 'https://poloniex.com/public?command=returnTicker') 
       data = r.json()[coin]
       if opened == 0:
           opened = Decimal(data['last'])
           small = Decimal(data['lowestAsk'])
       if big < Decimal(data['highestBid']):
           big = Decimal(data['highestBid'])
       if small > Decimal(data['lowestAsk']):
           small = Decimal(data['lowestAsk'])
    closed = Decimal(data['last'])

    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO candles VALUES (%s, %s, %s, %s, %s, %s, %s)''',(name, interval, now.strftime('%Y-%m-%d %H:%M:%S'), opened, small, big, closed))
        mysql.connection.commit()

atexit.register(lambda: cron.shutdown(wait=False))
