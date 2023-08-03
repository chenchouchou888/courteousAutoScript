import pyautogui

menuPosition = pyautogui.locateCenterOnScreen("./imgs/dongfu.jpg")
print(menuPosition)
pyautogui.click("./imgs/dongfu.jpg")
