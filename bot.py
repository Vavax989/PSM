import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=",", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user} and is ready!")

# Load the PSM cog
if __name__ == "__main__":
    bot.load_extension("psm")  # Load the psm.py cog
    TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace this with your actual bot token
    bot.run(TOKEN)
