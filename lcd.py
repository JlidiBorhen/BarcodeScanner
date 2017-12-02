import RPi.GPIO as GPIO
from RPLCD import CharLCD, BacklightMode


lcd = CharLCD(pin_rs=37, pin_rw=22, pin_e=35, pins_data=[33,40,38,36],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              auto_linebreaks=True,
              pin_backlight=None, backlight_enabled=True,
              backlight_mode=BacklightMode.active_low)
def refresh() :
	lcd = CharLCD(pin_rs=37, pin_rw=22, pin_e=35, pins_data=[33,40,38,36],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              auto_linebreaks=True,
              pin_backlight=None, backlight_enabled=True,
              backlight_mode=BacklightMode.active_low)

def writeLCD(str1,str2) :
	lcd.write_string(str1.decode('utf-8'))
	lcd.cursor_pos = (1, 0)
	lcd.write_string(str2.decode('utf-8'))

def resetLCD():
	lcd.close(clear=True)
	GPIO.cleanup()
