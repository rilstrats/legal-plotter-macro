import pyautogui

ready = input("Ready? ")

pyautogui.click(button="left")

pyautogui.write("1", interval=0.25)
pyautogui.write("\n", interval=1)
pyautogui.write("55.4236", interval=0.25)
pyautogui.write("\n", interval=1)
pyautogui.write("300", interval=0.25)
pyautogui.write("\n", interval=1)

# pyautogui.write("Hello world!\nI love you!\nA lot!", interval=0.25)
