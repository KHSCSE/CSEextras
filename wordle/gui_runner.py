# starter created by Gemini AI
import tkinter as tk


def submit_data():
    url = "https://www.nytimes.com/svc/wordle/v2/"
    
    """Reads the content of all three entry fields and prints it."""
    # We use .get() on each Entry widget to retrieve the current text
    field1_text = entry1.get()
    field2_text = entry2.get()
    field3_text = entry3.get()
    
    
    # format data
    
    
    # set URL
    
    
    # make request
    message = ""
    
    
    
    # view response
    result_label.config(text=message, fg="#008080") 




# 1. Create the main window
root = tk.Tk()
root.title("Multi-Field Form")
root.geometry("300x250") # Set a fixed size for better appearance


# --- Field 1 ---
tk.Label(root, text="Thing1:", anchor="w").pack(fill='x', padx=10, pady=(10, 0))
entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=(0, 5))


# --- Field 2 ---
tk.Label(root, text="Thing2:", anchor="w").pack(fill='x', padx=10, pady=(5, 0))
entry2 = tk.Entry(root)
entry2.pack(padx=10, pady=(0, 5))


# --- Field 3 ---
tk.Label(root, text="Thing3:", anchor="w").pack(fill='x', padx=10, pady=(5, 0))
entry3 = tk.Entry(root)
entry3.pack(padx=10, pady=(0, 10))


# --- Button ---
submit_button = tk.Button(root, text="Submit Data", command=submit_data, bg="#4CAF50", fg="white")
submit_button.pack(pady=10)


# --- New Label at the Bottom ---
# We store a reference to this label in 'result_label' so submit_data() can update it.
result_label = tk.Label(root, text="Click 'Submit Data' to see results.", fg="gray")
result_label.pack(pady=10)


# 4. Start the application loop
root.mainloop()
