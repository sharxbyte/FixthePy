import openai
import sys
import os
import time
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from PIL import Image, ImageTk


# Set OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define function to correct code
def correct_code(code):
    # Initialize variables
    corrected_code = ''
    start_index = 0
    end_index = 4096
    line_number = 1
    
    # Loop through code in blocks of 4096 tokens
    while start_index < len(code):
        # Get the next block of code
        code_block = code[start_index:end_index]
        
        # Call the OpenAI API to correct the code block
        prompt = f"Please correct the following Python code:\n\n{code_block}\n\nLine {line_number}: "
        response = openai.Completion.create(engine="davinci-codex", prompt=prompt, max_tokens=4096, n=1, stop=None, temperature=0.7)
        corrected_text = response.choices[0].text.strip()
        
        # Add the corrected code block to the corrected code
        corrected_code += corrected_text
        
        # Update the start and end indices for the next block of code
        start_index = end_index
        end_index += 4096
        
        # Find the nearest line break to the end of the block
        last_line_break = corrected_code.rfind('\n', 0, end_index)
        if last_line_break > start_index:
            end_index = last_line_break
        
        # Increment the line number
        line_number += corrected_text.count('\n') + 1
    
    # Write the corrected code to a file
    with open("corrected_code.txt", "a") as f:
        f.write(corrected_code)

    return corrected_code

# Define function to read code from a file
def read_code(filename):
    with open(filename, "r") as f:
        return f.read()

# Define function to write code to a file
def write_code(filename, code):
    with open(filename, "w") as f:
        f.write(code)

# Define main function
def main():
    # Create a basic tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Create the splash window
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash_image_path = os.path.join(os.path.dirname(sys.executable), "splash.png")
    splash_img = ImageTk.PhotoImage(Image.open(splash_image_path))
    splash_label = tk.Label(splash, image=splash_img)
    splash_label.pack()

    # Center the splash window on the screen
    splash.update_idletasks()
    width = splash.winfo_width()
    height = splash.winfo_height()
    x = (splash.winfo_screenwidth() // 2) - (width // 2)
    y = (splash.winfo_screenheight() // 2) - (height // 2)
    splash.geometry("{}x{}+{}+{}".format(width, height, x, y))

    # Define a function to hide the splash window
    def hide_splash():
        for i in range(6):
            alpha = splash.attributes("-alpha")
            alpha -= 0.06
            splash.attributes("-alpha", alpha)
            splash.update_idletasks()
            time.sleep(0.009)
        splash.destroy()

    # Schedule the function to hide the splash window
    splash.after(7500, hide_splash)

    root.update()

    # Ask the user for their API key
    api_key = simpledialog.askstring("API Key", "Please enter your API key:", parent=root)
    if api_key is not None:
        openai.api_key = api_key
    else:
        messagebox.showinfo("Info", "No API key entered. Exiting the application.")
        root.destroy()
        return

    # Get the name of the file to correct
    filename = filedialog.askopenfilename(title="Select the file to correct", filetypes=(("Python files", "*.py"), ("All files", "*.*")))
    if not filename:
        messagebox.showinfo("Info", "No file selected. Exiting the application.")
        root.destroy()
        return

    # Read the code from the file
    code = read_code(filename)

    # Correct the code
    corrected_code = correct_code(code)

    # Save the corrected code to a new file with the same filename but with "_fixed" added to the end and with a ".py" extension
    file_base, file_ext = os.path.splitext(filename)
    fixed_filename = f"{file_base}_fixed.py"
    write_code(fixed_filename, corrected_code)

    messagebox.showinfo("Info", f"Done! The corrected code has been saved to '{fixed_filename}'.")
    root.destroy()

# Call the main function
if __name__ == "__main__":
    main()
