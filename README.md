<p align="center">
<img src="https://github.com/shabir-mp/Express_Booking.id/assets/133546000/bdd17f65-b9e2-4fa4-aa2c-733342132033" width="150" />
<h1 align="center">Date and Time App v1.0.0</h1>
</p>

This project is a simple graphical user interface (GUI) application that displays the current date and time using Python's `tkinter` library. The time updates every second and this application has a clean and easy to view appearance. 

## About
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/shabir-mp/Image-Background-Remover/blob/main/LICENSE)

- **Developer:** Shabir Mahfudz Prahono - @shabir-mp
- **Application creation date:** 16 June 2024
## Features

- **Real-Time Clock:** The application updates the time every second.
- **Current Date Display:** The application displays the current date.
- **Neat appearance:** Neat and tidy application appearance.

## Preview
<p align="center">
<img src="https://github.com/shabir-mp/Caesar-Cipher-Encryptor-and-Decryptor/assets/133546000/40cb048f-c6d5-4b81-9fb3-7a3b990e7fa9" width="700" />
<h4 align="center">This is a preview of the date and time application by Shabir Mahfudz Prahono</h4>
</p>

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)
- `Pillow` library for handling images

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    ```
2. **Navigate to the project directory:**
    ```sh
    cd your-repo-name
    ```
3. **Install the required packages:**
    ```sh
    pip install Pillow
    ```

## Usage

1. **Place your icon image:**
   Ensure you have an icon image named `icon.png` in the same directory as the script. This image will be used as the window icon.

2. **Run the script:**
    ```sh
    python your_script_name.py
    ```
   Replace `your_script_name.py` with the name of your Python script file.

## Code Explanation

The main components of the script are:

1. **Imports:**
    - `tkinter` for creating the GUI.
    - `datetime` for getting the current date and time.
    - `PIL` (Pillow) for handling images.

    ```python
    import tkinter as tk
    from datetime import datetime
    from PIL import Image, ImageTk
    ```

2. **Update Time Function:**
    - This function gets the current date and time and updates the labels.
    - It also schedules itself to run again after 1 second (1000 milliseconds).

    ```python
    def update_time():
        current_time = datetime.now().strftime('%H:%M:%S')
        current_date = datetime.now().strftime('%Y-%m-%d')
        time_label.config(text=current_time)
        date_label.config(text=current_date)
        root.after(1000, update_time)
    ```

3. **Creating the Main Window:**
    - Initializes the main window.
    - Sets the window title, size, and icon.

    ```python
    root = tk.Tk()
    root.title("Date and Time")
    root.geometry("600x250")
    image = Image.open('icon.png') 
    icon = ImageTk.PhotoImage(image)
    root.iconphoto(False, icon)
    ```

4. **Labels for Time and Date:**
    - Creates and packs the labels for displaying the time and date.

    ```python
    label = tk.Label(root, bg='white')
    label.pack()
    time_label = tk.Label(label, font=('Kanit', 80), fg='black', bg='white')
    time_label.pack(pady=20)
    date_label = tk.Label(label, font=('Kanit', 24), fg='black', bg='white')
    date_label.pack(pady=0)
    ```

5. **Initial Update and Main Loop:**
    - Calls the `update_time` function to start the update cycle.
    - Starts the main loop of the `tkinter` window.

    ```python
    root.configure(bg='white')
    update_time()
    root.mainloop()
    ```

## Customization

- **Change Font:** You can change the font and size of the time and date labels by modifying the `font` parameter in the `tk.Label` definitions.
- **Change Colors:** You can change the foreground and background colors by modifying the `fg` and `bg` parameters in the `tk.Label` definitions.
- **Window Size:** You can adjust the window size by modifying the `root.geometry("600x250")` line.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

-----------------------------------------------------------------------------------------
![Github Footer](https://github.com/shabir-mp/Kereta-Api-Indonesia-Booking-System/assets/133546000/c1833fe4-f470-494f-99e7-d583421625be)
