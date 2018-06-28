import tkinter
def BPAction(): 
	name = entry.get()
	Label1.configure(text = "Hello {}".format(name))

	print(name)
def BPEvent(action):
	BPAction()
root = tkinter.Tk()
Label1 = tkinter.Label(root)
Label1.grid(row = 0, padx = 7.5, pady = 7.5)
Label2 = tkinter.Label(root, text = "What is your name? ").grid(row = 1, column = 0, padx = 7.5, pady = 15)
entry = tkinter.Entry(root, width = 10)
entry.bind("<Return>",BPEvent)
entry.grid(row = 1, column = 1, padx = 7.5, pady = 15)

button = tkinter.Button(root, text = "Submit", command = BPAction)
button.grid(row = 2, column = 0, padx = 7.5, pady = 7.5)
root.mainloop()