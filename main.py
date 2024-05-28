from settings import TOKEN
from initializer import Initializer
import sys


def main():
    initializer = Initializer()
    bot = initializer.initialize_bot()

    #logs in using the token found in the settings file
    try:
        bot.run(TOKEN)
    except TypeError:
            print("Token is NoneType. Make sure your token is included in .bot_token.env!")
            sys.exit()

if __name__ == "__main__":
    #to be run when main.py is used as entry point for the program
    main()