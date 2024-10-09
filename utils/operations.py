import pyautogui
import time


class PCController:
    def __init__(self):
        pass

    # 按下某个键
    def press_key(self, key):
        pyautogui.keyDown(key)

    # 松开某个键
    def release_key(self, key):
        pyautogui.keyUp(key)

    # 移动鼠标指定距离
    def move_mouse(self, x, y, duration=0):
        pyautogui.move(x, y, duration=duration)

    # 将鼠标移动到特定坐标
    def move_mouse_to(self, x, y, duration=0):
        pyautogui.moveTo(x, y, duration=duration)

    # 按下鼠标的左键
    def click_left_mouse(self):
        pyautogui.mouseDown(button="left")

    # 松开鼠标的左键
    def release_left_mouse(self):
        pyautogui.mouseUp(button="left")

    # 按下鼠标的右键
    def click_right_mouse(self):
        pyautogui.mouseDown(button="right")

    # 松开鼠标的右键
    def release_right_mouse(self):
        pyautogui.mouseUp(button="right")

    # 按下鼠标的中键
    def click_middle_mouse(self):
        pyautogui.mouseDown(button="middle")

    # 松开鼠标的中键
    def release_middle_mouse(self):
        pyautogui.mouseUp(button="middle")

    # 滚动鼠标滚轮，正数向上滚动，负数向下滚动
    def scroll_mouse(self, clicks):
        pyautogui.scroll(clicks)


def run():
    # 测试示例
    controller = PCController()
    # 按下和松开 'a' 键
    controller.press_key("a")
    time.sleep(1)
    controller.release_key("a")
    # 鼠标移动 (100, 0)，向右移动100像素
    controller.move_mouse(100, 0, duration=0.2)
    # 将鼠标移动到屏幕坐标 (500, 500)
    controller.move_mouse_to(500, 500, duration=0.2)
    # 按下左键
    controller.click_left_mouse()
    time.sleep(1)
    controller.release_left_mouse()
    # 向上滚动鼠标100个单位
    controller.scroll_mouse(100)


if __name__ == "__main__":
    run()
