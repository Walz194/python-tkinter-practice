import tkinter

window = tkinter.Tk()
label = tkinter.Label(window,text='This is new text')
label.pack()

def action():
    print('DO something !!!')

button = tkinter.Button()
button['text'] = 'Click Me'
button['command'] = action
button.pack()

text_input = tkinter.Entry()
text_input.insert(tkinter.END, string='Some text to begin with.')
text_input['width']=40
print(text_input.get())
text_input.pack()

text_area = tkinter.Text(height=5,width=25)
text_area.insert(tkinter.END,'Example of multi-line text entry')
text_area.focus()
text_area.pack()

def spinbox_used():
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0,to=10,width=5)
spinbox['command'] = spinbox_used
spinbox.pack()

def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0,to=1000)
scale['command'] = scale_used
scale.pack()


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text='Is On?',variable=checked_state)
checkbutton['command'] = lambda: print(checked_state.get())
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text='Option1',value=1,variable=radio_state,command=radio_used)
radiobutton2 = tkinter.Radiobutton(text='Option2',value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ['Apple','Pear','Orange','Banana']
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()





window.minsize(width=500, height=450)
window.title('Play Ground')

window.mainloop()
