import discord
from . import timers

class Messages:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        #ignore any messages sent by the bot
        if message.author == self.bot.user:
            return
        
        #simple hello world test
        if message.content.startswith('!hello'):
            await message.channel.send('nyaster!')
        if message.content.startswith("!time"):
            await message.channel.send(f'The current time is <t:{timers.Actions.current_time()}>, nyaster!')   
        #TODO: add logic to read timestamps. new file will need to be made
        #in order to handle unix conversion logic.