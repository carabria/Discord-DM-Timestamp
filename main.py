import logging
import discord
import sys

class Main:
    def __init__(self):
        #init client
        intents = discord.Intents.default()
        intents.message_content = True
        self.client = discord.Client(intents=intents)

        #run function to confirm bot is logged in and working properly 
        self.on_startup()

        #run client
        self.login()

    def on_startup(self):
        @self.client.event
        async def on_ready():
            print(f'Logged in as {self.client.user}')

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')

    def login(self):
        #init logger
        handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')

        #read token from token.txt
        try:
            with open('token.txt', 'r') as file:
                token = file.read().strip()
                self.client.run(token, log_handler=handler, log_level=logging.DEBUG)
        except FileNotFoundError:
            print("Please create a token.txt file for the program to run!")
            sys.exit()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.login()