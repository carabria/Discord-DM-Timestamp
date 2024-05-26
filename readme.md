The purpose of this discord bot is to respond to a message containing a timestamp with the UNIX timestamp equivalent. Functionality for displaying current time and time from now or ago determined by years/months/days/hours etc. Functionality for inputting a specific date/time and getting it back as a unix timestamp is planned.

Pipenv is required to install dependencies.

run 
```pip install pipenv```
then run 
```pipenv install```

To activate this project's virtualenv, run 
```pipenv shell```

Alternatively, run a command inside the virtualenv with
```pipenv run```

You will need to input your bot's token in the root folder. create a .bottoken.env file in the project's root folder in the format of
```TOKEN=YOUR_BOT_TOKEN_HERE```

If you don't have a bot, check https://discordpy.readthedocs.io/en/stable/discord.html for detailed instructions.

Finally, cd to the project's root folder and run
```python main.py```