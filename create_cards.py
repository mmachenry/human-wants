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
margin = 0.05
marginal_width = width - width * margin * 2

def main (filename):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  with open(filename, 'r') as f:
    for line in f:
      create_card(line.rstrip())

def create_card (word):
  font = ImageFont.truetype(font_file, max_font_size)
  text = add_line_break(font, word)
  fit_font = fit_to_card (font, text)
  img = Image.new('RGB', (width, height), color = white)
  draw = ImageDraw.Draw(img)
  draw.multiline_text(
    (width / 2, height / 2),
    "\n".join(text),
    font = fit_font,
    fill = black,
    anchor = "mm",
    align = "center")
  #rot_img = img.rotate(270, fillcolor = white)
  img.save(output_dir + "/" + word + ".png")

def add_line_break(font, word):
  if font.getsize(word)[0] < marginal_width or ' ' not in word:
    return [word]
  else:
    return split_at_middle_space(word)

def split_at_middle_space(word):
  spaces = [pos for pos, char in enumerate(word) if char == ' ']
  spaces.sort(key=lambda p: abs(len(word)/2 - p))
  middle = spaces[0]
  return [word[0:middle], word[middle+1:]]

def fit_to_card (font, lines):
  size = max_font_size
  new_font = font
  while max([new_font.getsize(txt)[0] for txt in lines]) > marginal_width:
    size -= 1
    new_font = ImageFont.truetype(font_file, size)
  return new_font

if __name__ == "__main__":
  main(sys.argv[1])
