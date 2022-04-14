#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
import RGB1602
import time

lcd=RGB1602.RGB1602(16,2)

# Beispielfarben des Herstellers
rgb1 = (148,0,110)  # Dunkellila
rgb2 = (255,0,255)  # Lila
rgb3 = (144,249,15) # Blauweiß
rgb4 = (0,128,60)   # Hellblau
rgb5 = (255,209,0)  # Gelb
rgb6 = (248,248,60) # Geisterweiß
rgb7 = (80,80,145)  # Dunkelblau
rgb8 = (255,0,0)    # Rot
rgb9 = (0,255,0)    # Grün

# LCD löschen, falls was drauf ist
lcd.clear()

# Cursor auf die erste Stelle der ersten Zeile setzen
# Zeichen,Zeile von 0,0 bis 15,1
lcd.setCursor(0, 0)

lcd.printout("Klein ä ö ü ß ")

# Cursor auf die erste Stelle der zweiten Zeile setzen
# Zeichen,Zeile von 0,0 bis 15,1
lcd.setCursor(0, 1)

lcd.printout("Groß Ä Ö Ü")
 
# LED Farbe setzen 
rgb= rgb7
lcd.setRGB(rgb[0],rgb[1],rgb[2]);
