
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
#import random

bot_token = Enter your bot token here' #to host code on Github, change to bot_token=os.environ['BOT_TOKEN'] then add a config var called BOT_TOKEN and put your bot token as the value
loaded={'systems':False,'msg_track':False}

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print ("testing")
    print ("I am a tree" + bot.user.name)
    print (bot.user.id)

@bot.command(pass_context=True)    
async def tree(ctx):
    await bot.say("I am a tree")

async def info(ctx, user: discord.Member):
    if discord.Member = N2 Dopey#2749
    #if *insert person* give statement else put unknown person or not put in yet :]   

bot.run(bot_token)
