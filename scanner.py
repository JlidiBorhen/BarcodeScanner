import os
import lcd
import dbc

rows = ('','','','')
def scan():
	n=0
	barcode=" "
	nums=['0','1','2','3','4','5','6','7','8','9']
	dev = os.open("/dev/usb/hiddev0", os.O_RDONLY)
	os.lseek(dev,0,os.SEEK_SET)
	while True:
		rawcode=os.read(dev,25)

		if rawcode.find(';')!=-1 :
			lcd.lcd.clear()
			rawcode=os.read(dev,127)
			for ch in rawcode :
				if ch in nums :
					barcode +=ch
			barcode =  barcode[2:]
			lcd.refresh();
			cur=dbc.cur
			cur.execute("SELECT * FROM clients")
			output=cur.fetchall()
			for a in output:
			        if a[3]==barcode:
					n=1
					if a[4]==0 :
						cur.execute("UPDATE clients SET checkedin=1 WHERE checkedin=0 AND barcode=%s" %(str(barcode)))
						dbc.dbcon.commit()
						print a[2]+": exists and allowed to enter "
						lcd.writeLCD(a[2],'Welcome!')
					elif a[4]==1:
						print a[2]+": exists and already checked in"
						lcd.writeLCD(a[2],'Already in!')

			if n==0:
				print barcode+": doesn't exist!"
				lcd.writeLCD(barcode,'Not found !')
			n=0
			barcode =" "
