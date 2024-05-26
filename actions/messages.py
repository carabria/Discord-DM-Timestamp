import discord
import re
import textwrap
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
        
        #help menu displaying all available commands
        elif message.content.startswith('!help') or message.content.startswith('!h'):
            help_message = '''
                !hello: sends a message to verify the bot is running!
                !t (!time): commands related to unix timestamping!
                use -as a prefix at the end of the command for options (e.x. !time -help)
            '''
            await message.channel.send(textwrap.dedent(help_message))

        #commands relating to unix timestamps
        elif message.content.startswith("!time") or message.content.startswith("!t"):
            try:
                #display available parameters in time
                if message.content.endswith("-h") or message.content.endswith("-help"):
                    help_message = '''
                        -c (current): returns the current time!
                        -fn (from now): returns x hours/days/minutes/etc from now!
                        -a (ago): returns x hours/days/minutes/etc ago!
                    '''
                    await message.channel.send(textwrap.dedent(help_message))
                
                #get current time as a unix timestamp
                elif message.content.endswith("-c") or message.content.endswith("-current"):
                    await message.channel.send(f'The current time is <t:{timers.Actions.current_time()}{timers.Actions.formatter(message.content)}>!')
                
                #get a time x [hours/minutes/days/etc] from now
                elif message.content.endswith("-fn") or message.content.endswith("-from now"):
                    await message.channel.send(f'That would be <t:{timers.Actions.time_from_now(message.content)}{timers.Actions.formatter(message.content)}>')

                #get a time x [hours/minutes/days/etc] ago
                elif message.content.endswith("-a") or message.content.endswith ("-ago"):
                    await message.channel.send(f'That would be <t:{timers.Actions.time_ago(message.content)}{timers.Actions.formatter(message.content)}>!')

                #parameter was entered wrong, suggest help to user
                else:
                    await message.channel.send('You don\'t seem to have inputted the command in correctly... Use -h for help!')
            
            #user inputted number wrong
            except custom_exceptions.NoTimeValueError as e:
                await message.channel.send(f'{e}')
            
            #user inputted [hours/minutes/days/etc] wrong
            except custom_exceptions.NoTimeStringError as e:
                await message.channel.send(f'{e}')

        #checks to see if a command begins with ! and has leading characters, indicating a wrong command. prints an error message.
        elif re.match(r'^![^!]+', message.content):
            await message.channel.send('You don\'t seem to have inputted a command in correctly... Use -h for help!')