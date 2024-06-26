# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Christian\Desktop\Python projects\First Project\Money_Dashboard\Money-Tracker\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Budget Tracker")

# Format and display data
def add_Sum_And_Calculate_Display(some_var, some_id_text):
    new_income_rounded = round(some_var, 2)
    some_var = new_income_rounded
    
    new_text_display = "${:.2f}".format(new_income_rounded)
    canvas.itemconfig(tagOrId=some_id_text, text=new_text_display)
    return some_var

def check_For_Name():
    # Make our variables global cuz we need to access them
    global income, expense, balance
    try:
        name = entry_1.get().lower()
        # Take input and convert it to double sum
        new_income = float(entry_2.get())
        
        if name == "add" or name == "income":
            # Sum our new income with our current income value
            income += new_income
            # Equalize sums
            income = add_Sum_And_Calculate_Display(income, income_text)
            # Calculate our balance
            balance = income - expense
            balance = add_Sum_And_Calculate_Display(balance, balance_text)
        elif name == "subtract" or name == "expense":
            expense += new_income
            expense = add_Sum_And_Calculate_Display(expense, expense_text)
            balance = income - expense
            balance = add_Sum_And_Calculate_Display(balance, balance_text)
        else:
            messagebox.showinfo("ERROR", "Check if your inputs are correct!")
    except:
        messagebox.showinfo("ERROR", "Check if your inputs are correct!")

# Get info from "canvas.create_text" and save it
def convert_Sum_To_Float(some_text):
    text_property = canvas.itemconfig(some_text, "text")
    # Taka canvas configuration from "text" field
    float_text = text_property[4].lstrip("$")
    # We cut "$" symbol because we cant convert it to float num
    return float_text

window.geometry("720x605")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 605,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    720.0,
    85.0,
    fill="#100770",
    outline="")

canvas.create_text(
    54.0,
    27.0,
    anchor="nw",
    text="Budget Tracker",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 32 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    193.0,
    147.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    363.0,
    239.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    533.0,
    149.0,
    image=image_image_3
)

canvas.create_text(
    69.0,
    119.0,
    anchor="nw",
    text="Income",
    fill="#46550C",
    font=("Inter ExtraBold", 15 * -1)
)

canvas.create_text(
    69.0,
    209.0,
    anchor="nw",
    text="Current Balance",
    fill="#2E3416",
    font=("Inter ExtraBold", 15 * -1)
)

canvas.create_text(
    410.0,
    119.0,
    anchor="nw",
    text="Expense",
    fill="#2C340B",
    font=("Inter ExtraBold", 15 * -1)
)



# Save as variable that we want to change
income_text = canvas.create_text(
    69.0,
    139.0,
    anchor="nw",
    text="$0.00",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
income = float(convert_Sum_To_Float(income_text))

balance_text = canvas.create_text(
    69.0,
    231.0,
    anchor="nw",
    text="$0.00",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
balance = float(convert_Sum_To_Float(balance_text))

expense_text = canvas.create_text(
    410.0,
    141.0,
    anchor="nw",
    text="$0.00",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
expense = float(convert_Sum_To_Float(expense_text))



canvas.create_text(
    54.0,
    289.0,
    anchor="nw",
    text="Add Sum:",
    fill="#100770",
    font=("Inter ExtraBold", 20 * -1)
)

canvas.create_text(
    53.0,
    329.0,
    anchor="nw",
    text="Name",
    fill="#100770",
    font=("Inter ExtraBold", 15 * -1)
)

canvas.create_text(
    52.0,
    417.0,
    anchor="nw",
    text="Amount($)",
    fill="#100770",
    font=("Inter ExtraBold", 15 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    538.0,
    477.0,
    image=image_image_4
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    199.5,
    385.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E3E3E3",
    fg="#000716",
    highlightthickness=0,
    font=("Inter Bold", 20)
)
entry_1.place(
    x=57.0,
    y=360.0,
    width=285.0,
    height=48.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    198.5,
    473.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E3E3E3",
    fg="#000716",
    highlightthickness=0,
    font=("Inter Bold", 20)
)
entry_2.place(
    x=56.0,
    y=448.0,
    width=285.0,
    height=48.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_For_Name(),
    relief="flat"
)
button_1.place(
    x=41.0,
    y=522.0,
    width=315.0,
    height=55.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    648.0,
    239.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    649.0,
    42.0,
    image=image_image_6
)
window.resizable(False, False)
window.mainloop()
