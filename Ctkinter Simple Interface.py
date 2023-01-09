import customtkinter as ctk
import os
from PIL import Image

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("400x200")
app.title("HD to SD")

frame_1 = ctk.CTkFrame(master=app, width= 5, height= 5)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


def button_event():
    global f
    #assing the path of the image to a variable
    f = ctk.filedialog.askdirectory()
    #return the path
      
button = ctk.CTkButton(frame_1, text="Select Skin Path", command=button_event)
button.pack(padx=20, pady=30)


def button_event_start():
    for file in os.listdir(f):
        #read only the images that ends with @2x.png
        if file.endswith('@2x.png'):
            f_img = f+"/"+file
            img = Image.open(f_img)
            #define width and height as variables
            (width, height) = img.width // 2, img.height // 2
            #for skiping errors, only resizes images that are greater than 1
            if width and height > 1:
                img = img.resize((width, height),resample=3)
                img.save(f_img)
    #renames that @2x.png image
    for file in os.listdir(f):
        if file.endswith('@2x.png'):
            old = f+"/"+file
            new = f+"/"+file.replace('@2x', '')
            os.replace(old, new)

button = ctk.CTkButton(frame_1, text='Start', command=button_event_start,)
button.pack(padx=20, pady=10)

app.mainloop()