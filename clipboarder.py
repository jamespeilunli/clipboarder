import pyautogui
import pyperclip

class Clipboarder:

    def __init__(self, evaluate, paste=True, copy=True):
        self.evaluate = evaluate
        self.copy = copy
        self.paste = paste

        # config pyautogui
        pyautogui.PAUSE = 0

    def run(self):
        if self.copy:
            pyautogui.hotkey("ctrl", "c")
        
        clipboard_content = pyperclip.paste()
        modified_content = self.evaluate(clipboard_content)
        pyperclip.copy(modified_content)

        if self.paste:
            pyautogui.hotkey("ctrl", "v")



