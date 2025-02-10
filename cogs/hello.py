import discord
from discord.ext import commands

class hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.str = ['hello', 'Hello','hi','Hi']
        
    # Read message
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if(message.author == self.bot.user):
            return
        else:
            if message.content in self.str:
                await message.channel.send("Hello OuO")


# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(hello(bot))       