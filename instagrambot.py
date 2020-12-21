import json
import requests
from instabot import Bot
from PIL import Image, ImageDraw, ImageFont
import math
import os
from datetime import datetime

def get_quote():
  # Grab a quote from the API
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  # Parse Json format
  quote = json_data[0]['q'] + "\n ~" + json_data[0]['a']
  print("Quote: " + '\n' + quote)
  # Extract the quote
  quote1 = str(json_data[0]['q'])
  # Count the amount of spaces that are in the quote to get an estimate length of the quote. 
  spacecounter = 0
  for space in quote1:
    if (space.isspace()):
      spacecounter += 1
  print("Spacecounter: " + str(spacecounter))
  # Set the amount of words we want per line
  span = 8
  # Divide the amount of words in the quote by the desired number of words per line to get the amount of lines required
  parts = math.ceil(spacecounter/span)
  print('Parts: ' + str(parts))

  # Split the quote based on spaces
  quote1 = quote1.split(' ')
  
  quoteresult = [" ".join(quote1[i:i+span]) for i in range(0, len(quote1), span)]

  print("Quoteresult: " + str(quoteresult))
  

  # Draw the text on the background
  # open the image
  with Image.open('E:\\Desktop\\pycodes - kopie\\instagrambot\\background.jpg') as img:
    # get the background size
      width, height = img.size
      print('Width: ' + str(width) + " Height: " + str(height))

      # msg = ''
      # for x in range(parts+1):
      #   msg += msg + (quoteresult[x] + '\n')
      # print(msg)
      try:
              msg = str(quoteresult[0] + '\n' + quoteresult[1] + '\n' + '~' + json_data[0]['a'] + '~' )
      except: 
        print('Text too long, trying again...')
        get_quote()
      # set the draw function on the image
      draw = ImageDraw.Draw(img)
      w = draw.textsize(json_data[0]['q'])
      # Get the width of the quote
      w = w[0]
      # Fixed variable
      h = 26
      print(w)
      print(h)
      # Set the font variable
      font = ImageFont.truetype(r'C:\\Users\\System-Pc\\Desktop\\Gabriola.ttf', 40)
      # Draw the quote in the middle of the background
      draw.text(((width-w)/2,(height-h)/2), text = msg, align= "center", font = font, fill="white")
      # Save the edited image

      # Get a timestamp for the file name
      now = str(datetime.now())
      # Remove illegal characters for filename
      now = now.replace(':', '-').replace(' ', '-').replace('.', '-')
      img.save(f"E:\\Desktop\\pycodes - kopie\\instagrambot\\{now}.png", "PNG")
      print('Image saved')
    
def postpicture():
    bot = Bot()
    username = os.environ.get('DB_USER')
    pw = os.environ.get('DB_PASS')
    print(username)
    print(pw)
    bot.login(username= username, password= pw)
    print("Login succesful")
    #bot.upload_photo("E:\\Desktop\\pycodes - kopie\\instagrambot\\test.png")


get_quote()