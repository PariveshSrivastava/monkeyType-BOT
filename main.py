import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import ImageGrab
import time
import pyautogui as pag
# hi lolol
i = 3
print("starting in "+str(i)+" seconds")
time.sleep(i)
start_time = time.time()
#hihi this is uruj
# first line top left and right bottom pixel
def firstCall():
    x1, y1, x2, y2 = 180, 435, 1775, 485
    text = pytesseract.image_to_string(ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert('L'))
    pag.typewrite(text)
    pag.press('space')
    time.sleep(0.4)

def getTfI(): 
    x1, y1, x2, y2 = 180, 490, 1775, 540
    text = pytesseract.image_to_string(ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert('L'))
    return text

def write():
    l =getTfI()
    print(l)
    pag.typewrite(l)
    pag.press('space')
 
firstCall()
while True:
    write()
    time.sleep(0.5)
         
