import pyautogui
import time
import random
from pynput import keyboard
import threading

pyautogui.FAILSAFE = True


czas_kopania = 1050        
min_krok = 0.25            
max_krok = 0.45
szerokosc = 13
pauza_koniec = 0


running = False
thread = None

def kopanie():
    global running

    pozycja = 1        
    kierunek = 1       
    start = time.time()

    pyautogui.mouseDown(button='left')
    # pyautogui.keyDown('w')

    while running and (time.time() - start < czas_kopania):
        krok_czas = random.uniform(min_krok, max_krok)

        if kierunek == 1:
            pyautogui.keyDown('d')
            time.sleep(krok_czas)
            pyautogui.keyUp('d')
            pozycja += 1
        else:
            pyautogui.keyDown('a')
            time.sleep(krok_czas)
            pyautogui.keyUp('a')
            pozycja -= 1

        
        if pozycja == szerokosc or pozycja == 1:
            time.sleep(pauza_koniec)
            kierunek *= -1  

    pyautogui.mouseUp(button='left')
    # pyautogui.keyUp('w')
    running = False
    print("⛏️ Kopanie zatrzymane")

def on_press(key):
    global running, thread
    try:
        if key == keyboard.Key.f8:
            if not running:
                print("▶ START (F8)")
                running = True
                thread = threading.Thread(target=kopanie)
                thread.start()
            else:
                print("⏹ STOP (F8)")
                running = False
    except:
        pass

print("Gotowe.")
print("F8 = START / STOP")
print("Masz 5 sekund na przejście do Minecrafta...")

time.sleep(5)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
