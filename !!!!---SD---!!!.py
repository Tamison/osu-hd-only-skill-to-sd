import os
from PIL import Image
from progressbar import ProgressBar
def main():
    def sd_converter():
        pbar = ProgressBar()
        #assign the path of the images to a variable:
        f = os.path.realpath(os.path.dirname(__file__))
        path_2 = '% '+f+' %'
        path = ['%' for letter in path_2]
        print(*path, sep = '')
        print(path_2)
        print(*path, sep = '')
        #loop images and resizing it
        for file in pbar(os.listdir(f)):
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
        print('Done!!!!')
        print("Made by: Numbers")
    sd_converter()
if __name__ == '__main__':
    main()
