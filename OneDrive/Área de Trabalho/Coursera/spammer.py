import pyautogui, time
time.sleep(5)
rt= open("shrek", "r")
for linha in rt:
    pyautogui.typewrite(linha)
    pyautogui.press("enter")
    