from PIL import Image

# resize to 640 x 1136 before doing anything
im = Image.open('wordbase.png')
im = im.crop((0,304,640,1136))
im.save('cropped.png')
