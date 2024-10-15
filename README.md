# README 

This project is my first discord bot written in Python. This simple bot has the ability to automatically moderate any discord server it is part of, allowing a more accessible and easier experience with moderation. It can assist with chat moderation, manage users and various other functions.

## Features

- Automated Moderation: Automatically detect words and moderate the inappropriate behaviour.
- Custom Moderation Commands: Allows new easily accessible commands to warn, kick, ban, mute, unmute, add or remove warning words and banned words.
- Automated Warning System: Automated list that warns people when used in chats.
- Automated Ban System: Automated list that bans people when used in chats.
- Custom Prefix: Allows servers to use their own prefix for the bot, this prevents crossover with other bots they might have in the server.
- Purge Messages: Allows servers to purge any amount of messages in a chat.

## Usage / Commands

*Default prefix = !*

- ```!changeprefix <prefix>```: Sets a custom prefix
- ```!help```: Shows the lists of commands
- ```!ban @user <reason>```: To ban a user
- ```!unban @user <reason>```: To unban a user
- ```!kick @user <reason>```: To kick a user
- ```!mute @user <reason>```: To mute a user
- ```!ummute @user <reason>```: To unmute a user
- ```!purge <amount>```: To purge a certain amount of messages in the discord chat
- ```!addbanword <word>```: To add ban words into the ban word list
- ```!addwarnword <word>```: To add warn words into the warn word list
- ```!removebanword <word>```: To remove ban words into the ban word list
- ```!removewarnword <word>```: To remove warn words into the warn word list
- ```!deletebanword <word>```: Same command as removebanword
- ```!deletewarnword <word>```: Same command as removewarnword
- ```!filter <word>```: Shows all filtered words

There are much more commands that the bot has, and can be found through the help command list when added to your server!

## Permissions

Recommended to give the bot administrator as I have not tested the bot using specific moderation permissions. 

## Installations

To run this bot, you'll need:

- Python 3.8 or higher.
- A discord account and a Discord server where you have permissions to add bots.
- A discord bot token through creating a bot on the [Discord Developer Portal](https://discord.com/developers/applications)

1. Clone or download this repository to your machine:

```
git clone https://github.com/your-username/discord-moderation-bot.git
cd discord-moderation-bot
```

2. Installed the required Python dependencies:

```pip install -r requirements.txt```

3. Edit the python file to add your own discord token

4. Run the bot

## Future Updates

In the future, one of the more important features / changes I will most likely add is a seperate file that reads the token so the user does not have to edit the main python file itself.
I may also add a logging feature on the bot in the future.
