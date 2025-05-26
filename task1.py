from tkinter import *

window = Tk()
window.title("MADHU")
window.config(bg="#F0F8FF")

# Registration Form Title
label1 = Label(window, text="REGISTRATION FORM", font=("Times", 16, "bold"), bg="#F0F8FF", fg="dark blue", pady=10)
label1.grid(row=1, column=0, columnspan=2)

# Name
label2 = Label(window, text="NAME" , font=("Times", 14, "bold"), bg="#F0F8FF", fg="black", pady=10)
label2.grid(row=2, column=0)
entry = Entry(window, font=("Times", 14, "bold italic"))
entry.grid(row=2, column=1)

# Email
label3 = Label(window, text="E-MAIL", font=("Times", 14, "bold"), bg="#F0F8FF", fg="black", pady=10)
label3.grid(row=3, column=0)
entry1 = Entry(window, font=("Times", 14, "bold italic"))
entry1.grid(row=3, column=1)

# Address
label4 = Label(window, text="ADDRESS", font=("Times", 14, "bold"), bg="#F0F8FF", fg="black", pady=10)
label4.grid(row=4, column=0)
entry2 = Entry(window, font=("Times", 14, "bold italic"))
entry2.grid(row=4, column=1)

# Mobile No
label5 = Label(window, text="MOBILE NO", font=("Times", 14, "bold"),bg="#F0F8FF", fg="black", pady=10)
label5.grid(row=5, column=0)
entry3 = Entry(window, font=("Times", 14, "bold"))
entry3.grid(row=5, column=1)

# Submit Button
button = Button(window, text="Submit", fg="blue", padx=15, pady=5, width=5)
button.grid(row=6, column=0)
button.config(bg="#FFFACD")

# Clear Button
button1 = Button(window, text="Clear", fg="blue", padx=15, pady=5, width=5)
button1.grid(row=6, column=1)
button1.config(bg="#FFFACD")

# Window Size
window.geometry("800x600")
window.mainloop()
