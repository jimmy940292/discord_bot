import discord



# Refer to 
# https://hackmd.io/@smallshawn95/python_discord_bot_base


def getToken() ->str:
    
    file = open(".token.txt")
    token = ''
    for lines in file:
        token += lines
        
    return token




def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents= intents)
    token = getToken()
    
    @client.event
    async def on_ready():
        print(f'目前登入身份 --> {client.user}')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content == 'Hello':
            await message.channel.send('Hello world!')
    
    client.run(token)
    

if __name__ == "__main__":
    main()