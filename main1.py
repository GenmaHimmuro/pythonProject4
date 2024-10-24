from PIL import Image


image = Image.open("monro.jpg")
blue,green,red = image.split()

cropped_blue = blue.crop((25,0,671,image.height))
cropped_blue1=blue.crop((50 , 0, image.width,image.height))
image_blue1 = Image.blend(cropped_blue, cropped_blue1, 0.5)

cropped_red = red.crop((25,0,671,image.height))
cropped_red1 = red.crop((50 , 0, image.width,image.height))
image_red1 = Image.blend(cropped_red, cropped_red1, 0.5)

cropped_green=green.crop((25,0,671,image.height))

new_monro = Image.merge("RGB", (image_blue1, image_red1, cropped_green))
new_monro.save("new_monro.jpg")
new_monro_resize = Image.open("new_monro.jpg")
new_monro_resize.thumbnail((80,80))
new_monro_resize.save("new_monro_resize.jpg")
new_monro.show()
new_monro_resize.show()