import tkinter as tk
from tkinter import scrolledtext

def count_words():
    text = text_area.get("1.0",'end-1c')
    word_count = len(text.split())
    result_label.config(text=f"Word Count: {word_count}")

# Create the main window
window = tk.Tk()
window.title("Word Counter")

# Create a Text widget for user input
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# Create a button to trigger the word count
count_button = tk.Button(window, text="Count Words", command=count_words)
count_button.pack()

# Display the word count result
result_label = tk.Label(window, text="Word Count: 0")
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
