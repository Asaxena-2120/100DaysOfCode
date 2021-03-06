from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# -------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters)for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

    # Copy generated password to clipboard
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD --------------------------- #


def search():
    website = website_entry.get()

    try:
        with open('data.json', 'r') as file:
            # read old data from json file
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title='Error', message=f"No details for {website} exists.")
# ---------------------------- SAVE PASSWORD --------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
             "email": email,
             "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message= "Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f" These are the details entered: \nEmail: "
                                                      f"{email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as file:

                    # read old data from json file
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data,file, indent=4)
            else:
                # update the old json data to new data
                data.update(new_data)

                with open('data.json', 'w') as file:
                    # write the updated data
                    json.dump(data, file, indent=4)
            finally:
                ## write data to txt file
                # file.write(f"{website} | {email} | {password}")
                # file.write('\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Tomato Image canvas
canvas = Canvas(width=200, height=200)

# read through a file and get hold of the image
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
# Website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Email label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# Password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Enteries

# website Entry
website_entry = Entry(width=17)
website_entry.grid(row=1, column=1)
website_entry.focus()

# Email Entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"abc@gmail.com")
# Password Entry
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)


# Buttons
# Generate_password button
generate_password_button = Button(text="Generate Password", command= generate_password)
generate_password_button.grid(row=3, column=2)
# Add button
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)
# Search button
search_button = Button(text="Search",width=17,command=search)
search_button.grid(row=1, column=2)

window.mainloop()