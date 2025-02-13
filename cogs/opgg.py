import discord
import json
from json.decoder import JSONDecodeError
import os.path
from discord.ext import commands
from discord import app_commands
from libs.wab_scapping import getDataFromOpgg

class opgg(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.filename = 'files/id_mapping.json'
        self.dic = {}
        self.readIdMapping()
        
    # Read id mapping from file
    def readIdMapping(self) -> None:

        with open(self.filename, 'r') as f:
            try:
                data = json.load(f)
                for key, value in data.items():
                    self.dic[key] = value
            except JSONDecodeError:
                pass
                
    # Return dict
    def getIdMapping(self) -> dict:
        return self.dic
    
    # Write dict to file
    def writeIdMapping(self) -> None:
        with open(self.filename, 'w') as f:
            if(len(self.dic)  > 0):
                f.write(json.dumps(self.dic, ensure_ascii=False))
        
        
 
        
    # Search riot id with discord name
    @app_commands.command(name='opgg', description='add user name for Riot ID')
    @app_commands.describe(name = "Discord name")
    async def opgg(self, interaction: discord.Interaction, name: str) -> None :
        # Get data
        self.readIdMapping()
        
        if(name in self.dic): 
            riotId = self.dic[name]
            
            await interaction.response.defer()
            winLose = getDataFromOpgg(riotId)
            if(winLose == ''):
                await interaction.followup.send(f"Riot ID error!")
            else:
                await interaction.followup.send(f"{name} : {riotId}\n{winLose}")
            
        else:
            return 
        

# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(opgg(bot))       