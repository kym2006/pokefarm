import cv2
import pytesseract
#pytesseract.pytesseract.tesseract_cmd=  r'Tesseract-OCR\\tesseract.exe'
import pyautogui as gui
import time
from pokemons import pokemons as pokemon
prefix = "p!catch"



recent = []
recentmons = []

time.sleep(3)
turn = 0


def on_press():
    global last, turn
    turn += 1
    # shot = gui.screenshot(region=(467,105,1532-467,907-105))
    shot = gui.screenshot()
    shot.save(r"screen.png")
    img = cv2.imread("screen.png")
    text = pytesseract.image_to_string(img)
    for mon in pokemon:
        if text.find(mon) != -1 and mon not in recentmons:
            gui.write(prefix + " " + mon + "\n")
            recent.append((mon, turn))
            recentmons.append(mon)
            turn += 1
            return
    gui.write("'\n")
    turn += 1
    if len(recent) and turn - recent[0][1] > 40:
        recent.pop(0)
        recentmons.pop(0)
while 1:
    on_press()
    #time.sleep(0.8)


