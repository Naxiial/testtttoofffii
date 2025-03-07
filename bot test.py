import wmi
import time
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
username = "moiss"

intents = discord.Intents.default()
intents.messages = True
intents.members = True
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    user = await bot.fetch_user(1161621607941423198)
    await user.send(f"test")

    user.send(f"test") 
    

keep_alive()
bot.run(token)