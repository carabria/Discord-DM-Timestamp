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
            await message.channel.send('world!')

        if message.content.startswith("!time") | message.content.startswith("!t"):
            try:
                #get current time as a unix timestamp
                if message.content.endswith("-h") | message.content.endswith("-help"):
                    await message.channel.send(
                        '-c (current): returns the current time!\n-fn (from now): returns x hours/days/minutes/etc from now!\n-a (ago): returns x hours/days/minutes/etc ago!')
                
                elif message.content.endswith("-c") | message.content.endswith("-current"):
                    await message.channel.send(f'The current time is <t:{timers.Actions.current_time()}>!')
                
                elif message.content.endswith("-fn") | message.content.endswith("-from now"):
                    await message.channel.send(f'That would be <t:{timers.Actions.time_from_now(message.content)}>')

                elif message.content.endswith("-a") | message.content.endswith ("-ago"):
                    await message.channel.send(f'That would be <t:{timers.Actions.time_ago(message.content)}>!')
            
                else:
                    await message.channel.send('You don\'t seem to have inputted the command in correctly... Use -h for help!')
            
            except custom_exceptions.NoTimeValueError as e:
                await message.channel.send(f'{e}')
                
            except custom_exceptions.NoTimeStringError as e:
                await message.channel.send(f'{e}')

