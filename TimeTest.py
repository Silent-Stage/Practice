import time


def unload(clips):
    mag = 12
    while mag > 0:
        mag -= 1
        print(f"{mag}\nbrrrr\n")
        time.sleep(0.05)
    if mag == 0:
        for _ in range(clips):
            print("reloading...")
            time.sleep(1.5)
            unload(clips)

for p in range(clips):
    mag = 12
    while mag > 0:
        mag -= 1
        print(f"{mag}\nbrrrr\n")
        time.sleep(0.05)
        if mag == 0:
            print("reloading...")
            time.sleep(0.05)
            


