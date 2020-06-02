import discord

client = discord.Client()
token = 'NzE3MTc1NjE3Njk0NzI4MzM0.XtWgOQ.KkyalarZIuE3zuq4o-J4-KUBk3M'

@client.event
async def on_ready():
    print('I ready bitch')

client.run(token)
