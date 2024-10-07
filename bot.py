# imports
import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# load env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

# start bot
@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print("Bot is ready!")
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


# cat snowball
@client.tree.command(name='cat', description="cat SnowBall")
@app_commands.describe(
    name="@ someone"
)
async def cat(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(
        f"""
        好无聊逗逗{name}吧
        嘬嘬嘬𐃆 ˒˒ ͏                               
͏
͏
͏
͏                              ╱|、
                            (˚ˎ 。7 
                            |、˜ 〵 
                            じしˍ,)ノ
        """
    )

client.run(DISCORD_TOKEN)