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
        #logs bot username and id both to console and log file
        @self.bot.event
        async def on_ready():
            self.logger.info(f"User: {self.bot.user} (ID: {self.bot.user.id})")
        #runs on_message functionality of bot to read messages sent to it
        self.bot.event(self.message_reader.on_message)

    def login(self):
            self.bot.run(settings.TOKEN)

if __name__ == "__main__":
    main_instance = Main()
    main_instance.login()