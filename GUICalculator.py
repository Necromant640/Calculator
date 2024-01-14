#Testo 2

import tkinter as tk
import customtkinter as ctk
import os

#Functions
i = 0
calculation = ""

def add_to_calculation(symbol):
    global calculation
    if symbol == "%":
        symbol = "/100"
    calculation += str(symbol)
    entry.delete(0, ctk.END)
    entry.insert(0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        entry.delete(0, ctk.END)
        entry.insert(0, calculation)
    except:
        clear_field()
        entry.insert(0, "Error")
    
def clear_field():
    global calculation
    entry.delete(0, ctk.END)
    calculation = ""

def smile():
    file_path = (r"C:\Users\Public\Downloads\rick.cmd")
    with open(file_path, "w") as file:
        file.write("curl ascii.live/rick")
    os.system(file_path)

#Window setup
root = ctk.CTk()
root.title("Calculator")
root.geometry("255x370")
root._set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
#Shit :)
bfont = ("Arial", 30, "bold")

#Entry setup
entry = ctk.CTkEntry(root, font=bfont, width=255, bg_color="#242424", fg_color="#242424", border_color="#242424", text_color="white")
entry.place(x=0, y=10)

#Buttons
bAC = ctk.CTkButton(root, font=("Arial", 26, "bold"), width=50, height=50, fg_color="#323232", border_color="#323232", text="%", bg_color="#242424", command=lambda:add_to_calculation("%"))
bAC.place(x=5, y=60)

bdiv = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#323232", border_color="#323232", text="÷", bg_color="#242424", command=lambda:add_to_calculation("/"))
bdiv.place(x=70, y=60)

bumult = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#323232", border_color="#323232", text="×", bg_color="#242424", command=lambda:add_to_calculation("*"))
bumult.place(x=135, y=60)

bbackspace = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#323232", border_color="#323232", text="AC", bg_color="#242424", command=clear_field)
bbackspace.place(x=200, y=60)

b7 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="7", bg_color="#242424", command=lambda:add_to_calculation(7))
b7.place(x=5, y=120)

b8 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="8", bg_color="#242424", command=lambda:add_to_calculation(8))
b8.place(x=70, y=120)

b9 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="9", bg_color="#242424", command=lambda:add_to_calculation(9))
b9.place(x=135, y=120)

bminus = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#323232", border_color="#323232", text="-", bg_color="#242424", command=lambda:add_to_calculation("-"))
bminus.place(x=200, y=120)

b4 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="4", bg_color="#242424", command=lambda:add_to_calculation(4))
b4.place(x=5, y=180)

b5 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="5", bg_color="#242424", command=lambda:add_to_calculation(5))
b5.place(x=70, y=180)

b6 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="6", bg_color="#242424", command=lambda:add_to_calculation(6))
b6.place(x=135, y=180)

bplus = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#323232", border_color="#323232", text="+", bg_color="#242424", command=lambda:add_to_calculation("+"))
bplus.place(x=200, y=180)

b1 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="1", bg_color="#242424", command=lambda:add_to_calculation(1))
b1.place(x=5, y=240)

b2 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="2", bg_color="#242424", command=lambda:add_to_calculation(2))
b2.place(x=70, y=240)

b3 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="3", bg_color="#242424", command=lambda:add_to_calculation(3))
b3.place(x=135, y=240)

import math
bsqrt = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="🙃", bg_color="#242424", command=lambda:smile())
bsqrt.place(x=5, y=300)

b0 = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#3b3b3b", border_color="#3b3b3b", text="0", bg_color="#242424", command=lambda:add_to_calculation("0"))
b0.place(x=70, y=300)

bdot = ctk.CTkButton(root, font=bfont, width=50, height=50, fg_color="#323232", border_color="#323232", text=".", bg_color="#242424", command=lambda:add_to_calculation("."))
bdot.place(x=135, y=300)

beq = ctk.CTkButton(root, font=bfont, width=50, height=110, fg_color="#323232", border_color="#323232", text="=", bg_color="#242424", command=evaluate_calculation)
beq.place(x=200, y=240)

root.mainloop()