import Tkinter as tk
import time

textOut = 0
textOut2 = 10000
textOut3 = 100000
textOut4 = 1000000

root = tk.Tk()
w = tk.Label(root, text="Fuel")
w.pack()

textDispw = tk.Text(root, height=2, width=30)
textDispw.pack()
textDispw.insert(tk.END, textOut)

x = tk.Label(root, text="Wind Speed")
x.pack()

textDispx = tk.Text(root, height=2, width=30)
textDispx.pack()
textDispx.insert(tk.END, textOut2)

y = tk.Label(root, text="Wind Direction")
y.pack()

textDispy = tk.Text(root, height=2, width=30)
textDispy.pack()
textDispy.insert(tk.END, textOut3)

z = tk.Label(root, text="Depth")
z.pack()

textDispz = tk.Text(root, height=2, width=30)
textDispz.pack()
textDispz.insert(tk.END, textOut4)

root.attributes("-alpha",0.5)

while True:
    textOut += 1
    textOut2 += 1
    textOut3 += 1
    textOut4 += 1

    textDispw.delete('1.0', tk.END)
    textDispw.insert(tk.END, textOut)
    textDispw.update_idletasks()
    textDispx.delete('1.0', tk.END)
    textDispx.insert(tk.END, textOut2)
    textDispx.update_idletasks()
    textDispy.delete('1.0', tk.END)
    textDispy.insert(tk.END, textOut3)
    textDispy.update_idletasks()
    textDispz.delete('1.0', tk.END)
    textDispz.insert(tk.END, textOut4)
    textDispz.update_idletasks()
root.mainloop()
#root.update_idletasks()
#root.update()


