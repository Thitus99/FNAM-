import pygame as pg
import time
import keyboard as kb
pg.init()
running = False
lizard = pg.mixer.Sound("lizard-button.mp3")
pressed_keys = set()
oldkeys = pg.key.get_pressed()
def onKey(event):
    if event.event_type == 'down' and event.name not in pressed_keys:
        for i in range(50):
            kb.send("volume up")
        lizard.play()
        pressed_keys.add(event.name)
    elif event.event_type == 'up' and event.name in pressed_keys:
        pressed_keys.remove(event.name)
if running:
    kb.hook(onKey)
    kb.wait()

    
    