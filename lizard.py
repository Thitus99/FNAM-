import pygame as pg
import time
import keyboard as kb
import sys
pg.init()
running = True
lizard = pg.mixer.Sound("lizard-button.mp3")
pressed_keys = set()
oldkeys = pg.key.get_pressed()
def onKey(event):
    if len(pressed_keys) == 2 and 'delete' in pressed_keys and 'ctrl' in pressed_keys:
        print("welp")
        sys.exit()
        quit()
    elif event.event_type == 'down' and event.name not in pressed_keys:
        lizard.play()
        pressed_keys.add(event.name)
    elif event.event_type == 'up' and event.name in pressed_keys:
        pressed_keys.remove(event.name)
    for i in range(50):
        kb.send("volume up")
if running:
    kb.hook(onKey)      
    kb.wait()

    
    