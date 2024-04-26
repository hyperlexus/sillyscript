import tkinter as tk
from datetime import datetime
def up():
    with open("C:\\Users\\HyperLexus\\Desktop\\beginning.txt", "r") as f:
        st = f.read().strip()
        s = datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    e = now - s
    y, d = divmod(e.days, 365)
    d = d % 7
    w_e = (now.date().isocalendar()[1] - s.date().isocalendar()[1]) % 53
    os = f"{y:04}:{w_e:02}:{d}:{e.seconds // 3600:02}:{e.seconds % 3600 // 60:02}:{e.seconds % 60:02}"
    tl.config(text=os)
    w.after(1000, up)
def save_timestamp():
    with open("C:\\Users\\HyperLexus\\Desktop\\beginning.txt", "w") as f:
        now = datetime.now()
        ts = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(ts)
w = tk.Tk()
w.title("streak")
w.geometry("700x150")
tl = tk.Label(w, font=("Mario Kart Wii Placement Regular", 48))
tl.pack(expand=True, fill='both')  # Center the label
sb = tk.Button(w, text="reset", command=save_timestamp)
sb.pack(expand=True)
up()
w.mainloop()