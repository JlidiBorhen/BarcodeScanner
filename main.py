#!/usr/bin/python

from threading import  Thread
import scanner
import dbc
import lcd
import sync


dbc.connectDB()
cur=dbc.cur;
lcd.writeLCD('Willkommen','Welcome')


try :
	tsync=Thread(target=sync.update,args=())
	tscan=Thread(target=scanner.scan,args=())
	tsync.start()
	tscan.start()

	print "Scanning..."
except:
	print "Error: unable to start thread"



while 1:
	pass
