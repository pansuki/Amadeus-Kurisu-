import discord
from discord.ext import commands
import asyncio
import json
import requests as rq
import os
from discord.utils import get,find
import apiai
import random
import msg_track
import time
import systems as sys
import events


bot_token = Enter your bot token here' #to host code on Github, change to bot_token=os.environ['BOT_TOKEN'] then add a config var called BOT_TOKEN and put your bot token as the value
loaded={'systems':False,'msg_track':False}

bot = commands.Bot(command_prefix='s.')  # SETUP BOT COMMAND PREFIX
bot.remove_command('help')

extensions=['events','msg_track','fun','tools']
