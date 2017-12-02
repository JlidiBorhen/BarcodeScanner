import json
import urllib
import time
import dbc

def update() :

	while True:
		url = "http://192.168.1.29/phps/broadcast.php"
		response = urllib.urlopen(url)
		data = response.read().decode("utf-8")
		dec=json.loads(data)
		for k in dec:
			try:
				dbc.cur.execute("INSERT INTO clients (id,firstname,lastname,barcode,checkedin,sync) VALUES (%s,'%s','%s','%s',0,1)" % (str(k['id']),str(k['firstname']),str(k['lastname']),str(k['barcode'])))
				dbc.dbcon.commit()
			except:
				dbc.dbcon.rollback()
		time.sleep(10)
