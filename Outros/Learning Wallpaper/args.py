import argparse

# Add word
# Set Wallpaper
# Delete a word
# Set size
# Set font
# Set font size
# Set background color
# Set text color


parser = argparse.ArgumentParser()

# --add
parser.add_argument('-a', '--add',
                    help='adds word to json/wallpaper',
                    default=[],
                    action='append')
# --set
parser.add_argument('-s', '--set',
                    help='sets the wallpaper',
                    action='store_true')
# --delete
parser.add_argument('-d', '--delete',
                    help='deletes the specified word/s',
                    default=[],
                    action='append')
# --imagesize
parser.add_argument('-i', '--imagesize',
                    help='defines the size of the output image (must be formated as the default: 1920x1080)',
                    default='1920x1080')
# --font
parser.add_argument('-f', '--font',
                    help='defines the font to be used in the wallpaper',
                    default='HachiMaruPop-Regular.ttf')
# --fontsize
parser.add_argument('--fontsize',
                    help='defines the font size in points (default: 30)',
                    default='30')
# --color
parser.add_argument('-c', '--color',
                    help='set background color in hexadecimal',
                    default='#14001E')
# --textcolor
parser.add_argument('-t', '--textcolor',
                    help='set text color in hexadecimal',
                    default='#F0C814')

args = parser.parse_args()