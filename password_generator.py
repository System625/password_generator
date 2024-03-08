from tkinter import *
from random import randint

root = Tk()
root.title("My Personal Password Generator")
root.iconbitmap("C:/Users/Olamiposi/OneDrive/Documents/posi/python/beginnerCourse/avatar.ico")
root.geometry("500x300")

my_password = chr(randint(33, 126))

# Generate Random Strong Password Generator
def new_rand():
    # Clean our Entry Box
    pw_entry.delete(0, END)
    
    # Get PW Length and convert to integer
    pw_length = int(my_entry.get())
    
    # Create a Variable to Hold our Password
    my_password = ""
    
    # Loop Through Password Length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
        
    # Output Password to the Screen
    pw_entry.insert(0, my_password)
    
    # Copy to Clipboard
def clipper():
    # Clear the Clipboard
    root.clipboard_clear()
    # Copy to Clipboard
    root.clipboard_append(pw_entry.get())
    
def save_to_file():
    # Save the generated password to a text file
    password = pw_entry.get()
    with open("generated_password.txt", "w") as file:
        file.write(password)
    status_label.config(text="Password saved to generated_password.txt")
    

# Label Frame
lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

# Crate Entry Box to Designate Number of Characters
my_entry = Entry(lf, font=("Heveltica", 24))
my_entry.pack(pady=20, padx=20)

# Create an Entry Box for our Returned Password
pw_entry = Entry(root, text="", font=("Heveltica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Create a frame for our Buttons

my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Generate a Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

save_button = Button(my_frame, text="Save to File", command=save_to_file)
save_button.grid(row=0, column=2, padx=5)

# Label to display status
status_label = Label(root, text="")
status_label.pack()


root.mainloop()