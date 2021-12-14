import tkinter

window = tkinter.Tk()
window.config(padx=50,pady=50)
window.title('Mile to Km Converter')
window.resizable(width=False,height=False)

def calculate_km():
    km = 0
    miles = miles_input.get()
    try:
        km = round(float(miles) * 1.609344,2)
        km_out_label['text'] = f'{km}'
    except ValueError:
        print('Not a supported type')
        # Clear text input

miles_input = tkinter.Entry()
miles_input.grid(row=0,column=1)

miles_label = tkinter.Label(text='Miles')
miles_label.config(padx=5,pady=5)
miles_label.grid(row=0,column=2)

is_equal_label = tkinter.Label(text='is equal to')
is_equal_label.grid(row=1,column=0)

km_out_label = tkinter.Label(text='0')
km_out_label.grid(row=1,column=1)

km_label = tkinter.Label(text='Km')
km_label.grid(row=1,column=2)

calc_button = tkinter.Button(text='Calculate')
calc_button['command'] = calculate_km
calc_button.grid(row=2,column=1)


window.mainloop()