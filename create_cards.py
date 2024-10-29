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
margin = 0.10
marginal_width = width - width * margin * 2
border_width = 60
border_color = black #(50,50,50)
border_font_size = round(border_width * 0.8)

def main (filename):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  with open(filename, 'r') as f:
    for line in f:
      create_card(line.rstrip())
  create_blank_cards(10)

def create_card (word):
  font = ImageFont.truetype(font_file, max_font_size)
  text = add_line_break(font, word)
  fit_font = fit_to_card (font, text)
  img = Image.new('RGB', (width, height), color = border_color)
  draw = ImageDraw.Draw(img)
  draw.rectangle(
    [(border_width,border_width),(width-border_width,height-border_width)],
    fill=white)

  draw_border_text(img, font_file, word)

  draw.multiline_text(
    (width / 2, height / 2),
    "\n".join(text),
    font = fit_font,
    fill = border_color,
    anchor = "mm",
    align = "center")
  rot_img = img.rotate(270, fillcolor = white, expand=True)
  rot_img.save(output_dir + "/" + word + ".png")

def draw_border_text(img, font_file, word):
  border_font = ImageFont.truetype(font_file, border_font_size)
  text_img = Image.new('RGB', (width, border_width), color = border_color)
  draw = ImageDraw.Draw(text_img)
  draw.text(
    (border_width, border_width/2),
    word,
    font = border_font,
    fill = white,
    anchor = "lm")
  rot_text_img = text_img.rotate(180)
  img.paste(text_img, (0, height-border_width))
  img.paste(rot_text_img, (0, 0))

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

def create_blank_cards (n):
  img = Image.new('RGB', (width, height), color = white)
  rot_img = img.rotate(270, fillcolor = white, expand=True)
  for i in range(0,n):
    rot_img.save(output_dir + "/blank_" + str(i) + ".png")

if __name__ == "__main__":
  main(sys.argv[1])
