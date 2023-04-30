import time
import cv2
import numpy as np
import pyautogui
import keyboard
def find_icon_on_screen(icon_image):
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    icon = cv2.imread(icon_image, cv2.IMREAD_GRAYSCALE)
    width, height = icon.shape[::-1]

    res = cv2.matchTemplate(screenshot_gray, icon, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val > 0.85:  # Change the threshold value to be more or less strict in matching
        top_left = max_loc
        center = (top_left[0] + width // 2, top_left[1] + height // 2)
        return center
    else:
        return None

def solo():
    yes_icon = 'yes.png'
    next_icon = 'next.png'
    again_icon = 'again.png'
    decide_icon = 'decide.png'
    disconnect_icon = 'disconnect.png'

    yes_pos = find_icon_on_screen(yes_icon)
    next_pos = find_icon_on_screen(next_icon)
    decide_pos = find_icon_on_screen(decide_icon)
    again_pos = find_icon_on_screen(again_icon)
    disconnect_pos = find_icon_on_screen(disconnect_icon)

    if disconnect_pos:
        time.sleep(0.1)
        pyautogui.click(disconnect_pos)
    elif again_pos:
        time.sleep(0.1)
        pyautogui.click(again_pos)
    elif decide_pos:
        time.sleep(0.3)
        pyautogui.click(decide_pos)
        time.sleep(0.1)
    elif next_pos:
        time.sleep(0.1)
        pyautogui.click(next_pos)
        time.sleep(0.1)
    elif yes_pos:
        time.sleep(0.1)
        pyautogui.click(yes_pos)
        time.sleep(0.1)
    else:
        print("Icon not found on screen")
def main():
    join_icon = 'join.png'
    refresh_icon = 'refresh.png'
    decide_icon = 'decide.png'
    go_icon = 'go.png'
    next_icon = 'next.png'
    return_icon = 'return.png'
    yes_icon = 'yes.png'
    ok_icon = 'ok.png'
    disconnect_icon = 'disconnect.png'

    disconnect_pos = find_icon_on_screen(disconnect_icon)
    join_pos = find_icon_on_screen(join_icon)
    refresh_pos = find_icon_on_screen(refresh_icon)
    decide_pos = find_icon_on_screen(decide_icon)
    go_pos = find_icon_on_screen(go_icon)
    next_pos = find_icon_on_screen(next_icon)
    return_pos = find_icon_on_screen(return_icon)
    yes_pos = find_icon_on_screen(yes_icon)
    ok_pos = find_icon_on_screen(ok_icon)

    if disconnect_pos:
        time.sleep(0.1)
        pyautogui.click(disconnect_pos)
    elif join_pos:
        time.sleep(0.1)
        pyautogui.click(join_pos)
        time.sleep(0.1)
        print(f"Icon found and clicked at {join_pos}")
    elif ok_pos:
        time.sleep(0.1)
        pyautogui.click(ok_pos)
    elif refresh_pos:
        time.sleep(0.1)
        pyautogui.click(refresh_pos)
        time.sleep(0.1)
    elif decide_pos:
        time.sleep(0.3)
        pyautogui.click(decide_pos)
        time.sleep(0.1)
    elif go_pos:
        time.sleep(0.1)
        pyautogui.click(go_pos)
        time.sleep(0.1)
    elif next_pos:
        time.sleep(0.1)
        pyautogui.click(next_pos)
        time.sleep(0.1)
    elif return_pos:
        time.sleep(0.1)
        pyautogui.click(return_pos)
        time.sleep(0.1)
    elif yes_pos:
        time.sleep(0.1)
        pyautogui.click(yes_pos)
        time.sleep(0.1)
    else:
        print("Icon not found on screen")

def draw():
    _550_icon = '550.png'
    boxconfirm_icon = 'boxconfirm.png'
    nextbox_icon = 'nextbox.png'
    redok_icon = 'redok.png'
    disconnect_icon = 'disconnect.png'
    whiteticket_icon = 'whiteticket.png'
    yesbox_icon = 'yesbox.png'


    yesbox_pos = find_icon_on_screen(yesbox_icon)
    nextbox_pos = find_icon_on_screen(nextbox_icon)
    boxconfirm_pos = find_icon_on_screen(boxconfirm_icon)
    redok_pos = find_icon_on_screen(redok_icon)
    disconnect_pos = find_icon_on_screen(disconnect_icon)
    whiteticket_pos = find_icon_on_screen(whiteticket_icon)
    _550_pos = find_icon_on_screen(_550_icon)
    checked_pos = find_icon_on_screen('checked.png')

    if disconnect_pos:
        time.sleep(0.1)
        pyautogui.click(disconnect_pos)
    elif checked_pos and yesbox_pos:
        time.sleep(0.1)
        pyautogui.click(yesbox_pos)
        time.sleep(0.1)
    elif whiteticket_pos:
        time.sleep(0.1)
        pyautogui.click(whiteticket_pos)
        time.sleep(0.1)
    elif _550_pos:
        time.sleep(0.3)
        pyautogui.click(_550_pos)
        time.sleep(0.1)
    elif redok_pos:
        time.sleep(0.3)
        pyautogui.click(redok_pos)
        time.sleep(0.1)
    elif nextbox_pos:
        time.sleep(0.1)
        pyautogui.click(nextbox_pos)
    elif boxconfirm_pos:
        time.sleep(0.3)
        pyautogui.click(boxconfirm_pos)
        time.sleep(0.1)

    else:
        print("Icon not found on screen")

if __name__ == '__main__':
    mode = 1
    while not keyboard.is_pressed('space'):
        if mode == 1:
            main()
        elif mode == 2:
            solo()
        elif mode == 3:
            draw()
        time.sleep(0.1)
    print("Space key pressed, stopping...")