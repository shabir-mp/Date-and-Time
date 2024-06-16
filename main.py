import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

# Function to update the time and date
def update_time():
    # Get the current time and date
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Update the labels with the current time and date
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # Schedule the update_time function to be called after 1000 milliseconds (1 second)
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Date and Time")
root.geometry("600x250")
image = Image.open('icon.png') 
icon = ImageTk.PhotoImage(image)

# Set the icon for the window
root.iconphoto(False, icon)

# Set label
label = tk.Label(root, bg='white')
label.pack()

# Create and pack the time label
time_label = tk.Label(label, font=('Kanit', 80), fg='black', bg='white')
time_label.pack(pady=20)

# Create and pack the date label
date_label = tk.Label(label, font=('Kanit', 24), fg='black', bg='white')
date_label.pack(pady=0)

# Set the window background color
root.configure(bg='white')

# Call the update_time function to update the time initially
update_time()

# Start the main loop of the tkinter window
root.mainloop()
