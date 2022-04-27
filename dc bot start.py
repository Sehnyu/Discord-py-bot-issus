import discord

from discord.ext import commands


TOKEN = "Token [I do have one]"

client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("bot is ready as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0] 
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"({username} in {channel}): {user_message}")

    if message.author == client.user:
        return
    
    if user_message.lower() == "hello": 
        await message.channel.send(f"Hello {username}")
        return 



@client.event
async def on_message(message):
    user_message = str(message.content)
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name)
    print(f"in ({channel}) from {username}: {user_message}")

    if user_message.lower() == "respond":
        await message.author.send(f"**_responded_**!")
        return

# The msg fromate is different, i was mid changing it

@client.event
async def on_message(message):
    user_message = str(message.content)
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name)
    print(f"in ({channel}) from {username}: {user_message}")

    if user_message.lower() == "club tag":
        await message.channel.send(f"#VCYJV99Q")
        return






client.run(TOKEN)