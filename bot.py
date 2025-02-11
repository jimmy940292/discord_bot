import os
import asyncio
import discord
from discord.ext import commands


# Get token from file
def get_token() -> str:
    with open('.token.txt', 'r') as token_file:
        return token_file.read()
    
'''
Change help command
ref: https://stackoverflow.com/questions/64092921/how-do-i-put-discord-py-help-command-in-an-embed
'''

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
                e.description += page
        await destination.send(embed=e)


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents= intents)
bot.help_command = MyHelpCommand() # change help command

# Ready 
@bot.event
async def on_ready() -> None:
    slash = await bot.tree.sync()
    print(f'User -> {bot.user}')
    print(f'Load {len(slash)} commands')
    
# Load command
@bot.command()
async def load(ctx: commands.Context, extension: str) -> None:
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension} done')
    
# Unload command
@bot.command()
async def unload(ctx: commands.Context, extension: str) -> None:
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension} done')
    
# Reload command
@bot.command()
async def reload(ctx: commands.Context, extension: str) -> None:
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reload {extension} done')
    
# Load all commands when starts
async def load_extensions()-> None:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            # ex: hello.py  
            await bot.load_extension(f'cogs.{filename[:-3]}')   
            

# Main function
async def main() -> None:
    token = get_token()
    async with bot:
        await load_extensions() 
        await bot.start(token)


if __name__ == '__main__':
    asyncio.run(main())