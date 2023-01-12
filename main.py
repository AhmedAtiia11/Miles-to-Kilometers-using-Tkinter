from tkinter import *
window=Tk()
window.title("Mile to Kilometer Program")
window.minsize(width=300,height=200)
def button_func():
    num_in_miles=int(user_input.get())
    num_in_kilos=num_in_miles*1.60934
    result.config(text=num_in_kilos)


in_label=Label(text="The input in Miles")
in_label.grid(column=2,row=2)

user_input=Entry()
user_input.grid(column=2,row=3)


my_button=Button(text="Calculate",command=button_func)
my_button.grid(column=1,row=4)

out_label=Label(text="The output in Kilometers is")
out_label.grid(column=2,row=5)

result=Label(text="0")
result.grid(column=2,row=6)


window.mainloop()

