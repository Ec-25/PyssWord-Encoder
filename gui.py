import tkinter as tk
import pyperclip
import codex as cdx


# Define function to clear input boxes
def clean():
    inputBox_password.delete(0, tk.END)
    inputBox_result.delete(0, tk.END)

# Define the function to copy the text of the input box
def copy():
    texto = inputBox_result.get()
    pyperclip.copy(texto)

# Define the function to encode password
def encode():

    return

# Define the function to decode password
def decode():

    return

# Create the main window
window = tk.Tk()

# Set window size and title
window.geometry("600x300")
window.resizable(False, False)
window.title("PyssWord Encoder")

# Add an icon to the window
window.iconbitmap("icon.ico")

# Create the widgets
font = ("Helvetica", 14)  # Set the typeface and font size
bg_color = "#4c4c4c"  # Set the background color of widgets
fg_color = "#f6f6f6"  # Set the font color
input_box_state = "readonly"  # Set input box state
window.config(bg="#0f0f0f")  # Change the background color of the window

label_password = tk.Label(window, text="Password:",
                          font=font, bg="#0f0f0f", fg=fg_color)
inputBox_password = tk.Entry(
    window, width=26, font=font, bg=bg_color, fg=fg_color)
label_result = tk.Label(window, text="Result:", font=font,
                         bg="#0f0f0f", fg=fg_color)
inputBox_result = tk.Entry(window, width=26, font=font,
                            bg=bg_color, fg=fg_color, state=input_box_state)
button_copy = tk.Button(window, text="Copy", width=20, height=1,
                        font=font, bg=bg_color, fg=fg_color, command=copy)
button_clean = tk.Button(window, text="Clean", width=20,
                         height=1, font=font, bg=bg_color, fg=fg_color, command=clean)
button_encode = tk.Button(window, text="Encode", width=20,
                            height=1, font=font, bg=fg_color, fg=bg_color, command=encode)
button_decode = tk.Button(window, text="Decode", width=20,
                            height=1, font=font, bg=fg_color, fg=bg_color, command=decode)

# Position widgets in the window using the place method
label_password.place(relx=0.3, rely=0.2, anchor="center")
inputBox_password.place(relx=0.65, rely=0.2, anchor="center")
label_result.place(relx=0.3, rely=0.4, anchor="center")
inputBox_result.place(relx=0.65, rely=0.4, anchor="center")
button_copy.place(relx=0.3, rely=0.6, anchor="center")
button_clean.place(relx=0.7, rely=0.6, anchor="center")
button_encode.place(relx=0.3, rely=0.8, anchor="center")
button_decode.place(relx=0.7, rely=0.8, anchor="center")
