import pyautogui
import pyperclip

pyautogui.PAUSE = 0

def run(evaluate, preserve_clipboard=True, copy=True, paste=True):
    previous_content = None

    if preserve_clipboard:
        previous_content = pyperclip.paste()

    if copy:
        pyautogui.hotkey("ctrl", "c")
    
    clipboard_content = pyperclip.paste()
    modified_content = evaluate(clipboard_content)
    pyperclip.copy(modified_content)

    if paste:
        pyautogui.hotkey("ctrl", "v")

    if preserve_clipboard:
        pyautogui.sleep(0.2) # i believe pyautogui.hotkey is asynchronous
        pyperclip.copy(previous_content)
