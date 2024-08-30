import pyautogui as pg
import time as t
t.sleep(1)
for i in range(10):
    pg.write("AP")
    pg.press("enter")