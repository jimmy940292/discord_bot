import discord
from discord.ext import commands
from discord import app_commands

class Echo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    
    # Read message, return origin words
    @app_commands.command(name='echo', description='echo your words')
    @app_commands.describe(words = "??")
    async def Echo(self, interaction: discord.Interaction, words: str) -> None:
        await interaction.response.send_message(content=words+" 0.0")
        
    
# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(Echo(bot))       