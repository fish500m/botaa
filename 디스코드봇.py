import discord
import random
import openpyxl
import datetime
import os
import time



client = discord.Client()
times = int(time.time())


    
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
        
     if message.content.startswith("도움말"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어들이다 크크크큭',
            description = '베타입니다',
            colour = discord.Colour.blue()
        )

        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name='도움말', value = '이메시지 생성!',inline = False)
        embed.add_field(name='프로필 @멘션', value='프로필을 보여줌', inline=False)

        await client.send_message(channel,embed=embed)  
        
     if message.content.startswith('따라해'):
        if id in owner:
         learn = message.content.replace('따라해', "")
         await client.delete_message(message) 
         await client.send_message(message.channel,learn+'')     
        else:
          await client.send_message(channel,'')         
        
     if message.content.startswith('say'):
        learn = message.content.replace('say', "")
        await client.send_message(message.channel,learn+'') 
        
     if message.content.startswith("프로필"):

        text = ""

        learn = message.content.split(" ")

        vrsize = len(learn)

        vrsize = int(vrsize)

        for i in range(1, vrsize):
            text = text + " " + learn[i]
        for user in message.mentions:
            embed = discord.Embed(color=0xffffff)
            embed.set_image(url=user.avatar_url)
            await client.send_message(message.channel, embed=embed)        
        
     if message.content.startswith('공지'):
        if id in owner:
         learn = message.content.replace('공지', "")        
         channel = discord.Object(id='561487738025803787')
         await client.send_message(channel,learn+'')                       # await client.send_message(message.channel,learn+'')
        else:
          await client.send_message(channel,'권한이 없습니다!') 
        
     if message.content.startswith('업타임'):
          a = int(time.time())
          await client.send_message(channel,str(a-times)+'초')         


access_token = os.environ["BOT_TOKEN"] 
client.run (access_token)
       
