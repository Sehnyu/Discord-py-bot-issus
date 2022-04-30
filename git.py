import discord

from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix = "-") #prefix 

@client.event
async def on_ready():
    print("bot is ready as {0.user}".format(client))

#works now
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0] 
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username} in ({channel}): {user_message}")

    if message.author == client.user:
        return
    
    #Hello
    if user_message.lower() == "hello": 
        await message.channel.send(f"Hello {username}")
        return 
    
    #Respond
    elif user_message.lower() == "respond":
        await message.author.send(f"**_responded_**!")
        return
    
    #Club tag
    elif user_message.lower() == "club tag":
        await message.channel.send(f"#VCYJV99Q")
        return

#has not been tested
@client.event
async def on_member_join(member):
    print(f"{member} welcome to the server")

#has not been tested
@client.event
async def on_member_leave(member):
    print(f"Sad to see you go {member} ")


#issue
@client.command()
async def ping(ctx):
    await ctx.send("pong")


client.run(TOKEN)