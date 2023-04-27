from pynput import mouse
import os
os.system("cls")

"""def on_press(Key): 
    print(" la touche à été appoyer : ", Key)

    if Key == keyboard.Key.esc:
        return False

def on_release(Key):
    print("La touche a été realché : ", Key)

    if Key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_release, on_release=on_release) as Listener:
    Listener.join()
"""
def on_click(x,y, boutton, pressed):
    print("Le boutton ", boutton, "a été cliqué en ", x, " ", y)
    if boutton == mouse.Button.left:
        return False

def on_move(x,y):
    print("La souri à bouger ", x, " ", y)


def on_scroll(x, y, dx, dy):
    print("L'utilisateur à scroll")

with mouse.Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll) as listener:
    listener.join()