from PIL import Image

im = Image.open('wordbase.png')
im = im.crop((0,304,640,1136))
im.save('cropped.png')
