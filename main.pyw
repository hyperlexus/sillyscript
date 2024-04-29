import tkinter as tk
import time, math
from datetime import datetime
def tts(ms):
    y = ms // 31556952
    ms %= 31556952
    we = ms // 604800
    ms %= 604800
    d = ms // 86400
    ms %= 86400
    h = ms // 3600
    ms %= 3600
    m = ms // 60
    s = ms % 60
    return f"{y:04}:{we:02}:{d:01}:{h:02}:{m:02}:{s:02}"
def up():
    with open("C:\\Users\\HyperLexus\\Desktop\\beginning.txt", "r") as f:
        st = f.read().strip()
    now = int(time.time())
    e = now - int(st)
    os = tts(e)
    tl.config(text=os)
    w.after(1000, up)
def save_timestamp():
    with open("C:\\Users\\HyperLexus\\Desktop\\beginning.txt", "w") as f:
        now = int(time.time())
        print(now)
        f.write(str(now))
w = tk.Tk()
w.title("streak")
w.geometry("700x150")
tl = tk.Label(w, font=("Mario Kart Wii Placement Regular", 48))
tl.pack(expand=True, fill='both')  # Center the label
sb = tk.Button(w, text="reset", command=save_timestamp)
sb.pack(expand=True)
up()
w.mainloop()