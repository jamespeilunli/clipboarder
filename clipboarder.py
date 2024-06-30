import pyautogui
import pyperclip

pyautogui.PAUSE = 0

def run(evaluate, copy=True, paste=True):
    if copy:
        pyautogui.hotkey("ctrl", "c")
    
    clipboard_content = pyperclip.paste()
    modified_content = evaluate(clipboard_content)
    pyperclip.copy(modified_content)

    if paste:
        pyautogui.hotkey("ctrl", "v")
