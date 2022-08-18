import os
from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD

from os import listdir

#

from termcolor import colored
from os.path import isfile,isdir,join,getsize,basename
import json

os.system("color")

def rec(mypath,obj={}):
	sum=0
	for f in listdir(mypath):
		fp = join(mypath,f)
		if isfile(fp):
			# print( colored(f,"green"), colored(getsize(fp),"red"))
			sum+=getsize(fp)
			obj[f]=getsize(fp)
		elif isdir(fp):
			obj[f]={}
			sum+=rec(fp,obj[f])[0]
	return [sum,obj]

#

root = TkinterDnD.Tk()

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

root.geometry("800x400")
# root.config(bg=rgb_hack((66,69,73)))

lb = Listbox(root,font=("TkDefaultFont",15))
lb.pack(padx=20,pady=20,fill=BOTH,expand=True)

scrollbar = Scrollbar(lb, orient="vertical")
scrollbar.config(command=lb.yview)
scrollbar.pack(side="right",fill="y")

lb.config(yscrollcommand=scrollbar.set)

table=[]

def handle(e):

	if os.path.isdir(e.data):
		a = basename(e.data)
		b = rec(e.data)[0]
		obj = {}
		obj["name"]=a
		obj["size"]=b
		obj["full"]=e.data
		obj["type"]="folder"
		table.append(obj)
		if len(table) > 2 : table.pop(0)
		# content = f"size : {b}"
		lb.insert(END, e.data)
	elif os.path.isfile(e.data):
		obj = {}
		obj["name"]=basename(e.data)
		obj["size"]=getsize(e.data)
		obj["full"]=e.data
		obj["type"]="file"
		table.append(obj)
		if len(table) > 2 : table.pop(0)
		lb.insert(END,e.data)
		# f = open(e.data, "r")
		# lb.insert(END, f.read())

lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', handle )

def someFunction():
	# print(*table,sep='\n')
	if len(table) == 0:
		return 0
	if table[0]["full"] == table[1]["full"]:
		changeText("folder name are identical","red")
	elif table[0]["type"] != table[1]["type"]:
		changeText("folder type are different","red")
	elif table[0]["size"] != table[1]["size"]:
		changeText("folder size are different","red")
	elif table[0]["size"] == table[1]["size"]:
		changeText("folder size are identical","lightgreen")

def changeText(value,color):
	spacer1.config( text=value, fg=color )

def delete():
	lb.delete(0,END)

def show_table():
	print(json.dumps(table,indent=4))

top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM)

button = Button(root,font=("TkDefaultFont",20),text="compare",command=someFunction)
button.pack(in_=top, side=LEFT, pady=20, padx=5 )

button2 = Button(root,font=("TkDefaultFont",20),text="clear",command=delete)
button2.pack(in_=top, side=LEFT, pady=20, padx=5 )

button3 = Button(root,font=("TkDefaultFont",20),text="table",command=show_table)
button3.pack(in_=top, side=LEFT, pady=20, padx=5 )

spacer1 = Label(root,font=("TkDefaultFont",20),text="Hello World")
spacer1.pack(side=BOTTOM,pady=20,fill=BOTH)
spacer1.config(bg="black",fg="white")

root.mainloop()
