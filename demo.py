import customtkinter
from tkinter import IntVar

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def toggle_combobox():
    if checkbox_var.get() == 1:
        combobox_frame.pack(pady=10)
    else:
        combobox_frame.pack_forget()

def search():
    keywords = entry.get()  # Get keywords from the entry widget
    output_text.configure(text=f"Searching for: {keywords}")  # Update the output text

root = customtkinter.CTk()
root.geometry("600x500")
root.title("Nova AI Tool")

title_label = customtkinter.CTkLabel(master=root, text="Nova AI Tool", font=("Helvetica", 24, "bold"))
title_label.pack(pady=(50, 15)) 

description_label = customtkinter.CTkLabel(master=root, text="A revolutionary tool to streamline knowledge management.", font=("Helvetica", 13, "italic"))
description_label.pack()

keyword_entry_label = customtkinter.CTkLabel(master=root, text="Enter keywords separated by spaces:", font=("Helvetica", 16))
keyword_entry_label.pack(pady=6)

entry = customtkinter.CTkEntry(master=root, placeholder_text="e.g. United Group Nova", corner_radius=16, border_color="#104E8B", font=("Helvetica", 14))
entry.pack(pady=6)
entry.configure(width=300, height=30)

search_button = customtkinter.CTkButton(master=root, text="Search", corner_radius=32, command=search)
search_button.pack(pady=10)
search_button.configure(width=50, height=20)

# Checkbox
checkbox_var = IntVar()
checkbox = customtkinter.CTkCheckBox(master=root, text="I want to refine my search", variable=checkbox_var, command=toggle_combobox, font=("Helvetica", 13, "bold"))
checkbox.pack(pady=10)

combobox_frame = customtkinter.CTkFrame(master=root)

# drop-down menu
combobox = customtkinter.CTkComboBox(master=combobox_frame, values=["Marketing", "Human Resources", "IT", "Sales"])
combobox.pack(pady=10)
combobox.configure(width=300, height=30)

output_text = customtkinter.CTkLabel(master=root, text="", wraplength=400)
output_text.pack(pady=10)

root.mainloop()
