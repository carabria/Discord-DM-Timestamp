import discord
import settings
from actions.messages import Messages

class Main:
    def __init__(self):
        #init logger
        self.logger = settings.logging.getLogger("bot")

        #init bot
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = discord.Client(intents=intents)

        #init event listeners
        self.message_reader = Messages(self.bot)
        self.on_startup()


    def on_startup(self):
        #logs bot username and id both to console and log file upon login
        @self.bot.event
        async def on_ready():
            self.logger.info(f"User: {self.bot.user} (ID: {self.bot.user.id})")
        #runs on_message functionality of bot to read messages sent to it
        self.bot.event(self.message_reader.on_message)

    def login(self):
            #logs in using the token found in the settings file
            self.bot.run(settings.TOKEN)

if __name__ == "__main__":
    #to be run when main.py is used as entry point for the program
    main_instance = Main()
    main_instance.login()