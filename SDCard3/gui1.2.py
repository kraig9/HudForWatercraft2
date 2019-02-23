import Tkinter as tk
import time

windSpeed = '50 M/s'
fuel = '5 L'
windDirection = 'NW'
depth = '5 M'
BoatSpeed = '50 M/s'

#This block makes the base window and makes it fullscreen.
#Credit from https://gist.github.com/TravisJoe/5576258
root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())
root.configure(background='black')

w = tk.Label(root, text="Wind Speed", fg='yellow', bg='black', font=("",60))
w.grid(row=0, column=0, sticky=tk.NW)

textDispw = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("",60))
textDispw.grid(row=1, column=0, sticky=tk.NW)
textDispw.insert(tk.END, windSpeed)

x = tk.Label(root, text="Fuel", fg='yellow', bg='black', font=("",60))
x.place(rely=0, relx=1, x=0, y=0, anchor=tk.NE)

textDispx = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("",60))
textDispx.place(rely=0, relx=1, x=0, y=90, anchor=tk.NE)
textDispx.insert(tk.END, fuel)

#################################################################################
#added in later
mid = tk.Label(root, text="Boat Speed", fg='yellow', bg='black', font=("",60))
mid.place(rely=0, relx=.5, x=0, y=0, anchor=tk.N)

textDispMid = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("",60))
textDispMid.place(rely=0, relx=.5, x=0, y=90, anchor=tk.N)
textDispMid.insert(tk.END, BoatSpeed)
##################################################################################

y = tk.Label(root, text="Wind Direction", fg='yellow', bg='black', font=("",60))
y.place(rely=1.0, relx=0, x=0, y=0, anchor=tk.SW)

textDispy = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("",60))
textDispy.place(rely=1.0, relx=0, x=0, y=-90, anchor=tk.SW)
textDispy.insert(tk.END, windDirection)

z = tk.Label(root, text="Depth", fg='yellow', bg='black', font=("",60))
z.place(rely=1.0, relx=1.0, x=0, y=0, anchor=tk.SE)

textDispz = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("",60))
textDispz.place(rely=1.0, relx=1.0, x=0, y=-90, anchor=tk.SE)
textDispz.insert(tk.END, depth)

root.attributes("-alpha",0.5)

while True:
    '''
        windSpeed += 1
        fuel += 1
        windDirection += 1
        depth += 1
        BoatSpeed += 1
    '''


    textDispw.delete('1.0', tk.END)
    textDispw.insert(tk.END, windSpeed)
    textDispw.update_idletasks()
    textDispx.delete('1.0', tk.END)
    textDispx.insert(tk.END, fuel)
    textDispx.update_idletasks()
######################################
    textDispMid.delete('1.0', tk.END)
    textDispMid.insert(tk.END, BoatSpeed)
    textDispMid.update_idletasks()
######################################
    textDispy.delete('1.0', tk.END)
    textDispy.insert(tk.END, windDirection)
    textDispy.update_idletasks()
    textDispz.delete('1.0', tk.END)
    textDispz.insert(tk.END, depth)
    textDispz.update_idletasks()
root.mainloop()
#root.update_idletasks()
#root.update()


