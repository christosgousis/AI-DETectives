import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def search():
    keywords = entry.get()  # Get keywords from the entry widget
    output_text.configure(text=f"Searching for: {keywords}")  # Update the output text

root = customtkinter.CTk()
root.geometry("600x500")
root.title("Nova AI Tool")

title_label = customtkinter.CTkLabel(master=root, text="Nova AI Tool", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

description_label = customtkinter.CTkLabel(master=root, text="A revolutionary tool to streamline knowledge management.", font=("Helvetica", 12, "italic"))
description_label.pack()

keyword_entry_label = customtkinter.CTkLabel(master=root, text="Enter keywords separated by spaces:")
keyword_entry_label.pack(pady=6)

entry = customtkinter.CTkEntry(master=root, placeholder_text="e.g., United Group Nova")
entry.pack(pady=6)
entry.configure(width=300, height=30)

search_button = customtkinter.CTkButton(master=root, text="Search", command=search)
search_button.pack(pady=6)
search_button.configure(width=50, height=20)

output_text = customtkinter.CTkLabel(master=root, text="", wraplength=400)
output_text.pack(pady=10)

root.mainloop()
