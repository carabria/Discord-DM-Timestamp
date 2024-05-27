This is an ongoing project of mine, both to learn python and how Discord bots work. 
The purpose of this discord bot is to respond to a message containing a timestamp with the UNIX timestamp equivalent. Functionality for displaying current time and time from now or ago determined by years/months/days/hours etc is implemented. 
Functionality for inputting a specific date/time and getting it back as a unix timestamp is planned.

# INSTALLATION INSTRUCTIONS

## 1. Activate a local bot-env for yourself

On Linux:

```$ cd your-bot-source```

```$ python3 -m venv bot-env```

On Windows:

```$ cd your-bot-source```

```$ py -3 -m venv -bot-env```

## 2. Activate the venv

On Linux:

```$ source bot-env/bin/activate```

On Windows:

```$ bot-env\Scripts\activate.bat```

## 3. Install discord.py

```$ pip install -U discord.py```

## 4. Install pipenv for other dependencies

run 

```pip install pipenv```

then run 

```pipenv install```


## 5.  You will need to input your bot's token in the root folder. create a .bottoken.env file in the project's root folder in the format of
```TOKEN=YOUR_BOT_TOKEN_HERE```

If you don't have a bot, check https://discordpy.readthedocs.io/en/stable/discord.html for detailed instructions on how to create one and get its token.

## 6. Create a ```log``` folder and insert a ```discord.log``` file into it.

## 7. Finally, cd to the project's root folder and run

```python main.py```