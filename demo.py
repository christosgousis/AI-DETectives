import customtkinter
from tkinter import IntVar

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def toggle_combobox():
    if checkbox_var.get() == 1:
        combobox_frame.pack(pady=(5, 10))  # Adjust the top and bottom padding of the combobox frame
        output_text.pack_forget()  # Hide the output text label if the combobox is selected
    else:
        combobox_frame.pack_forget()  # Hide the combobox frame if the checkbox is not selected
        output_text.pack(pady=(5, 0), anchor="center") 
        
def search():
    keywords = entry.get()  
    if keywords:
        output_text.configure(text=f"Searching for: {keywords}") 
        output_text.pack(pady=(5, 0), anchor="center") 
    else:
        output_text.pack_forget()  

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

checkbox_var = IntVar()
checkbox = customtkinter.CTkCheckBox(master=root, text="I want to refine my search", variable=checkbox_var, command=toggle_combobox, font=("Helvetica", 13, "bold"))
checkbox.pack(pady=(10, 0))  # Adjusting the top padding only

combobox_frame = customtkinter.CTkFrame(master=root)

combobox = customtkinter.CTkComboBox(master=combobox_frame, values=["Marketing", "Human Resources", "IT", "Sales"])
combobox.pack(pady=10)
combobox.configure(width=300, height=30)

output_text = customtkinter.CTkLabel(master=root, text="", wraplength=400)
output_text.pack(pady=(5, 0), anchor="center")  

root.mainloop()
