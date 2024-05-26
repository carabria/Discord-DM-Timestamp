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

        #run function to confirm bot is logged in and working properly 
        self.on_startup()

        #run client
        self.login()

        #begin reading mesages
        self.message_reader = Messages(self.bot)

    def on_startup(self):
        @self.bot.event
        async def on_ready():
            self.logger.info(f"User: {self.bot.user} (ID: {self.bot.user.id})")

    def login(self):
            self.bot.run(settings.TOKEN)

if __name__ == "__main__":
    main_instance = Main()
    main_instance.login()