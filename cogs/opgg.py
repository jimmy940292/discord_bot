import discord
import json
import os.path
from discord.ext import commands
from discord import app_commands

class opgg(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.filename = 'files/id_mapping.json'
        self.dic = {}
        self.readIdMapping()
        
    # Read id mapping from file
    def readIdMapping(self) -> None:

        with open(self.filename, 'r') as f:
            data = json.load(f)
            for key, value in data.items():
                self.dic[key] = value
                
    # Return dict
    def getIdMapping(self) -> dict:
        return self.dic
    
    # Write dict to file
    def writeIdMapping(self) -> None:
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.dic))
        
    # Search riot id with discord name
    @app_commands.command(name='opgg', description='add user name for Riot ID')
    @app_commands.describe(name = "Discord name")
    async def opgg(self, interaction: discord.Interaction, name: str) -> None :
        # Get data
        self.readIdMapping()
        
        if(name in self.dic): 
            riotId = self.dic[name]
            await interaction.response.send_message(f"{name} : {riotId}")
        else:
            return 
        

# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(opgg(bot))       