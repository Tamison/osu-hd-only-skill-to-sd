import customtkinter as ctk
import os
from PIL import Image


icon_path = 'icon.ico'

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry(f"{300}x{250}")
app.minsize(width=300, height=250)
app.maxsize(width=300, height=250)
app.configure(fg_color = '#101010')
app.title("HD to SD")

if os.path.isfile(icon_path):
    app.iconbitmap(icon_path)
else:
    pass

frame_1 = ctk.CTkFrame(master=app, 
                       width= 5, 
                       height= 5,
                       fg_color='#151515',
                       )
frame_1.pack(pady=20, padx=30, fill="both", expand=True)

#program self.location
path = os.path.realpath(os.path.dirname(__file__))

#check if there's a skin.path at the program location
if os.path.isfile('skin.path'):
    with open('skin.path', 'r+') as fp:
        if len(fp.readline()) == 0:
           f= ctk.filedialog.askdirectory()
           fp.write(f)
           fp.close()
        else:
            with open('skin.path', 'r') as fp:
                #set 'f' as skin.path content
                f = fp.readline()
                fp.close()
#if not skin.path
else:
    #ask for a diretory
    f= ctk.filedialog.askdirectory()
    #create a skin.path
    open(os.path.join(path, 'skin.path'), 'x')
    #write the 'f' in the skin.path file
    with open('skin.path', 'w') as fp:
        fp.write(f)
        fp.close()
       

combobox_var = ctk.StringVar(value="Select a skin")  # set initial value

#callback for the combobox
def combobox_callback(choice):
    #define 'f' as a global variable
    global f
    #reset 'f' as the skin.path 
    with open('skin.path', 'r') as fp:
        f = fp.readline()
        fp.close()
    #set 'f' as skin.path + skin_combobox content
    f = f+'/'+choice
    #print for debug
    # print("optionmenu dropdown clicked:", choice)



#skins_combobox
combobox = ctk.CTkComboBox(frame_1, 
                                    #loop the skin folder content to a file list
                                    values = [file for file in os.listdir(f)],
                                    command = combobox_callback,    
                                    variable = combobox_var,
                                    width = 200,
                                    height = 30,
                                    fg_color = 'black',
                                    text_color = 'white',
                                    border_color ='white',
                                    border_width = 2,
                                    button_color = 'grey',
                                    button_hover_color = '#474747',
                                    dropdown_fg_color = 'black',
                                    dropdown_text_color = 'white',
                                    dropdown_hover_color = '#474747',
                                    justify = 'center'
                                    )
combobox.pack(padx=20, pady=30)


#reload
def reload():
    #reset 'f' as the skin.path 
    with open('skin.path', 'r') as fp:
        f = fp.readline()
        fp.close()
    combobox.configure(values=[file for file in os.listdir(f)])

#start the convertion
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
    window = ctk.CTkToplevel(app)
    window.title('Done!')
    window.geometry('120x0')
    window.maxsize(width=120, height=0)
    window.minsize(width=120, height=0)
    


def button_1():
    button_1 = ctk.CTkButton(frame_1, text='Start', command=button_event_start)
    button_1.pack(padx=20, pady=10)
    button_1.configure(fg_color = 'black',
                       text_color = 'white',
                       border_color = 'white',
                       hover_color = 'grey',
                       border_width = 2,
                       )

def button_2():
    button_2 = ctk.CTkButton(frame_1, text='Reload Skins', command=reload)
    button_2.pack(padx=20, pady=10)
    button_2.configure(fg_color = 'black',
                       text_color = 'white',
                       border_color = 'white',
                       hover_color = 'grey',
                       border_width = 2,
                       )


button_1()
button_2()  
app.mainloop()
