import math
import time

import cv2
import pyautogui
import numpy as np


time.sleep(3)

RADIUS = 470
STEPS = 60

screenshot = pyautogui.screenshot()
cropped_image = screenshot.crop((1920/2-200, 1080/2-200, 1920/2+200, 1080/2+200))
image_grayscale = cv2.cvtColor(np.array(cropped_image), cv2.COLOR_RGB2GRAY)

# GET Y
brightness = cv2.threshold(image_grayscale, 240, 255, cv2.THRESH_BINARY)[1]
y_brightness = [sum(x) for x in brightness]
start = -1
end = -1
for n, i in enumerate(y_brightness):
    if start == -1:
        if i != 0:
            start = n
    else:
        if i == 0:
            end = n
            break
y = np.argmax(y_brightness[start:end]) + start

# GET X
start = -1
end = -1
for n, i in enumerate(brightness[y]):
    if start == -1:
        if i != 0:
            start = n
    else:
        if i == 0:
            end = n
            break
x = (end - start) // 2 + start

# Start
x_center = 1920/2 - 200 + x
y_center = 1080/2 - 200 + y
pyautogui.moveTo(x_center + RADIUS, y_center)
pyautogui.mouseDown(button='left')

def y(t):
    return RADIUS * math.sin(t) + y_center

def x(t):
    return RADIUS * math.cos(t) + x_center

for tdeg in range(0, 360, 360 // STEPS):
    t = math.radians(tdeg)
    pyautogui.moveTo(x(t), y(t))

pyautogui.moveTo(x(2*math.pi), y(2*math.pi))

pyautogui.mouseUp(button='left')
