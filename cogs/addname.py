import discord
from discord.ext import commands
from discord import app_commands

class addName(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        
    # Add name into dictionary
    @app_commands.command(name='addname', description='add user name for Riot ID')
    async def addname(self, interaction: discord.Interaction) -> None :
        # await interaction.response.send_message("OuO", file=discord.File(self.picPath))
        None
        
    


# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(addName(bot))       