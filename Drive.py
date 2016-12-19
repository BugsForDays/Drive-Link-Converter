import Tkinter as tk

window = tk.Tk()

def cleart():
    lr.configure(state=tk.NORMAL)
    le.delete(0, tk.END)
    lr.delete(0, tk.END)
    lr.configure(state=tk.DISABLED)
def copy():
    window.clipboard_clear()
    window.clipboard_append(lr.get())

def convert():
    ide = le.get()
    ide = ide[32:60]
    lr.configure(state=tk.NORMAL)
    lr.insert(0,"https://drive.google.com/uc?export=download&id=" + ide)
    lr.configure(state=tk.DISABLED)

title = tk.Label(window, text ='GOOGLE DRIVE LINK CONVERTER')
title.grid(row=1, column=1, columnspan=2)
ll = tk.Label(window, text ='Google Drive Share Link: ')
ll.grid(row=3, column=1, columnspan=2)
le = tk.Entry(window)
le.grid(row=4, column=1, columnspan=2)
ll2 = tk.Label(window, text ='Direct Download Link: ')
ll2.grid(row=5, column=1, columnspan=2)
lr = tk.Entry(window)
lr.configure(state=tk.DISABLED)
lr.grid(row=6, column=1, columnspan=2)
cb = tk.Button(window, text="Convert!", command=convert)
cb.grid(row=7, column=1)
clb = tk.Button(window, text="Clear", command=cleart)
clb.grid(row=7, column=2)
ctb = tk.Button(window, text="Copy Download Link", command=copy)
ctb.grid(row=8, column=1, columnspan=2)

window.mainloop()
