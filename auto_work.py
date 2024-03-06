'''
MANIPULATING IMAGES

Photos

need to edit a massive number of images


Pillow: crop, resize, and edit the content of an image
All the rotations, resizing, cropping, drawing, and other image manipulations will be done through method calls on this Image object.

The origin is the pixel at the top-left corner of the image and is specified with the notation (0, 0). 
Coordinates and Box Tuples: Many of Pillow’s functions and methods take a box tuple argument, like (3, 1, 9, 6), which is (Left, Top, Right, Bottom).
'''
from PIL import ImageColor
from PIL import Image


aIm = Image.open('zophie.png')
aIm.save('zophie.jpg')

width, height = aIm.size
# catIm.format_description
print(f"{aIm.filename}, {aIm.format}")



cIm = aIm.crop((335, 345, 565, 560)) # exclusive
cIm.save('cropped.png')

dIm = aIm.copy()
dIm.paste(cIm, (0, 0))

x, y = dIm.size[0]-cIm.size[0], dIm.size[1]-cIm.size[1]
dIm.paste(cIm, (x, y))

eIm = aIm.resize((int(width / 2), int(height / 2)))
eIm.save('quartersized.png')

aIm.rotate(90).save('rotated90.png')

fIm = aIm.rotate(7, expand=True)
fIm.save('rotated7_expanded.png')


gIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
gIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')






from PIL import Image, ImageColor


def change_individual_pixels():
    # Create a new RGBA image with dimensions 100x100
    im = Image.new('RGBA', (100, 100))
    # bIm = Image.new('RGBA', (100, 200), 'purple') # ('purple' can be omitted which means Invisible black, (0, 0, 0, 0), is the default color used if no color argument is specified

    # Set the pixels in the top half of the image to (210, 210, 210, 255)
    for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (210, 210, 210, 255))

    # Set the pixels in the bottom half of the image to 'darkgray'
    for x in range(100):
        for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
            # get RGBA values from color name
            # ImageColor.getcolor('red', 'RGBA') # case-insensitive

    # Print the pixel values at specific coordinates
    print(im.getpixel((0, 0)))    # (210, 210, 210, 255)
    print(im.getpixel((0, 50)))   # (169, 169, 169, 255)

    # Save the image
    im.save('putPixel.png')




from PIL import Image
# tile Zophie’s head across the entire image
def tile_object_across_background(background_path, object_path, output_path):
    # Open the images
    background = Image.open(background_path)
    obj = Image.open(object_path)

    # Get image dimensions
    background_width, background_height = background.size
    obj_width, obj_height = obj.size

    # Create a copy of the background image
    result_image = background.copy()

    # Iterate over positions and paste the object image
    for left in range(0, background_width, obj_width):
        for top in range(0, background_height, obj_height):
            result_image.paste(obj, (left, top))

    # Save the result
    result_image.save(output_path)

# the boring job of resizing thousands of images and adding a small logo watermark to the corner of each.
    



#!/usr/bin/env python3
from PIL import Image
import os

def resize_and_add_logo(input_dir='.', output_dir='withLogo', square_fit_size=300, logo_filename='catlogo.png'):
    # Load the logo image
    logo_im = Image.open(logo_filename)
    logo_width, logo_height = logo_im.size
    print(f"Logo dimensions: {logo_width} x {logo_height}")

    # Create a directory to store images with logos
    os.makedirs(output_dir, exist_ok=True)

    # Loop over all files in the input directory
    for filename in os.listdir(input_dir):
        # Skip non-image files and the logo file itself
        if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_filename:
            continue

        # Open the image
        im = Image.open(os.path.join(input_dir, filename))
        width, height = im.size
        print(f"Original image dimensions: {width} x {height}")
        ori_width, ori_height = width, height

        # Check if the image needs to be resized
        if width > square_fit_size or height > square_fit_size:
            # Calculate the new width and height to resize to
            if width > height:
                height = int((square_fit_size / width) * height)
                width = square_fit_size
            else:
                width = int((square_fit_size / height) * width)
                height = square_fit_size

            # Resize the image
            print(f'Resizing {filename}... from original ({ori_width}, {ori_height}) to ({width}, {height}).')
            im = im.resize((width, height))

        # Add the logo to the lower-right corner
        print(f'Adding logo to {filename}...')
        logo_im_resized = logo_im.resize((int(min(width, height) * 1/10), int(min(width, height) * 1/10 * logo_height/logo_width)))
        logo_resized_width, logo_resized_height = logo_im_resized.size
        im.paste(logo_im_resized, (width - logo_resized_width, height - logo_resized_height), logo_im_resized)

        # Save changes
        im.save(os.path.join(output_dir, filename))

# Example usage
# resize_and_add_logo(input_dir='.', output_dir='withLogo', square_fit_size=300, logo_filename='catlogo.png')



'''PATTERN MATCHING WITH REGULAR EXPRESSIONS


ttps://pythex.org/.

'''





'''
My work:
Ideas for Similar Programs
Being able to composite images or modify image sizes in a batch can be useful in many applications. You could write similar programs to do the following:

Add text or a website URL to images.
Add timestamps to images.
Copy or move images into different folders based on their sizes.
Add a mostly transparent watermark to an image to prevent others from copying it.'''


from PIL import Image, ImageDraw

# Create a new RGBA image with a white background
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# Draw a black square
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')

# Draw a blue rectangle
draw.rectangle((20, 30, 60, 60), fill='blue')

# Draw a red ellipse (or circle in this case)
draw.ellipse((120, 30, 160, 60), fill='red')

# Draw a brown polygon
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')

# Draw green lines
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

# Save the image
im.save('drawing.png')



from PIL import Image, ImageDraw, ImageFont
import os

# Create a new RGBA image with a white background
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# Draw text using the default font
draw.text((20, 150), 'Hello', fill='purple')

# Specify a custom font (Arial in this case)
fonts_folder = 'FONT_FOLDER'  # Replace with the actual path to your font folder
arial_font_path = os.path.join(fonts_folder, 'arial.ttf')
arial_font = ImageFont.truetype(arial_font_path, 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arial_font)

# Save the image
im.save('text.png')







def make_66_plans():
    import pyperclip as p
    import random as r
    text = p.paste().strip()
    lines = text.split('\n')
    print(f'Lines found: {len(lines)}')
    if len(lines) < 36:
        lines.extend(["contiue"]*(36-len(lines)))
    r.shuffle(lines)
    pre_plans = lines[:36]
    plans = []
    for i in range(1,7):
        for j in range(1, 7):
            plans.append(f"D{i}{j}-{pre_plans.pop()}")
    print(plans)
    txt = '\n'.join(plans).strip()
    p.copy(txt)

    
import re
phoneNumRegex = re.compile(r'((\d\d\d)|(\(\d\d\d\))-)?(\d\d\d-\d\d\d\d)') # The first set of parentheses in a regex string will be group 1
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo = phoneNumRegex.search('My number is (415)-555-4242.')
mo = phoneNumRegex.search('My number is 555-4242.')
print(f'{mo.group(1)}, {mo.group(0)}, {mo.group()}, {mo.groups()}')
# Passing 0 or nothing to the group() method will return the entire matched text. 
# If you would like to retrieve all the groups at once, use the groups() method

def magic(temp):
    ts = temp.group(1)
    ts_all = temp.group()
    return rf"{ts}{'*'*(len(ts_all)-7)}"

sample_str =  'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****',sample_str)
agentNamesRegex.sub(magic, sample_str)
agentNamesRegex.sub(lambda mo:mo.group(1).title(), sample_str)

def m():
    import pyperclip as p
    import re
    original_txt = p.paste()
    re_obj = re.compile(r'第(\d)章')
    re_obj = re.compile(r'\d,\s+\w*.+')
    re_obj = re.compile(r"\{% static '(.*?)' %\}") # {% static 'css/nucleo-icons.css' %}
    new_txt = re_obj.sub(r"{% static 'new_/\1' %}", original_txt)
    # txt_lt = re_obj.findall(original_txt)
    p.copy(new_txt)
    # p.copy('\n'.join(txt_lt).strip())


'''


PATTERN MATCHING WITH REGULAR EXPRESSIONS
https://pythex.org/


In regular expressions, the following characters have special meanings: 
.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )


'''


'''
都可缓存，可累加

学习自动化20分钟 
做自己网站-15分钟
PS-10分钟
了解工作10分钟
看书5分钟
学习视频剪辑10分钟
学习自动化20分钟 
做自己网站-15分钟
PS-10分钟
游戏45分钟
出去走30分钟
学习视频剪辑10分钟
学习自动化20分钟 
做自己网站-15分钟
PS-10分钟
了解工作10分钟
看书5分钟
学习视频剪辑10分钟
学习自动化20分钟 
做自己网站-15分钟
PS-10分钟
游戏30分钟
看书5分钟
学习视频剪辑10分钟
学习自动化20分钟 
做自己网站-15分钟
PS-10分钟
了解工作10分钟
看书5分钟
游戏1小时
Plank 1min
Plank 1min
Push-up 20
Push-up10
Plank 30sec
Plank 30sec



D11-游戏45分钟
D12-了解工作10分钟
D13-Push-up 20
D14-做自己网站-15分钟
D15-看书5分钟
D16-PS-10分钟
D21-做自己网站-15分钟
D22-学习自动化20分钟 
D23-PS-10分钟
D24-看书5分钟
D25-Plank 1min
D26-学习视频剪辑10分钟
D31-Plank 30sec
D32-PS-10分钟
D33-PS-10分钟
D34-休息40分钟
D35-学习自动化20分钟 
D36-游戏1小时
D41-了解工作20分钟
D42-学习视频剪辑10分钟
D43-游戏30分钟
D44-学习视频剪辑10分钟
D45-做自己网站-15分钟
D46-了解工作30分钟
D51-做自己网站-15分钟
D52-学习自动化20分钟 
D53-学习自动化20分钟 
D54-做自己网站-15分钟
D55-学习自动化20分钟 
D56-看书5分钟
D61-Plank 1min
D62-学习视频剪辑10分钟
D63-PS-10分钟
D64-Push-up10
D65-Plank 30sec
D66-出去走30分钟





















'''