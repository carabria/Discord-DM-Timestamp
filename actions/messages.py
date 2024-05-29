import discord
import re
import textwrap
from actions import timers
from actions import custom_exceptions
from DLogger import DLogger

class Messages:
    def __init__(self, bot):
        self.bot = bot
        self.logger = DLogger("bot")
        self.timers = timers.Actions

    async def on_message(self, message):
        #ignore any messages sent by the bot
        if message.author == self.bot.user:
            return
        
        #simple hello world test
        if message.content.startswith('!hello'):
            await message.channel.send('world!')
            self.logger.info("Hello command executed successfully.")
        
        #help menu displaying all available commands
        # # # # # # # # # # # # # # # # # # # # # # #

        elif message.content.startswith('!help') or message.content.startswith('!h'):
            help_message = '''
                !hello: sends a message to verify the bot is running!
                !t (!time): commands related to unix timestamping!
                use -as a prefix at the end of the command for options (e.x. !time -help)
            '''
            await message.channel.send(textwrap.dedent(help_message))
            self.logger.info("Help command executed successfully.")

        #commands relating to unix timestamps
        # # # # # # # # # # # # # # # # # # #
        
        elif message.content.startswith("!time") or message.content.startswith("!t"):
            try:
                #display available parameters in time
                if message.content.endswith("-h") or message.content.endswith("-help"):
                    help_message = '''
                        Time formatting options, include these as the 2nd to last part of the command:
                        -t: displays in short time (<t:1543392060:t>)
                        -T: displays in long time (<t:1543392060:T>)
                        -d: displays in short date (<t:1543392060:d>)
                        -D: displays in long date (<t:1543392060:D>)
                        -f: displays in short date/time (<t:1543392060:f>)
                        -F: displays in long date/time (<t:1543392060:F>
                        -R: displays in relative time (<t:1543392060:R>)
                        Leave blank to display as <t:1543392060>

                        Operation parameters, include this as the last part of the command:
                        -c (current): returns the current time!
                        -fn (from now): returns x hours/days/minutes/etc from now!
                        -a (ago): returns x hours/days/minutes/etc ago!
                        -s (specific): returns converted time of a specific unix timestamp

                        Time values, include this before formatting and operation parameters:
                        year[s]
                        month[s]
                        week[s]
                        day[s]
                        hour[s]
                        minute[s]
                        second[s]
                    '''
                    await message.channel.send(textwrap.dedent(help_message))
                    self.logger.info("Time help command executed successfully.")
                
                #get current time as a unix timestamp
                elif message.content.endswith("-c") or message.content.endswith("-current"):
                    timestamp = self.timers.current_time()
                    time_format = self.timers.formatter(message.content)

                    await message.channel.send(f'The current time is <t:{timestamp}{time_format}>!')
                    self.logger.info("Current time command executed successfully.")
                
                #get a time x [hours/minutes/days/etc] from now
                elif message.content.endswith("-fn") or message.content.endswith("-from now"):
                    #pased in with 1 to add in time_calc function
                    timestamp = self.timers.time_calc(message.content, 1)
                    time_format = self.timers.formatter(message.content)

                    await message.channel.send(f'That would be <t:{timestamp}{time_format}>')
                    self.logger.info("Time from now command executed successfully.")

                #get a time x [hours/minutes/days/etc] ago
                elif message.content.endswith("-a") or message.content.endswith ("-ago"):
                    #passed in with -1 to subtract in time_calc function
                    timestamp = self.timers.time_calc(message.content, -1)
                    time_format = self.timers.formatter(message.content)

                    await message.channel.send(f'That would be <t:{timestamp}{time_format}>!')
                    self.logger.info("Time ago command executed successfully.")

                #convert a specific timestamp into unix format
                elif message.content.endswith("-s") or message.content.endswith("-specific"):
                    timestamp = self.timers.time_convert(message.content)
                    time_format = self.timers.formatter(message.content)

                    await message.channel.send(f'That would be <t:{timestamp}{time_format}>!')
                    self.logger.info("Specific time command executed successfully.")

                #parameter was entered wrong, suggest help to user
                else:
                    await message.channel.send('You don\'t seem to have inputted the command in correctly... Use -h for help!')
                    self.logger.error("Time error command displayed, parameter entered wrong?")
            
            #user inputted number wrong
            except custom_exceptions.NoTimeValueError as e:
                await message.channel.send(f'{e}')
                self.logger.error("NoTimeValueError displayed, time number entered wrong?")

            
            #user inputted [hours/minutes/days/etc] wrong
            except custom_exceptions.NoTimeStringError as e:
                await message.channel.send(f'{e}')
                self.logger.error("NoTimeStringError displayed, time string entered wrong?")

        #checks to see if a command begins with ! and has leading characters, indicating a wrong command. prints an error message.
        elif re.match(r'^![^!]+', message.content):
            await message.channel.send('You don\'t seem to have inputted a command in correctly... Use -h for help!')
            self.logger.error("Time command error displayed, command entered wrong?")