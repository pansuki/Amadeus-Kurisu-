
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
#import random

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print ("testing")
    print ("I am a tree" + bot.user.name)
    print (bot_userId)

@bot.command(pass_context=True)    
async def nurupo(ctx):
    await bot.say("Gah")

@bot.command(pass_context=True)
async def drink(ctx):
    await bot.say("Dr. Pepper of couse, it is The intellectual drink, for the chosen ones!")

#@bot.command(pass_context=True)
#async def spam(ctx, phrase, num):
    
     

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    if user.name == 'Amadeus(Kurisu)':
        await bot.say("Lab Member 004 Christina. online name: KuriGohan and Kamehameha")
    elif user.name == '<@189542988647497728>':
        await bot.say("listen buddy")
    elif user.name == 'loik':    
        await bot.say("listen buddy")
    else:
        await bot.say("unknown person or not put in yet <@189542988647497728>")    
    #if *insert person* give statement else put unknown person or not put in yet :]    

bot.run(process.env.BOT_TOKEN)
