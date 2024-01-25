import tkinter as tk

from main import DES_encrypt, DES_decrypt


def on_button1_click():
    # Function to handle the first button click
    plain_text = text1.get("1.0", "end-1c")  # Get the content of the Text widget
    key = text2.get()

    cipher_text = DES_encrypt(plain_text, key)

    text3.delete("1.0", tk.END)
    text3.insert(tk.END, cipher_text)


def on_button2_click():
    cipher_text = text1.get("1.0", "end-1c")  # Get the content of the Text widget
    key = text2.get()

    plain_text = DES_decrypt(cipher_text, key)

    text3.delete("1.0", tk.END)
    text3.insert(tk.END, plain_text)


# Create the main window
window = tk.Tk()
window.title("Data Encryption Standard")

# Label for the first input
label1 = tk.Label(window, text="INPUT:", font=("Helvetica", 14))
label1.pack(pady=5)

# Create the first Text widget
text1 = tk.Text(window, height=5, width=30, font=("Helvetica", 14))
text1.pack(pady=5, padx=10, expand=True, fill=tk.BOTH)

# Label for the second input
label2 = tk.Label(window, text="KEY:", font=("Helvetica", 14))
label2.pack(pady=5)

# Create the second Text widget
text2 = tk.Entry(window, width=30, font=("Helvetica", 14))
text2.pack(pady=5, padx=10, expand=True, fill="x")

# Label for the second input
label3 = tk.Label(window, text="OUTPUT:", font=("Helvetica", 14))
label3.pack(pady=5)

# Create the second Text widget
text3 = tk.Text(window, height=5, width=30, font=("Helvetica", 14))
text3.pack(pady=5, padx=10, expand=True, fill=tk.BOTH)

# Create the first button
button1 = tk.Button(window, text="Encrypt", command=on_button1_click, width=15, font=("Helvetica", 14))
button1.pack(side=tk.LEFT, pady=10, padx=10)

# Create the second button
button2 = tk.Button(window, text="Decrypt", command=on_button2_click, width=15, font=("Helvetica", 14))
button2.pack(side=tk.RIGHT, pady=10, padx=10)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the GUI event loop
window.geometry("500x700+10+10")
window.mainloop()
