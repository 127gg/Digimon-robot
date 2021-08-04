import glob
import os
import random

from KanekiRobot.events import register
from telegram.ext import run_async
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos
from KanekiRobot import telethn as pbot 


@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
 
  if not quew:
     await event.reply('Provide Some Text To Draw!')
     return
 await event.reply('Creating your logo...wait!')
 try:
    pics = []
        async for i in event.client.filter_messages(
            "@Kanekilogo", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)  
    id = random.choice(pics)
    bg = await id_.download_media()  
    text = event.pattern_match.group(1)
    img = Image.open(bg)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    fpath = glob.glob("KanekiRobot/riz-ex/fonts/*")
    font = random.choice(fpath)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "LogoByKaneki.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="`Made by` @kanekiexbot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @kanekisupport, {e}')



   
@register(pattern="^/wlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
 
  if not quew:
     await event.reply('Provide Some Text To Draw!')
     return
 await event.reply('Creating your logo...wait!')
 try:
    pics = []
        async for i in event.client.filter_messages(
            "@Kanekilogo", filter=InputMessagesFilterPhotos
        ):
            pics.append(i) 
    id = random.choice(pics)
    bg = await id_.download_media()
    text = event.pattern_match.group(1)
    img = Image.open(bg)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    fpath = glob.glob("KanekiRobot/riz-ex/fonts/*")
    font = random.choice(fpath)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "LogoByKaneki.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="`Made by` @kanekiexbot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @kanekisupport, {e}')

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍  /logo text :  Create your logo with your name
 ❍  /wlogo text :  Create your logo with your name
 """
__mod_name__ = "ʟᴏɢᴏ"
