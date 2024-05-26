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
            #get current time as a unix timestamp
            if message.content.endswith("current"):
                await message.channel.send(f'The current time is <t:{timers.Actions.current_time()}>, nyaster!')
            
            elif message.content.endswith("from now"):
                 await message.channel.send(f'That would be <t:{timers.Actions.time_from_now(message.content)}>, nyaster!')