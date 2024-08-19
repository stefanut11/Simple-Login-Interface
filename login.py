import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x300")

def login():
    print("GUI")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Update: Changed text_font to font
label = customtkinter.CTkLabel(master=frame, text="Thank you for visiting the app. Please login!", font=('Arial', 20))
label.pack(pady=20, padx=20)

# Update: Changed text to placeholder_text
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=10, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame, text="Log in", command=login)
button.pack(pady=10, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=10, padx=10)

root.mainloop()