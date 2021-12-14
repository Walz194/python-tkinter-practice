import tkinter

window = tkinter.Tk()
window.title('My First GUI program')
window.minsize(width=500,height=300)

def button_clicked():
    input_text = inputx.get()
    if input_text != '':
        my_label['text'] = input_text
    inputx.insert(tkinter.END, string='book')

# Label
my_label = tkinter.Label(text='I am a label',font=('Arial',12,'bold'))
# Just creating a label does not make the label to come up on the window
# To add the label to the screen, we'll need to either...
# my_label.grid(row=0,column=1)
# OR

# tkinter was based of another project called tk/tcl so all the attributes that was specified there is made available in the tkinter module
# Essentially, those attributes are just a bunch of kwargs that can be accessed using the dictionary style of setting variables
my_label['text'] = 'New Text'

# We could use config to set multiple properties
my_label.config(text='Another text')
my_label.grid(row=0,column=0)
# Pack positions the label at the center of the screen, grid allows us to postion the element at specific positions

new_button = tkinter.Button(text='New Button')
new_button.grid(row=0,column=2)

button = tkinter.Button()
button['text'] = 'A button'
button['command'] = button_clicked
button.grid(row=1,column=1)

inputx = tkinter.Entry()
inputx['width'] = 50
inputx.grid(row=2,column=3)


window.mainloop()