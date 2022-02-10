import sys
import os
import re
from PIL import Image, ImageDraw, ImageFont
 
width = 1125
height = 750
max_font_size = 150
black = (0,0,0)
white = (255,255,255)
font_file = 'easy-print.regular.ttf'
output_dir = "cards"

def main (filename):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  with open(filename, 'r') as f:
    for line in f:
      create_card(line.rstrip())

def create_card (word):
  lines = word.split("|")
  filename = re.sub("[|]", " ", word)
  font = ImageFont.truetype(font_file, max_font_size)
  fit_font = fit_to_card (font, lines)
  img = Image.new('RGB', (width, height), color = white)
  draw = ImageDraw.Draw(img)
  draw.multiline_text(
    (width / 2, height / 2),
    "\n".join(lines),
    font = fit_font,
    fill = black,
    anchor = "mm",
    align = "center")
  #rot_img = img.rotate(270, fillcolor = white)
  img.save(output_dir + "/" + filename + ".png")

def fit_to_card (font, lines):
  marginal_width = width * 0.9
  size = max_font_size
  new_font = font
  while max([new_font.getsize(txt)[0] for txt in lines]) > marginal_width:
    size -= 1
    new_font = ImageFont.truetype(font_file, size)
  return new_font

if __name__ == "__main__":
  main(sys.argv[1])
