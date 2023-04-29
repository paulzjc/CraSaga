import cv2
import numpy as np
import pyautogui

def find_icon_on_screen(icon_image):
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    icon = cv2.imread(icon_image, cv2.IMREAD_GRAYSCALE)
    width, height = icon.shape[::-1]

    res = cv2.matchTemplate(screenshot_gray, icon, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val > 0.8:  # Change the threshold value to be more or less strict in matching
        top_left = max_loc
        center = (top_left[0] + width // 2, top_left[1] + height // 2)
        return center
    else:
        return None

def main():
    icon_image = 'icon.png'

    icon_position = find_icon_on_screen(icon_image)
    if icon_position:
        pyautogui.click(icon_position)
        print(f"Icon found and clicked at {icon_position}")
    else:
        print("Icon not found on screen")

if __name__ == '__main__':
    main()