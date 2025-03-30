import json
import keyboard
import time


with open("./data/all.json") as f:
    data = json.load(f)

kf = []
r13 = []
r18 = []

for i in data:
    print("[1] = kf, [2] = r13, [3] = r18 \n")
    print(i)
    print("\n\n")
    while True:
        if keyboard.is_pressed("1"):
            kf.append(i)
            break
        elif keyboard.is_pressed("2"):
            r13.append(i)
            break
        elif keyboard.is_pressed("3"):
            r18.append(i)
            break
    while True:
        if not keyboard.is_pressed("1") and not keyboard.is_pressed("2") and not keyboard.is_pressed("3"):
            break

with open("./data/kf.json", "w") as f:
    f.write(json.dumps(kf))

with open("./data/r13.json", "w") as f:
    f.write(json.dumps(r13))

with open("./data/r18.json", "w") as f:
    f.write(json.dumps(r18))

