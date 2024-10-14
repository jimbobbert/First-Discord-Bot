import discord
import json
import asyncio
import os.path
import datetime
from discord.ext import commands

botID = 114

# --- Json/Variables --- #

def filecreation():
    if not os.path.exists("bannedwords.json"):
        with open("bannedwords.json", 'w+') as NewFile:
            NewFile.write('["foo", "doo"]')
        print("New bannedwords json file created!")
    if not os.path.exists("prefix.json"):
        with open("prefix.json", 'w+') as NewFile:
            NewFile.write('["!"]')
        print("New prefix json file created!")
    if not os.path.exists("warningwords.json"):
        with open("warningwords.json", 'w+') as NewFile:
            NewFile.write('["too, loo"]')
    else:
        return

filecreation()


with open("bannedwords.json", "r") as bannedwordL:
    bannedword = json.load(bannedwordL)
with open("warningwords.json", "r") as warnwordL:
    warnword = json.load(warnwordL)
with open("prefix.json", "r") as prefixL:
    prefix = json.load(prefixL)
# --- StartUP --- #

intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents=intents)

async def get_prefix(bot, message):
    with open("prefix.json", "r") as prefixL:
        newPrefix = json.load(prefixL)
    return newPrefix

bot = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive=True, pass_context=True)
bot.remove_command("help")
botChannel = "bot" + str(botID)

prefixW = prefix[0].replace("'", "")
# --- Main Code --- #

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def test(ctx):
    await ctx.send('This is a test command.')

# - Prefixes - #

@bot.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, word=None):
    import json

    changeError = discord.Embed(title="Missing Arguement", color=0xfea9ef)
    changeError.add_field(name="How to use?", value=f"{prefixW}changeprefix [any character], for example: {prefixW}changeprefix !", inline=False)

    changeSuc = discord.Embed(title="Success!", color=0xfea9ef)
    changeSuc.add_field(name="Prefix successfully changed!", value="", inline=False)

    if word == None:
        await ctx.send(embed=changeError, delete_after=5.0)
        return
    else:
        with open("prefix.json", "r") as prefixL:
            prefix = json.load(prefixL)
        prefix.clear()
        prefix.append(word)
        with open("prefix.json", "w") as prefixL:
            json.dump(prefix ,prefixL)
        await ctx.send(embed=changeSuc, delete_after=5.0)

@bot.command()
async def prefix(ctx):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")
    await ctx.send("The prefix for this bot is: " + prefixW)

# --- User Actions --- #

# - Help - #

@bot.command()
async def help (ctx):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")
    # - about embed - #

    embedabout = discord.Embed(title="About", color=0xfea9ef)
    embedabout.add_field(name="What is this bot about?",value="This bot is a moderation bot project that is capable of moderating users in a discord server, for example the bot can ban, unban, and kick users from a server through a command that only people with administrator permissions can run!",inline=False)

    # - commands embed - #

    embedcom = discord.Embed(title="Command", color=0xfea9ef)
    embedcom.add_field(name="The list of commands are: ", value="", inline=False)
    embedcom.add_field(name=f"{prefixW}ban", value=f"Usage: {prefixW}ban [@user or ID] [Reason], for example: {prefixW}ban @jim he stinks!", inline=False)
    embedcom.add_field(name=f"{prefixW}unban", value=f"Usage: {prefixW}unban [@user or ID], for example: {prefixW}unban @jim", inline=False)
    embedcom.add_field(name=f"{prefixW}kick", value=f"Usage: {prefixW}kick [@user or ID] [Reason], for example: {prefixW}kick @jim he stinks!", inline=False)
    embedcom.add_field(name=f"{prefixW}mute", value=f"Usage: {prefixW}mute [@user]/[user ID] [s]/[m]/[h], for example: {prefixW}mute @jim 10m", inline=False)
    embedcom.add_field(name=f"{prefixW}purge", value=f"Usage: {prefixW}purge [amount of messages], for example: {prefixW}purge 15", inline=False)
    embedcom.add_field(name=f"{prefixW}addbanword", value=f"Usage: {prefixW}addbanword [word], for example: {prefixW}addbanword stinky", inline=False)
    embedcom.add_field(name=f"{prefixW}addwarnword", value=f"Usage: {prefixW}addwarnword [word], for example: {prefixW}addwarnword stinky", inline=False)
    embedcom.add_field(name=f"{prefixW}removebanword", value=f"Usage: {prefixW}removebanword [word], for example: {prefixW}removebanword stinky", inline=False)
    embedcom.add_field(name=f"{prefixW}removewarnword", value=f"Usage: {prefixW}removewarnword [word], for example: {prefixW}removewarnword stinky", inline=False)
    embedcom.add_field(name=f"{prefixW}deletebanword", value=f"Usage: {prefixW}deletebanword [word], for example: {prefixW}deletebanword stinky", inline=False)
    embedcom.add_field(name=f"{prefixW}deletewarnword", value=f"Usage: {prefixW}deletewarnword [word], for example: {prefixW}deletewarnword stinky", inline=False)
    embedcom.add_field(name=f"{prefixW}filter", value=f"Usage: {prefixW}filter", inline=False)

    # - misc embed - #

    embedmisc = discord.Embed(title="Other", color=0xfea9ef)
    embedmisc.add_field(name="As this is a project, there might be bugs: please refer to me at W22021886@Northumbria.ac.uk to report bugs", value="", inline=False)

    # - regular help embed - #
    helpembed = discord.Embed(title="Help",description=f"A list of commands and how to use them, type {prefixW}help [section] below to get to different help sections. For example: {prefixW}help about",color=0xfea9ef)
    helpembed.add_field(name="About", value="What is this bot?", inline=False)
    helpembed.add_field(name="Commands", value="This is will show you a list of commands", inline=False)
    helpembed.add_field(name="Other", value="Miscellaneous information", inline=False)

    if "about" in ctx.message.content.lower():
        await ctx.send(embed=embedabout, delete_after=30.0)
        return
    if "commands" in ctx.message.content.lower():
        await ctx.send(embed=embedcom, delete_after=30.0)
        return
    if "other" in ctx.message.content.lower():
        await ctx.send(embed=embedmisc, delete_after=30.0)
        return
    else:
        await ctx.send(embed=helpembed, delete_after=30.0)
        return
# - ban - #

@bot.command()
@commands.has_permissions(administrator=True)
# - * means that everything after member count/tagging the member is part of the reason
async def ban(ctx, member:discord.Member=None, *, reason=None):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")

    #- discord.Member here is a class that from the discord.py library that allows the bot to interact with the api, like interactions in chat and profiles.
    #--checks author of message and the recipient--#
    if member.guild_permissions.administrator:
        await ctx.send("You can't ban an admin!", delete_after=5.0)
        return
    if ctx.message.author == member:  # checks if user is the author of the message
        await ctx.send("You can't ban yourself!", delete_after=5.0)
        return
    if discord.Member.bot == member:
        await ctx.send("You can't ban a bot!", delete_after=5.0)
        return
    if member == None:
        embed = discord.Embed(title="Missing Arguement", description="Ban a user", color=0xfea9ef)
        embed.add_field(name="How to use?", value=f"{prefixW}ban [@user] [reason], for example: {prefixW}ban @jim he stinks!", inline=False)
        await ctx.send(embed=embed, delete_after=5.0)
        return
    elif reason == None:
        embed = discord.Embed(title="Missing Arguement", description="Ban a user", color=0xfea9ef)
        embed.add_field(name="How to use?", value=f"{prefixW}ban [@user]/[user ID] [reason], for example: {prefixW}ban @jim he stinks!", inline=False)
        await ctx.send(embed=embed, delete_after=5.0)
        return
    else:
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        embed = discord.Embed(title="Banned", description=f"User {member.mention} has been banned for {reason} | ID: {member.id}", color=0xfea9e6)
        await member.send(message)
        await ctx.send(embed=embed, delete_after=5.0)
        await member.ban(reason=reason)


# - kick - #

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member=None, *, reason=None):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")


    #--checks author of message and the recipient--#
    if member.guild_permissions.administrator:
        await ctx.send("You can't kick an admin!", delete_after=5.0)
        return
    if ctx.message.author == member:  # checks if user is the author of the message
        await ctx.send("You can't kick yourself!", delete_after=5.0)
        return
    if discord.Member.bot == member:
        await ctx.send("You can't kick a bot!", delete_after=5.0)
        return
    if member == None:
        embed = discord.Embed(title="Missing Arguement", description="Kick a user", color=0xfea9ef)
        embed.add_field(name="How to use?", value=f"{prefixW}kick [@user] [reason], for example: {prefixW}kick @jim he stinks!", inline=False)
        await ctx.send(embed=embed, delete_after=5.0)
        return
    elif reason == None:
        embed = discord.Embed(title="Missing Arguement", description="Kick a user", color=0xfea9ef)
        embed.add_field(name="How to use?", value=f"{prefixW}kick [@user]/[user ID] [reason], for example: {prefixW}kick @jim he stinks!", inline=False)
        await ctx.send(embed=embed, delete_after=5.0)
        return
    else:
        message = f"You have been kicked from {ctx.guild.name} for {reason}"
        embed = discord.Embed(title="Kicked", description=f"User {member.mention} has been Kicked for {reason} | ID: {member.id}", color=0xfea9e6)
        await member.send(message)
        await ctx.send(embed=embed, delete_after=5.0)
        await member.kick(reason=reason)

# - purge - #

@bot.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount:int=None):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")

    embedpurge = discord.Embed(title="Missing Arguement", color=0xfea9ef)
    embedpurge.add_field(name="how to use?", value=f"{prefixW}purge [amount of messages], for example: {prefixW}purge 15", inline=False)

    if amount is None:
        await ctx.send(embed=embedpurge, delete_after=5.0)
    elif amount == 1:
        embedpurge = discord.Embed(title="Purge", color=0xfea9ef)
        embedpurge.add_field(name=f"Sucessfully purged {amount} message!", value="", inline=False)
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(embed=embedpurge, delete_after=5.0)
        return
    elif amount > 1:
        embedpurge = discord.Embed(title="Purge", color=0xfea9ef)
        embedpurge.add_field(name=f"Sucessfully purged {amount} messages!", value="", inline=False)
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(embed=embedpurge, delete_after=5.0)
        return
    else:
        await ctx.send(embed=embedpurge, delete_after=5.0)


# - mute - #

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member:discord.Member=None):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")

    unmuteerror = discord.Embed(title="Missing Arguement", color=0xfea9ef)
    unmuteerror.add_field(name="How to use?", value=f"{prefixW}Unmute [@user]/[user ID], for example: {prefixW}mute @jim", inline=False)

    unmute = discord.Embed(title="Unmute", color=0xfea9ef)
    unmute.add_field(name=f"Sucessfully unmuted {member} | ID: {member.id}", value="", inline=False)
    if member == None:
        await ctx.send(embed=unmuteerror, delete_after=5.0)

    else:
        timeOut = datetime.timedelta(seconds=0)
        await member.edit(timed_out_until=discord.utils.utcnow() + timeOut)
        await ctx.send(embed=unmute, delete_after=5.0)

@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member:discord.Member=None, time=None):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")

    embedmute = discord.Embed(title="Mute", color=0xfea9ef)
    embedmute.add_field(name=f"Sucessfully muted {member} | ID: {member.id}", value="", inline=False)

    embederror = discord.Embed(title="Missing Arguement", color=0xfea9ef)
    embederror.add_field(name="How to use?", value=f"{prefixW}mute [@user]/[user ID] [s]/[m]/[h], for example: {prefixW}mute @jim 10m", inline=False)

    if member == None:
        await ctx.message.delete()
        await ctx.send(embed=embederror, delete_after=5.0)
        return
    if time == None:
        await ctx.message.delete()
        await ctx.send(embed=embederror, delete_after=5.0)
        return

    if "s" in time:
        # this gets time sent in chat and strips "S"
        timeG = time.strip("s")
        # this gets the current time date and adds the additional time
        timeN = datetime.timedelta(seconds=int(timeG))
        #here it times out the user until the time now (discord.utils.utcnow) + the additional time
        await member.edit(timed_out_until=discord.utils.utcnow()+timeN)
        await ctx.message.delete()
        await ctx.send(embed=embedmute, delete_after=5.0)

    if "S" in time:
        # this gets time sent in chat and strips "S"
        timeG = time.strip("S")
        # this gets the current time date and adds the additional time
        timeN4 = datetime.timedelta(seconds=int(timeG))
        #here it times out the user until the time now (discord.utils.utcnow) + the additional time
        await member.edit(timed_out_until=discord.utils.utcnow()+timeN4)
        await ctx.message.delete()
        await ctx.send(embed=embedmute, delete_after=5.0)


    elif "m" in time:
        timeG2 = time.strip("m")
        timeN2 = datetime.timedelta(minutes=int(timeG2))
        await member.edit(timed_out_until=discord.utils.utcnow()+timeN2)
        await ctx.message.delete()
        await ctx.send(embed=embedmute, delete_after=5.0)

    elif "M" in time:
        timeG2 = time.strip("M")
        timeN5 = datetime.timedelta(minutes=int(timeG2))
        await member.edit(timed_out_until=discord.utils.utcnow()+timeN5)
        await ctx.message.delete()
        await ctx.send(embed=embedmute, delete_after=5.0)


    elif "h" in time or "H" in time:
        timeG2 = time.strip("h")
        timeN3 = datetime.timedelta(days=int(timeG2))
        await member.edit(timed_out_until=discord.utils.utcnow()+timeN3)
        await ctx.message.delete()
        await ctx.send(embed=embedmute, delete_after=5.0)

    elif "H" in time:
        timeG2 = time.strip("H")
        timeN3 = datetime.timedelta(days=int(timeG2))
        await member.edit(timed_out_until=discord.utils.utcnow()+timeN3)
        await ctx.message.delete()
        await ctx.send(embed=embedmute, delete_after=5.0)

    else:
        await ctx.message.delete()
        await ctx.send(embed=embederror, delete_after=5.0)


# - unban - #

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, member:discord.User = None):
    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")

    if member is None or member == ctx.message.author:
        embed = discord.Embed(title="Missing Arguement", description="Unban a user", color=0xfea9ef)
        embed.add_field(name="How to use?", value=f"{prefixW}Unban [user ID]", inline=False)
        await ctx.send(embed=embed, delete_after=5.0)
        return
    else:
        guild = ctx.guild
        embed=discord.Embed(title="Unban", description=f"User {member} has been unbanned | ID: {member.id}")
        await ctx.send(embed=embed, delete_after=5.0)
        await guild.unban(user=member)

# - filter - #
with open("prefix.json", "r") as prefixL:
    prefixT = json.load(prefixL)
prefixC = prefixT[0].replace("'", "")

MisWord = discord.Embed(title="Missing Arguement", description="Add a word to your filter list", color=0xfea9ef)
MisWord.add_field(name="How to use?", value=f"{prefixC}addbanword [word], for example: {prefixC}addbanword stinky", inline=False)

MisWordW = discord.Embed(title="Missing Arguement", description="Add a word to your filter list", color=0xfea9ef)
MisWordW.add_field(name="How to use?", value=f"{prefixC}addwarnword [word], for example: {prefixC}addwarnword stinky", inline=False)

MisWord2 = discord.Embed(title="Missing Arguement", description="Add a word to your filter list", color=0xfea9ef)
MisWord2.add_field(name="How to use?", value=f"{prefixC}removebanword [word], for example: {prefixC}removebanword stinky", inline=False)

MisWordW2 = discord.Embed(title="Missing Arguement", description="Add a word to your filter list", color=0xfea9ef)
MisWordW2.add_field(name="How to use?", value=f"{prefixC}removewarnword [word], for example: {prefixC}removewarnword stinky", inline=False)

MisWord3 = discord.Embed(title="Missing Arguement", description="Add a word to your filter list", color=0xfea9ef)
MisWord3.add_field(name="How to use?", value=f"{prefixC}deletebanword [word], for example: {prefixC}deletebanword stinky", inline=False)

MisWordW3 = discord.Embed(title="Missing Arguement", description="Add a word to your filter list", color=0xfea9ef)
MisWordW3.add_field(name="How to use?", value=f"{prefixC}deletewarnword [word], for example: {prefixC}deletewarnword stinky", inline=False)

AddSuc = discord.Embed(title="Addition Success!", description="", color=0xfea9ef)
AddSuc.add_field(name="This word has been added to the list successfully!", value="", inline=False)

AddError = discord.Embed(title="Error!", description="", color=0xfea9ef)
AddError.add_field(name="This word has already been added to the list!", value="", inline=False)

DeleteSuc = discord.Embed(title="Delete Success!", description="", color=0xfea9ef)
DeleteSuc.add_field(name="This word has been deleted from the list successfully!", value="", inline=False)

DeleteError = discord.Embed(title="Error!", description="", color=0xfea9ef)
DeleteError.add_field(name="Unable to delete the word because it is not in the word filter list!", value="", inline=False)

WarnEm = discord.Embed(title="Do not be inappropriate!", description="", color=0xfea9ef)
WarnEm.add_field(name="", value="", inline=False)

@bot.command()
@commands.has_permissions(administrator=True)
async def addbanword(ctx, word=None):

    # some reason it doesn't work without having to import json into the function directly
    import json

    if word == None:
        await ctx.send(embed=MisWord, delete_after=5.0)
    else:
        # loads json file
        with open("bannedwords.json", "r") as bannedwordL:
            bannedword = json.load(bannedwordL)
        # loop for every word in list
        if word not in bannedword:
            # adds word from array
            bannedword.append(word)
            # easy way of removing duplicates
            newlist = [*set(bannedword)]
            # writes into json and saves it
            with open("bannedwords.json", "w") as bannedwordL:
                json.dump(newlist, bannedwordL)
            # sends message after word is appended to array
            await ctx.send(embed=AddSuc, delete_after=5.0)
            return
        if word in bannedword:
            await ctx.send(embed=AddError, delete_after=5.0)
            return

@bot.command()
@commands.has_permissions(administrator=True)
async def addwarnword(ctx, word=None):
    # some reason it doesn't work without having to import json into the function directly
    import json

    if word == None:
        await ctx.send(embed=MisWordW, delete_after=5.0)
    else:
        # loads json file
        with open("warningwords.json", "r") as warnwordL:
            warnword = json.load(warnwordL)
        # loop for every word in list
        if word not in warnword:
            # adds word from array
            warnword.append(word)
            # easy way of removing duplicates
            newlist = [*set(warnword)]
            # writes into json and saves it
            with open("warningwords.json", "w") as warnword:
                json.dump(newlist, warnword)
            # sends message after word is appended to array
            await ctx.send(embed=AddSuc, delete_after=5.0)
            return
        if word in warnword:
            await ctx.send(embed=AddError, delete_after=5.0)
            return

@bot.command()
@commands.has_permissions(administrator=True)
async def removebanword (ctx, word:str=None):
    # some reason it doesn't work without having to import json into the function directly
    import json

    if word == None:
        await ctx.send(embed=MisWord2, delete_after=5.0)

    # loads json file
    else:
        with open("bannedwords.json", "r") as list:
            filter = json.load(list)

        if word in filter:
            # removes the word from the array
            filter.remove(word)
            # easy way of removing duplicates
            newlist = [*set(filter)]
            # writes into json and saves it
            with open("bannedwords.json", "w") as list:
                json.dump(newlist, list)
            # sends message after word is appended to array
            await ctx.send(embed=DeleteSuc, delete_after=5.0)
            return
        else:
            await ctx.send(embed=DeleteError, delete_after=5.0)
            return

@bot.command()
@commands.has_permissions(administrator=True)
async def removewarnword (ctx, word:str=None):
    # some reason it doesn't work without having to import json into the function directly
    import json

    if word == None:
        await ctx.send(embed=MisWordW2, delete_after=5.0)

    # loads json file
    else:
        with open("warningwords.json", "r") as list:
            filter = json.load(list)

        if word in filter:
            # removes the word from the array
            filter.remove(word)
            # easy way of removing duplicates
            newlist = [*set(filter)]
            # writes into json and saves it
            with open("warningwords.json", "w") as list:
                json.dump(newlist, list)
            # sends message after word is appended to array
            await ctx.send(embed=DeleteSuc, delete_after=5.0)
            return
        else:
            await ctx.send(embed=DeleteError, delete_after=5.0)
            return

@bot.command()
@commands.has_permissions(administrator=True)
async def deletebanword (ctx, word=None):
    # some reason it doesn't work without having to import json into the function directly
    import json

    if word == None:
        await ctx.send(embed=MisWord3, delete_after=5.0)

    else:
        # loads json file
        with open("bannedwords.json", "r") as list:
            filter = json.load(list)
        if word in filter:
            # removes the word from the array
            filter.remove(word)
            # easy way of removing duplicates
            newlist = [*set(filter)]
            # writes into json and saves it
            with open("bannedwords.json", "w") as list:
                json.dump(newlist, list)
            # sends message after word is appended to array
            await ctx.send(embed=DeleteSuc, delete_after=5.0)
            return
        else:
            await ctx.send(embed=DeleteError, delete_after=5.0)
            return

@bot.command()
@commands.has_permissions(administrator=True)
async def deletewarnword (ctx, word=None):
    # some reason it doesn't work without having to import json into the function directly
    import json

    if word == None:
        await ctx.send(embed=MisWordW3, delete_after=5.0)

    else:
        # loads json file
        with open("warningwords.json", "r") as list:
            filter = json.load(list)
        if word in filter:
            # removes the word from the array
            filter.remove(word)
            # easy way of removing duplicates
            newlist = [*set(filter)]
            # writes into json and saves it
            with open("warningwords.json", "w") as list:
                json.dump(newlist, list)
            # sends message after word is appended to array
            await ctx.send(embed=DeleteSuc, delete_after=5.0)
            return
        else:
            await ctx.send(embed=DeleteError, delete_after=5.0)
            return

@bot.command()
@commands.has_permissions(administrator=True)
async def filter(ctx):
    import json
    with open("bannedwords.json", "r") as list:
        filter = json.load(list)
    with open("warningwords.json", "r") as warnwordList:
        warningword = json.load(warnwordList)
    # for every word in the banned words list it joins them together with a comma and space.
    word1 = str(', '.join(filter))
    word2 = str(', '.join(warningword))
    Word1 = discord.Embed(title="Filter list", description="", color=0xfea9ef)
    Word1.add_field(name=f"The list of banned words are:", value=f"{word1}", inline=False)
    Word2 = discord.Embed(title="Filter list", description="", color=0xfea9ef)
    Word2.add_field(name=f"The list of warning words are:", value=f"{word2}", inline=False)
    await ctx.send(embed=Word1, delete_after=5.0)
    await ctx.send(embed=Word2, delete_after=5.0)

@bot.event
async def on_message(message):
    global bannedword
    global warnword
    messageCont = message.content.lower()

    with open("prefix.json", "r") as prefixL:
        prefixD = json.load(prefixL)
    prefixW = prefixD[0].replace("'", "")

    ping = discord.Embed(title="Prefix", description="", color=0xfea9ef)
    ping.add_field(name=f"This bot's prefix is: {prefixW}", value="", inline=False)

    if bot.user.mentioned_in(message):
        await message.channel.send(embed=ping, delete_after=5.0)

    # for loop for every word that is in the list
    if message.author.guild_permissions.administrator:
        await bot.process_commands(message)
        return

    else:
        for words in bannedword:
            # checks if the message author is a bot
            if message.author.bot:
                return

            # if nothing fits the requirements it runs the code below
            else:

                # if word is the messageCont ( variable for message.content.lower() ) it will send this message
                if words in messageCont:
                    await message.delete()
                    BanW = discord.Embed(title="Message Delete!", description="", color=0xfea9ef)
                    BanW.add_field(name=f"<@{message.author.id}> Please do not be inappropriate!", value="", inline=False)
                    await message.channel.send(embed=BanW, delete_after=5.0)
                    timeOut = datetime.timedelta(hours=24)
                    await message.author.edit(timed_out_until=discord.utils.utcnow()+timeOut)
                    return

            # Allows other commands to work whilst also listening to chats
        for words1 in warnword:
            # checks if the message author is a bot
            if message.author.bot:
                return

            # if nothing fits the requirements it runs the code below
            else:
                # if word is the messageCont ( variable for message.content.lower() ) it will send this message
                if words1 in messageCont:
                    await message.delete()
                    WarnW = discord.Embed(title="Message Delete!", description="", color=0xfea9ef)
                    WarnW.add_field(name=f"<@{message.author.id}> Please do not be inappropriate!", value="", inline=False)
                    await message.channel.send(embed=WarnW, delete_after=5.0)
                    return

            # Allows other commands to work whilst also listening to chats
    await bot.process_commands(message)
    return

Tokens = [   'TOKEN'  ] #working

TOKEN = Tokens[ botID % len(Tokens) ]
print( TOKEN , botID % len(Tokens)  )

DISCORD_GUILD = 'Codewrangling'
bot.run(TOKEN)
