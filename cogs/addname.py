import discord
import json
from json.decoder import JSONDecodeError
from typing import Union
from discord.ext import commands
from discord import app_commands

class addName(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.filename = 'files/id_mapping.json'
        self.dic = {}
        
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
            if(len(self.dic) > 0):
                f.write(json.dumps(self.dic, ensure_ascii=False))
            # f.write(json.dump(self.dic))
        
    # Add name into dictionary
    @app_commands.command(name='addname', description='add user name for Riot ID')
    @app_commands.describe(name = "Discord name", id = "Riot id")
    async def addName(self, interaction: discord.Interaction, name: str, id: str) -> None:

        await interaction.response.send_message(content=f"{name} : {id}")
        
        self.readIdMapping()
        
        if(name not in self.dic or self.dic[name] != id):
            self.dic[name] = id
        
        self.writeIdMapping()

# Load Cog
async def setup(bot: commands.Bot):
    await bot.add_cog(addName(bot))       