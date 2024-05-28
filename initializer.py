import discord
from DLogger import DLogger
from actions.messages import Messages

class Initializer():
    def __init__(self):
        self.logger = DLogger("bot")

    def initialize_bot(self):
        #initialize bot
        intents = discord.Intents.default()
        intents.message_content = True
        bot = discord.Client(intents=intents)

        #initialize event listener
        message_reader = Messages(bot)

        @bot.event
        async def on_ready():
            #logs bot username and id both to console and log file upon login
            self.logger.info(f"User: {bot.user} (ID: {bot.user.id})")

            #enables on_message functionality of bot to read messages sent to it
            bot.event(message_reader.on_message)

        return bot