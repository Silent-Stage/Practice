# import pyautogui, time, subprocess
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