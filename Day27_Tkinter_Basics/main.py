from tkinter import *

def button_clicked():
    new_value=round(float(miles.get()) * 1.60934,2)
    km_value.config(text=f"{new_value}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)

#Entry
miles = (Entry(width=10))
miles.grid(column=2, row=0)


#miles Label
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=3, row=0)

#is_equal_to Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 10))
is_equal_to_label.grid(column=0, row=1)

#km_value Label
km_value = Label(text="0", font=("Arial", 10))
km_value.grid(column=2, row=1)

#miles Label
km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=3, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=2)

window.mainloop()