import pyautogui, time
# #This script just shows your current mouse position, even when you move it
# print("Move your mouse around. Press Ctrl+C to stop")
# try:
#     while True:
#         x, y = pyautogui.position()
#         print(f"\rMouse at: ({x:4d}, {y:4d})", end="", flush = True)
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     print("\nDone!")

# #This script uses absolute coordinates, each movement goes to an exact screen position
# print("Watch the mouse move in 3 seonds...")
# time.sleep(3)
# start_x, start_y = pyautogui.position()
# print(f"Starting at: ({start_x}, {start_y})")
# pyautogui.moveTo(400, 300,duration=1)
# pyautogui.moveTo(500, 300,duration=1)
# pyautogui.moveTo(500, 400,duration=1)
# pyautogui.moveTo(400, 400,duration=1)

# #
# print("Relative movement starting in 3 seconds...")
# time.sleep(3)
# pyautogui.move(100, 0, duration=1)
# pyautogui.move(0, 100, duration=1)
# pyautogui.move(-100, 0, duration=1)
# pyautogui.move(0, -100, duration=1)

# subprocess.run(["gnome-calculator"], check = False)
# time.sleep(2)

# def getposition():
#     try:
#         while True:
#             x, y = pyautogui.position()
#             print(f"\rCurrent mouse position: ({x}, {y})", end = "", flush = True)
#             time.sleep(0.1)
#     except KeyboardInterrupt:
#         print("Done")
# getposition()

# def saveposition():
#     saved_positions = []
#     print("Interactive position saver!")
    
#     while True:
#         choice = input("Press 's' to save current position, 'q' to quit: ").lower()
        
#         if choice == 's':
#             x, y = pyautogui.position()
#             saved_positions.append((x, y))
#             print(f"Saved position: ({x}, {y})")
            
#         elif choice == 'q':
#             break
            
#         else:
#             print("Please press 's' or 'q'")
    
#     print("Saved positions:", saved_positions)
#     return saved_positions

# # Call the function
# saveposition()


def hovertarget():
    try:
        target = pyautogui.locateOnScreen(r"D:\Downloads\ST_DownloadButton.png", confidence=0.8)
        if target:
            center = pyautogui.center(target)
            pyautogui.moveTo(center)
            time.sleep(0.3)
            print("found")
            return True
        else:
            print("not found")
            return False
    except pyautogui.ImageNotFoundException:
        print("not found 2")
        return False
        
def openFE():
    try:
        target = pyautogui.locateOnScreen(r"D:\Downloads\ST_pngbutton.png", confidence=0.8)
        if target:
            center = pyautogui.center(target)
            pyautogui.click(center)
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False
def saveFE():
    try:
        time.sleep(1.5)
        target = pyautogui.locateOnScreen(r"D:\Downloads\ST_FEsave.png", confidence=0.8)
        if target:
            center = pyautogui.center(target)
            pyautogui.click(center)
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False
def STdownload():
    if not hovertarget():
        return False
    if not openFE():
        return False
    if not saveFE():
        return False
    return True
def ST():
    """Run STdownload() on all tabs without knowing how many exist"""
    
    consecutive_failures = 0
    max_consecutive_failures = 2
    target = pyautogui.locateOnScreen(r"D:\Downloads\ST_DownloadButton.png", confidence=0.8)
    if target:
            center = pyautogui.center(target)
            pyautogui.click(center)
    for tab_num in range(1, 9):
        pyautogui.hotkey('ctrl', str(tab_num))
        time.sleep(0.3)
        try:
            if STdownload():
                consecutive_failures = 0
            else:
                consecutive_failures += 1
        except Exception:
            consecutive_failures += 1
        if consecutive_failures >= max_consecutive_failures:
            break
        time.sleep(0.5)
ST()



