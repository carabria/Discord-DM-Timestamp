import discord
from settings import TOKEN
from DLogger import DLogger
import sys
from actions.messages import Messages

def main():
    #init logger
    logger = DLogger.log("bot")
    #init bot
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)
    #init event listener
    message_reader = Messages(bot)

    @bot.event
    async def on_ready():
        #logs bot username and id both to console and log file upon login
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        #enables on_message functionality of bot to read messages sent to it
        bot.event(message_reader.on_message)
    
    #logs in using the token found in the settings file
    try:
        bot.run(TOKEN)
    except TypeError:
            print("Token is NoneType. Are you sure you created a .bot_token.env file in your root folder?")
            sys.exit()

if __name__ == "__main__":
    #to be run when main.py is used as entry point for the program
    main()