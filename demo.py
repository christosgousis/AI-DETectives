import customtkinter
from tkinter import IntVar

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

choice = None

def toggle_combobox():
    global choice
    if checkbox_var.get() == 1:
        combobox_frame.pack(pady=(5, 10))
        output_frame.pack_forget()  
        output_text.pack_forget()  
    else:
        combobox_frame.pack_forget()  # Hide the combobox frame if the checkbox is not selected
        output_frame.pack_forget()  # Hide the scrollable frame if the checkbox is not selected
        choice = None 

def search(choice):
    keywords = entry.get()  
    if keywords:
        output_text.configure(text=f"Searching for: {keywords}")
        if choice:
            print(f"Performing data scraping with keywords: {keywords}")
            print(f"Selected option: {choice}")
        else:
            print(f"Performing data scraping with keywords: {keywords}")
            print("No department selected")
        output_frame.pack(pady=(5, 0), anchor="center")  # Show the scrollable frame under the combobox
        output_text.pack(pady=(5, 0), anchor="center") 
    else:
        output_text.pack_forget()  # Hide the output text label if no keywords are entered
        output_frame.pack_forget()  # Hide the scrollable frame if no keywords are entered

def on_combobox_change(*args):
    global selected_option
    selected_option = combobox.get()

def get_choice():
    global choice
    choice = combobox.get()
    search(choice)  # Call the search function with the selected choice

root = customtkinter.CTk()
root.geometry("600x750")
root.title("Nova AI Tool")

title_label = customtkinter.CTkLabel(master=root, text="Nova AI Tool", font=("Helvetica", 24, "bold"))
title_label.pack(pady=(50, 15)) 

description_label = customtkinter.CTkLabel(master=root, text="A revolutionary tool to streamline knowledge management.", font=("Helvetica", 13,))
description_label.pack()

keyword_entry_label = customtkinter.CTkLabel(master=root, text="Enter keywords separated by spaces:", font=("Helvetica", 16))
keyword_entry_label.pack(pady=6)

entry = customtkinter.CTkEntry(master=root, placeholder_text="e.g. United Group Nova", corner_radius=16, border_color="#436EEE", font=("Helvetica", 14))
entry.pack(pady=6)
entry.configure(width=300, height=30)

search_button = customtkinter.CTkButton(master=root, text="Search", font=("Helvetica", 14), corner_radius=32, command=get_choice, fg_color= "#436EEE")
search_button.pack(pady=10)
search_button.configure(width=90, height=30)

checkbox_var = IntVar()
checkbox = customtkinter.CTkCheckBox(master=root, text="I want to refine my search", variable=checkbox_var, command=toggle_combobox, font=("Helvetica", 13, "bold"))
checkbox.pack(pady=(10, 0))  

combobox_frame = customtkinter.CTkFrame(master=root)

combobox = customtkinter.CTkComboBox(master=combobox_frame, values=["Marketing", "Human Resources", "IT", "Sales"])
combobox.pack(pady=10)
combobox.configure(width=300, height=30)

# Create a scrollable frame for the output text
output_frame = customtkinter.CTkScrollableFrame(master=root, width=500, height=200)
output_text = customtkinter.CTkLabel(master=output_frame, text="", wraplength=400)

root.mainloop()
