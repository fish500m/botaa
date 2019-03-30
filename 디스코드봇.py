import discord
import os



client = discord.Client()



    
@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='별로 없어요', type=1))  


@client.event
async def on_message(message):


     id = message.author.id
     channel = message.channel
     owner = ['545692889292734474','480568196286644224','375951816384446464','536133196706873352']
     if message.author.bot:
          return None
        
     if message.content.startswith('따라해'):
         try:
             if message.author.server_permissions.administrator:
         learn = message.content.replace('따라해', "")
         await client.delete_message(message) 
         await client.send_message(message.channel,learn+'')     
        else:
          await client.send_message(channel,'')         
        
     if message.content.startswith('say'):
        learn = message.content.replace('say', "")
        await client.delete_message(message) 
        await client.send_message(message.channel,learn+'')         
        
        


access_token = os.environ["BOT_TOKEN"] 
client.run (access_token)
       
