import cv2
import numpy as np
import pyautogui
import keyboard
import os
import time

from win32con import (
    IDC_APPSTARTING,
    IDC_ARROW,
    IDC_CROSS,
    IDC_HAND,
    IDC_HELP,
    IDC_IBEAM,
    IDC_ICON,
    IDC_NO,
    IDC_SIZE,
    IDC_SIZEALL,
    IDC_SIZENESW,
    IDC_SIZENS,
    IDC_SIZENWSE,
    IDC_SIZEWE,
    IDC_UPARROW,
    IDC_WAIT,
)

from win32gui import LoadCursor, GetCursorInfo

DEFAULT_CURSORS = {
    LoadCursor(0, IDC_APPSTARTING): "appStarting",
    LoadCursor(0, IDC_ARROW): "Arrow",
    LoadCursor(0, IDC_CROSS): "Cross",
    LoadCursor(0, IDC_HAND): "Hand",
    LoadCursor(0, IDC_HELP): "Help",
    LoadCursor(0, IDC_IBEAM): "IBeam",
    LoadCursor(0, IDC_ICON): "ICon",
    LoadCursor(0, IDC_NO): "No",
    LoadCursor(0, IDC_SIZE): "Size",
    LoadCursor(0, IDC_SIZEALL): "sizeAll",
    LoadCursor(0, IDC_SIZENESW): "sizeNesw",
    LoadCursor(0, IDC_SIZENS): "sizeNs",
    LoadCursor(0, IDC_SIZENWSE): "sizeNwse",
    LoadCursor(0, IDC_SIZEWE): "sizeWe",
    LoadCursor(0, IDC_UPARROW): "upArrow",
    LoadCursor(0, IDC_WAIT): "Wait",
}


def get_current_cursor():
    curr_cursor_handle = GetCursorInfo()[1]
    res = DEFAULT_CURSORS.get(curr_cursor_handle, "None")
    print(res)
    return res


def capture_screenshot_with_cursor():
    print("Start capturing screenshot...")
    # Create screenshots directory if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Capture the screen using pyautogui
    screenshot = pyautogui.screenshot()
    
    img = np.array(screenshot)

    # Convert RGB to BGR (OpenCV uses BGR by default)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Get the current position of the mouse cursor using pyautogui
    cursor_x, cursor_y = pyautogui.position()

    # Record the current cursor state
    cursor_state = get_current_cursor()
    print(f"current cursor state: {cursor_state}")

    # Convert the screenshot to a numpy array (which OpenCV uses)

    # Draw a white circle to represent the cursor
    cursor_radius = 7  # You can adjust the size of the circle here
    cursor_color = (255, 255, 255)  # White color
    cursor_thickness = -1  # Filled circle

    cv2.circle(img, (cursor_x, cursor_y), cursor_radius, cursor_color, cursor_thickness)

    # Generate the base filename using the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    base_filename = f"screenshot_{timestamp}"

    # Generate a unique filename to avoid overwriting
    output_file = os.path.join("screenshots", f"{base_filename}.jpg")
    counter = 1
    while os.path.exists(output_file):
        output_file = os.path.join("screenshots", f"{base_filename}_{counter}.jpg")
        counter += 1

    # Save the final image in the screenshots directory with the unique filename
    cv2.imwrite(output_file, img)
    print(f"Screenshot saved as {output_file}")
    return cursor_state


def on_hotkey():
    capture_screenshot_with_cursor()


def run():
    print("Press 'Ctrl+Shift+K' to capture a screenshot with the cursor.")
    # Register the hotkey
    keyboard.add_hotkey("ctrl+shift+k", on_hotkey)

    # Wait for the user to press ESC to exit the program
    print("Press 'ESC' to exit.")
    keyboard.wait("esc")


if __name__ == "__main__":
    run()
