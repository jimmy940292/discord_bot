import discord
from discord.ext import commands


def get_token() -> str:

    with open('.token.txt', 'r') as token_file:
        return token_file.read().strip()


intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)


async def on_ready() -> None:
    print(f'目前登入身份 --> {client.user}')


async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    if message.content == 'Hello':
        await message.channel.send('Hello world!')


client.on_ready = on_ready
client.on_message = on_message


def main() -> None:
    
    token = get_token()
    client.run(token)


if __name__ == '__main__':
    main()
