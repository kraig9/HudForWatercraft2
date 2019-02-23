import Tkinter as tk
import time

textOut = 0
textOut2 = 10000
textOut3 = 100000
textOut4 = 1000000

#This block makes the base window and makes it fullscreen.
#Credit from https://gist.github.com/TravisJoe/5576258
root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())
root.configure(background='black')

w = tk.Label(root, text="Fuel", fg='yellow', bg='black', font=("",44))
w.pack(anchor = tk.SW)

textDispw = tk.Text(root, height=2, width=10, fg='yellow', bg='black', font=("",44))
textDispw.pack(anchor = tk.SW)
textDispw.insert(tk.END, textOut)

x = tk.Label(root, text="Wind Speed", fg='yellow', bg='black', font=("",44))
x.pack(side = tk.BOTTOM, anchor = tk.NW)

textDispx = tk.Text(root, height=2, width=10, fg='yellow', bg='black', font=("",44))
textDispx.pack(side = tk.BOTTOM, anchor = tk.NW)
textDispx.insert(tk.END, textOut2)

y = tk.Label(root, text="Wind Direction", fg='yellow', bg='black', font=("",44))
y.pack(anchor = tk.NE)

textDispy = tk.Text(root, height=2, width=10, fg='yellow', bg='black', font=("",44))
textDispy.pack(anchor = tk.NE)
textDispy.insert(tk.END, textOut3)

z = tk.Label(root, text="Depth", fg='yellow', bg='black', font=("",44))
z.pack(side = tk.BOTTOM, anchor = tk.SE)

textDispz = tk.Text(root, height=2, width=10, fg='yellow', bg='black', font=("",44))
textDispz.pack(side = tk.BOTTOM, anchor = tk.SE)
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


