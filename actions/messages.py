import discord
from actions import timers
from actions import custom_exceptions

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
            try:
                #get current time as a unix timestamp
                if message.content.endswith("help"):
                    await message.channel.send(
                        'current: returns the current time!\nfrom now: returns x hours/days/minutes/etc from now!\nago: returns x hours/days/minutes/etc ago!')
                
                elif message.content.endswith("current"):
                    await message.channel.send(f'The current time is <t:{timers.Actions.current_time()}>, nyaster!')
                
                elif message.content.endswith("from now"):
                    await message.channel.send(f'That would be <t:{timers.Actions.time_from_now(message.content)}>, nyaster!')

                elif message.content.endswith("ago"):
                    await message.channel.send(f'That would be <t:{timers.Actions.time_ago(message.content)}>, nyaster!')     
            
            except custom_exceptions.NoTimeValueError as e:
                await message.channel.send(f'{e}')
            except custom_exceptions.NoTimeStringError as e:
                await message.channel.send(f'{e}')
            else:
                await message.channel.send('You don\'t seem to have inputted the command in correctly, nyaster... Why nyot try using help?')
