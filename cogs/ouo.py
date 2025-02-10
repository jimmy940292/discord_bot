import discord
from discord.ext import commands

class OuO(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        
    # Read message
    @commands.command()
    async def OuO(self, ctx: commands.Context):
        await ctx.send('OuO')
    


# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(OuO(bot))       