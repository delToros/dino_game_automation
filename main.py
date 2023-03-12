import pyautogui as ptg
import time
import keyboard
#
# time.sleep(3)
# print(ptg.position())

time.sleep(3)
ptg.press('space')
#
# screenshot = ptg.screenshot()
# base = screenshot.getpixel((361, 236))
# print(base[0])

while True:
    screenshot = ptg.screenshot()
    base = screenshot.getpixel((361, 236))

    tree_test1 = screenshot.getpixel((1020, 442))
    tree_test2 = screenshot.getpixel((1060, 441))
    tree_test3 = screenshot.getpixel((1080, 442))
    tree_test4 = screenshot.getpixel((1090, 441))

    # bird_test1 = screenshot.getpixel((1064, 415))
    # bird_test2 = screenshot.getpixel((1069, 412))
    # bird_test3 = screenshot.getpixel((1100, 413))
    # bird_test4 = screenshot.getpixel((1130, 413))

    if base[0] == 247:
        if tree_test1[0] != 247 or tree_test2[0] != 247 or tree_test3[0] != 247 :
            ptg.press('space')
            time.sleep(0.0001)

    if keyboard.is_pressed('s'):
        break