
#gif

from PIL import Image,ImageDraw

images = []
width = 600
center = (width//2)
color_1 = (255,0,0)
color_2 = (0,0,0)
max_radius = int(center*1.5)
step = 8

for i in range(0, max_radius, step):
    square = Image.new('RGB', (width, width), color_2)
    my_square = ImageDraw.Draw(square)
    my_square.ellipse((center-i, center-i, center+i, center+i), fill=color_1)
    images.append(square)

images[0].save('pillow.imagedraw.gif', save_all=True, append_images=images[1:], optimize=False, duration=10)










