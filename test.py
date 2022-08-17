import os
from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD

root = TkinterDnD.Tk()

root.geometry("600x200")

lb = Listbox(root)
lb.pack(padx=20,pady=20,fill=BOTH,expand=True)

scrollbar = Scrollbar(lb, orient="vertical")
scrollbar.config(command=lb.yview)
scrollbar.pack(side="right", fill="y")

lb.config(yscrollcommand=scrollbar.set)

def handle(e):

	if os.path.isdir(e.data):  
		lb.insert(END, "It is a directory")
	elif os.path.isfile(e.data):
		f = open(e.data, "r")
		lb.insert(END, f.read())
	else:  
		print("")

lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', handle )

root.mainloop()
