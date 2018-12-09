from config import *
from os import remove as rm
import traceback

import sqlite3

import json
from requests import get, post
from pyquery import PyQuery as pq

def checkPrice(url, priceSelector, alias, pbToken=None):
    
    data = pq(url=url)
    price = data(priceSelector).text()
    try:
        conn = sqlite3.connect('%s'%(priceChecker_historyStore_SQLite_file))
        c = conn.cursor()
        c.execute("SELECT previous_value FROM history where alias = '%s'"%(alias))
        
        try:
            previous_value = c.fetchone()[0]

        except TypeError:
            previous_value = None
            print("[INFO] No previous price values was recorded for %s."%(alias))

        if previous_value != None:
            c.execute("UPDATE history SET previous_value = '%s' WHERE alias = '%s' "%(price, alias))
        else:
            c.execute("INSERT INTO history VALUES ('%s', '%s')"%(alias, price))
        
        conn.commit()
    

    except Exception as e:
        traceback.print_exc()

    finally:
        conn.close()
    
    if pbToken is not None:          

        r = post(
            url='https://api.pushbullet.com/v2/pushes',
            data=json.dumps({"body":"Current price is %s (previous price was %s)."%(price, previous_value),"title":alias, "type":"note"}),
            headers={"Access-Token": pbToken, "Content-Type": "application/json"}
        )

        if r.status_code != 200:
            raise Exception("PushBullet API error, status_code is %d", r.status_code)


def resetPriceChecker():

    try:
        conn = sqlite3.connect('%s'%(priceChecker_historyStore_SQLite_file))
        c = conn.cursor()
        c.execute("DROP TABLE history")
    except sqlite3.OperationalError :
        print("[INFO] history table does not exist. creating...")
    finally:
        c.execute("CREATE TABLE history(alias, previous_value)")
        conn.commit()
        conn.close()
        print("[INFO] history table has been recreated and is now ready.")
