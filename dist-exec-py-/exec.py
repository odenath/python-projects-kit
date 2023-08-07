import pyautogui
import time
# Executável de teste
pyautogui.PAUSE = 0.5

time.sleep(4.5)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(4.5)
pyautogui.write("Pq o Gustavo é tão lindo?")
pyautogui.press("enter")


# Teste com o seu colega rs 
# while True:
#     pyautogui.hotkey("alt", "tab")
#     if pyautogui.press("esc"):
#         break   


