import discord

class Messages:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        #ignore any messages sent by the bot
        if message.author == self.client.user:
            return
        
        #simple hello world test
        if message.content.startswith('$hello'):
            await message.channel.send('world!')