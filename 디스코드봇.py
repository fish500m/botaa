import discord
import os



client = discord.Client()



    
@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='"도움말"입력"하세요!', type=1))  


@client.event
async def on_message(message):


     id = message.author.id
     channel = message.channel
     owner = ['545692889292734474','480568196286644224']
     if message.author.bot:
          return None
        
     if message.content.startswith('따라해'):
        if id in owner:
         learn = message.content.replace('따라해', "")
         await client.delete_message(message) 
         await client.send_message(message.channel,learn+'')     
        else:
          await client.send_message(channel,'')         
        
        
        
        


access_token = os.environ["BOT_TOKEN"] 
client.run (access_token)
       
