from PIL import Image 
import os

fit_size = int(input('Enter Size : '))
output_folder = input('Enter output folder name : ')

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for imagename in os.listdir('.') :
    if not imagename.endswith((".png" , ".jpg" , "jpeg")):
        continue


    # open the image --> get image size --> resize

    image = Image.open(imagename)
    width , height = image.size

    # image should be greated than the fit value
    if width > fit_size and height > fit_size : 
        if width > height:
            height = int((fit_size/width)*height)
            width = fit_size
        else :
            width = int((fit_size/height)*width)
            height = fit_size

        image = image.resize((width , height))
        print('resizing : %s ' %(imagename))

    image = image.save(os.path.join(output_folder , imagename))

    print('_______________') 

print("done resizing all images")           