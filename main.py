'''
from PIL import Image, ImageDraw, ImageFont
import discord

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

client = discord.Client();
client = commands.Bot(command_prefix="!");
@client.event
async def on_ready():
    print('"We Have logged in as {0.user}'.format(client));

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0];
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!');
    if message.content.startswith("!slap") and username != "AngelEXDI":
        image = Image.open("Batman-Slapping-Robin-Meme-Explained.jpg");
        font_type = ImageFont.truetype("arial.ttf", 64);
        draw = ImageDraw.Draw(image);
        draw.text(xy=(800, 50), text=username, fill=(255, 69, 0), font=font_type);
        draw.text(xy=(300, 275), text=message.content.split(" ")[1], fill=(255, 69, 0), font=font_type);
        image.save("Picture.png");
        image.show();
@client.command(pass_context=True)
async def test(ctx):
    await ctx.send(file=discord.File("Picture.png"));


client.run("");

'''
'''
image.show();
'''
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
from PIL import Image, ImageDraw, ImageFont
client = discord.Client();
client_message = " ";
bot = commands.Bot("!");
# Things to run when the bot connects to Discord
@bot.event
async def on_ready():
    print(f'"We Have logged in as: {bot.user.name}');

# Test command
@bot.command(name = "slap")
async def Test(ctx, name1:str, name2:str):
    ###Messing with my BestFriend Angel By the Bot Unaccessable to anyone named Angel in the server
    if name1 == "Angel" or name1 == "angel":
        await ctx.send("Not Today Buddy");
        image = Image.open("Batman-Slapping-Robin-Meme-Explained.jpg");
        font_type = ImageFont.truetype("arial.ttf", 64);
        draw = ImageDraw.Draw(image);
        draw.text(xy=(800, 50), text=name2, fill=(255, 69, 0), font=font_type);
        draw.text(xy=(300, 275), text=name1, fill=(255, 69, 0), font=font_type);
        image.save("Picture.png");
        await ctx.send(file=discord.File('Picture.png'))

    elif name1.casefold() == "------" or name2.casefold() == "-----":
        await ctx.send(file=discord.File('Capture.jpg'))
        await ctx.send(file = discord.File('SVL2VLB2SYSPT2HUE6RWZSYOZE.jpg'));
    else:
        image = Image.open("Batman-Slapping-Robin-Meme-Explained.jpg");
        font_type = ImageFont.truetype("arial.ttf", 64);
        draw = ImageDraw.Draw(image);
        draw.text(xy=(800, 50), text=name1, fill=(255, 69, 0), font=font_type);
        draw.text(xy=(300, 275), text=name2, fill=(255, 69, 0), font=font_type);
        image.save("Picture.png")
        await ctx.send(file=discord.File('Picture.png'))

bot.run("User's Bot Token")