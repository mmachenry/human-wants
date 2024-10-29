import sys
import os
import re
from PIL import Image, ImageDraw, ImageFont
 
width = 3450
height = 2700
black = (0,0,0)
white = (255,255,255)
font_file = 'easy-print.regular.ttf'
output_dir = "box"
margin = 0.10
marginal_width = width - width * margin * 2

def main ():
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  create_box()

def create_box ():
  large_font = ImageFont.truetype(font_file, 200)
  small_font = ImageFont.truetype(font_file, 50)
  tiny_font = ImageFont.truetype(font_file, 30)
  logo = Image.open("hematite.jpg", "r").resize((400,400))
  img = Image.new('RGB', (width, height), color = white)
  draw = ImageDraw.Draw(img)
  img.paste(logo, (round(width/2-logo.width/2),round(height*0.55)))
  draw.multiline_text(
    (width / 2, height * 0.45),
    "Human\nWants and Needs",
    font = large_font,
    fill = black,
    anchor = "mm",
    align = "center")
  draw.multiline_text(
    (width / 2, height * 0.55),
    "A game, tool, and icebreaker\nfor exploring your priorities, values, and desires",
    font = small_font,
    fill = black,
    anchor = "mm",
    align = "center")
  draw.text(
    (width / 2, height * 0.67),
    "Hematite Games",
    font = tiny_font,
    fill = black,
    anchor = "mm",
    align = "center")
  img.save(output_dir + "/cover.png")


if __name__ == "__main__":
  main()
