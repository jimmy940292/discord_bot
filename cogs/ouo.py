import discord
from discord.ext import commands
from discord import app_commands

class OuO(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.picPath = '/home/ccw/project/discord_bot/pic/nlnlouo.png'
        
        
    # Return figure 
    @app_commands.command(name='ouo', description='nlnlouo')
    async def OuO(self, interaction: discord.Interaction) -> None :
        await interaction.response.send_message("OuO", file=discord.File(self.picPath))
        
    
# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(OuO(bot))       