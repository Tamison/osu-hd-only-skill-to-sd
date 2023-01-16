import sys 
import customtkinter as ctk
import shutil
import os
from PIL import Image
from time import sleep

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

winWidth = 440
winHeight = 270
iconPath = 'icon.ico'
skinFolderPath = 'skin.path'
locationPath = os.path.realpath(os.path.dirname(__file__))




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('HDtoSD')
        self.geometry(f'{winWidth}x{winHeight}')
        self.minsize(width= winWidth, height= winHeight)
        self.maxsize(width= winWidth, height= winHeight)
        self.configure(fg_color = "#101010")


        self.main_frame = ctk.CTkFrame(self, width=5, height=5, fg_color='#151515')
        self.main_frame.grid(row = 0, column = 0,padx = (20,20), pady = (20,20), sticky = 'nsew')

        self.blending_mode_section =ctk.CTkFrame(self, fg_color='#151515')
        self.blending_mode_section.grid(row=0, column=1, padx=(0, 20), pady=(20, 20), sticky="nsew")
        self.radio_var = ctk.IntVar(value=-1)
        self.label_radio_group = ctk.CTkLabel(master=self.blending_mode_section, text="Blending Mode")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=0, sticky="")
        self.radio_button_1 = ctk.CTkRadioButton(self.blending_mode_section, variable = self.radio_var, text = 'NEAREST', value=0)
        self.radio_button_1.grid(row=1, column=2, pady=5, padx=20, sticky="n")
        self.radio_button_2 = ctk.CTkRadioButton(self.blending_mode_section, variable = self.radio_var, text = 'LANCZOS', value=1)
        self.radio_button_2.grid(row=2, column=2, pady=5, padx=20, sticky="n")
        self.radio_button_3 = ctk.CTkRadioButton(self.blending_mode_section, variable = self.radio_var, text = 'BILINEAR', value=2)
        self.radio_button_3.grid(row=3, column=2, pady=5, padx=20, sticky="n")
        self.radio_button_4 = ctk.CTkRadioButton(self.blending_mode_section, variable = self.radio_var, text = 'BICUBIC', value=3)
        self.radio_button_4.grid(row=4, column=2, pady=5, padx=20, sticky="n")
        self.radio_button_5 = ctk.CTkRadioButton(self.blending_mode_section, variable = self.radio_var, text = 'BOX', value=4)
        self.radio_button_5.grid(row=5, column=2, pady=5, padx=20, sticky="n")
        self.radio_button_6 = ctk.CTkRadioButton(self.blending_mode_section, variable = self.radio_var, text = 'HAMMING', value=5)
        self.radio_button_6.grid(row=6, column=2, pady=5, padx=20, sticky="n")


        self.combobox_1 = ctk.CTkComboBox(self.main_frame)
        self.combobox_1.pack(padx = 20, pady = (20, 10))
        self.combobox_1.set("Select a skin")

        self.switch_1 = ctk.CTkSwitch(self.main_frame, onvalue="on", offvalue="off", text="SDtoHD",text_color='white',fg_color='#101010',
                                progress_color='white',
                                button_color='grey',
                                button_hover_color='#575757')
        self.switch_1.pack(padx=(20,20), pady=(20,5))
        self.switch_1_var = ctk.StringVar(self.main_frame, value="off")

        self.button_1 = ctk.CTkButton(self.main_frame)
        self.button_1.pack(padx = (20,20), pady = (10,10))

        self.button_2 = ctk.CTkButton(self.main_frame)
        self.button_2.pack(padx = (20,20), pady = (10,30))




        #Cofiguration
        self.combobox_1.configure(  
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

        self.button_1.configure(
                                text = 'Start',
                                fg_color = 'black',
                                text_color = 'white',
                                border_color = 'white',
                                hover_color = 'grey',
                                border_width = 2,
        )

        self.button_2.configure( 
                                text = 'Reload Skins',
                                fg_color = 'black',
                                text_color = 'white',
                                border_color = 'white',
                                hover_color = 'grey',
                                border_width = 2,
        )
        


        

    
    #Functions
    def icon_exist(self, iconPath):
        if os.path.isfile(iconPath):
            app.iconbitmap(iconPath)
        else:
            pass

    def is_skin_path(self):
        if os.path.isfile(skinFolderPath):
            with open(skinFolderPath, 'r+') as fp:
                if len(fp.readline()) == 0:
                    f= ctk.filedialog.askdirectory()
                    fp.write(f)
                else:
                    with open(skinFolderPath, 'r') as fp:
                        f = fp.read()
        else:
            f= ctk.filedialog.askdirectory()
            open(os.path.join(locationPath, skinFolderPath), 'x')
            with open(skinFolderPath, 'w') as fp:
                fp.write(f)
        return f

    def check_f(self, f):
        if not f:
            sys.exit('Not F')

    def combobox_1_values(self, f):
        def combobox_callback(choice):
            global f
            with open(skinFolderPath, 'r') as fp:
                f = fp.read()
            f = f+'/'+choice
            print(f)
        self.combobox_1.configure(values = [file for file in os.listdir(f)], command = combobox_callback)


    def radiobutton_state(self):
        radio = [
            self.radio_button_1,
            self.radio_button_2,
            self.radio_button_3,
            self.radio_button_4,
            self.radio_button_5,
            self.radio_button_6,
            ]

        if self.switch_1_var.get() == "on":    
            for radial in radio:
                radial.configure(state = 'normal', text_color = 'white', fg_color='white',hover_color = '#AAAAAA',border_width_checked = 3, border_color = '#505050',hover = True)
            self.label_radio_group.configure(text_color = 'white')
        else:
            for radial in radio:
                radial.configure(state = 'disable', text_color = '#303030', border_color = '#202020',fg_color ='#202020',hover = False )
            self.label_radio_group.configure(text_color = '#303030')
            

    def switch_value(self):
        print('Swith is:', self.switch_1_var.get())

    def switch_HD(self):
        self.switch_1.configure(variable = self.switch_1_var, command = self.radiobutton_state)

    def done_window(self):
        window = ctk.CTkToplevel(app)
        window.title('Done!')
        window.geometry('120x0')
        window.maxsize(width=120, height=0)
        window.minsize(width=120, height=0)

    def button_1_event_start(self):
        if self.switch_1_var.get() == "off":
            back = f+'/Backup'
            if not os.path.isdir(back):
                os.mkdir(back)
                back = back+'/HDtoSD'
                os.mkdir(back)
            else:
                back = back+'/HDtoSD'

            for file in os.listdir(f):
                if file.endswith('@2x.png'):
                    f_img = f+"/"+file
                    f_img_back = back+"/"+file
                    shutil.copy(f_img, f_img_back)
                    img = Image.open(f_img)
                    (width, height) = img.width // 2, img.height // 2
                    if width and height > 1:
                        img = img.resize((width, height),resample=1)
                        img.save(f_img)
            for file in os.listdir(f):
                if file.endswith('@2x.png'):
                    old = f+"/"+file
                    new = f+"/"+file.replace('@2x', '')
                    os.replace(old, new)
            sleep(2)
            app.done_window()

        else:
            for file in os.listdir(f):
                if file.endswith('.png') and not file.endswith('@2x.png'):
                    old = f+"/"+file
                    new = f+"/"+file.replace('.png', '@2x.png')
                    shutil.copyfile(old, new)
            for file in os.listdir(f):
                if file.endswith('@2x.png'):
                    f_img = f+"/"+file
                    img = Image.open(f_img)
                    (width, height) = img.width * 2, img.height * 2
                    if width and height > 1:
                        img = img.resize((width, height),resample=self.radio_var.get())
                        img.save(f_img)
            sleep(2)
            app.done_window()


    def button_1_event(self):
        self.button_1.configure(command = app.button_1_event_start)
        
    def button_2_event(self):
        def reload():
            with open(skinFolderPath, 'r') as fp:
                f = fp.read()
            self.combobox_1.configure(values=[file for file in os.listdir(f)])
        self.button_2.configure(command = reload)



if __name__ == "__main__":
    app = App()
    f = app.is_skin_path()
    app.icon_exist(iconPath)
    app.check_f(f)
    app.combobox_1_values(f)
    app.switch_HD()
    app.radiobutton_state()
    app.button_1_event()
    app.button_2_event()
    app.mainloop()