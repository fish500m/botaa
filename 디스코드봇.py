import discord
import asyncio
import random
import urllib
import encodings
import urllib.request
import bs4
import sys
import json
import datetime
import time

client = discord.Client()
times = int(time.time())


    
@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='"도움말"입력"하세요!', type=1))  

@client.event
async def my_background_task():
        await client.wait_until_ready()
        channel = discord.Object(id='514078681094684672')
        while not client.is_closed:
            await client.send_message(channel, "헤브어님 소스를 사용중입니다")
            await asyncio.sleep(60*24) 

@client.event
async def on_message(message):



     id = message.author.id
     channel = message.channel
     owner = ['545692889292734474','480568196286644224']
     if message.author.bot:
          return None

     if message.content.startswith("관리자도움말"):       
         channel = message.channel
         embed = discord.Embed(
            title = '명령어들이다 크크크큭',
            description = '각각의 명령어들 이다 잘 봐둬라 큭...',
            colour = discord.Colour.blue()
        )

        #embed.set_footer(text = '끗')
         dtime = datetime.datetime.now() 
         embed.add_field(name='베이비기타문의', value='특정채널에 보낸다!', inline=False)
         embed.add_field(name='베이비잡담', value='특정채널에 보낸다!', inline=False)
         embed.add_field(name='베이비테스트', value='특정채널에 보낸다!', inline=False)
         embed.add_field(name='베이비지식인', value='특전채널에 메시지를 보낸다!', inline=False)
         embed.add_field(name='봇끄기', value='장비를 정지합니다', inline=False)
         await client.send_message(channel,embed=embed)       
        
     if message.content.startswith("도움말"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어들이다 크크크큭',
            description = '각각의 명령어들 이다 잘 봐둬라 큭...',
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
        embed.add_field(name='프로필', value='사용법 : @멘션', inline=False)
        embed.add_field(name='봇게임', value='봇게임 (할게임)', inline=False)
        embed.add_field(name='ping', value='핑확인', inline=False)
        embed.add_field(name='전용', value='놀는명령어', inline=False)
        embed.add_field(name='버려', value='주인님 양심 테스트', inline=False)
        embed.add_field(name='넌누구니?', value='주인확인', inline=False)
        embed.add_field(name='업타임', value='봇을 킨시간 확인용', inline=False)
        embed.add_field(name=';', value='세미콜론', inline=False)
        embed.add_field(name='ㅠ', value='운다', inline=False)

        



        await client.send_message(channel,embed=embed)
        
     if message.content.startswith('봇끄기'):
          if id in owner:
               await client.send_message(channel,':wave:')
               await client.logout() 
          else:
               await client.send_message(channel,'권한이 없습니다!')
               
     if message.content.startswith('베이비1'):
        if id in owner:
         learn = message.content.replace('베이비1', "")        
         channel = discord.Object(id='537609029019631616')
         await client.send_message(channel,learn+'')                       # await client.send_message(message.channel,learn+'')
        else:
          await client.send_message(channel,'권한이 없습니다!')
          

     if message.content.startswith('베이비2'):
        if id in owner:
         learn = message.content.replace('베이비2', "")        
         channel = discord.Object(id='514078770152341504')
         await client.send_message(channel,learn+'')                       # await client.send_message(message.channel,learn+'')
        else:
          await client.send_message(channel,'권한이 없습니다!')
          
     if message.content.startswith('베이비3'):
        if id in owner:
         learn = message.content.replace('베이비3', "")        
         channel = discord.Object(id='514078681094684672')
         await client.send_message(channel,learn+'')                       # await client.send_message(message.channel,learn+'')
        else:
          await client.send_message(channel,'권한이 없습니다!')
         

     if message.content.startswith('베이비4'):
        if id in owner:
         learn = message.content.replace('베이비4', "")        
         channel = discord.Object(id='536608073641361410')
         await client.send_message(channel,learn+'')                       # await client.send_message(message.channel,learn+'')
        else:
          await client.send_message(channel,'권한이 없습니다!')

     if message.content.startswith('공지'):
        if id in owner:
         learn = message.content.replace('공지', "")        
         channel = discord.Object(id='558859235212001280')
         await client.send_message(channel,learn+'')                       # await client.send_message(message.channel,learn+'')
        else:
          await client.send_message(channel,'권한이 없습니다!')          
               
     if message.content.startswith("전용"):        
          await client.send_message(channel,'아잇! 간지러워요ㅋㅋㅋ')
          
     if message.content.startswith("넌누구니?"):        
          await client.send_message(channel,'전 @디스코드#0025님의 주인님이에요!')

     if message.content.startswith("버려"):        
          await client.send_message(channel,'주인님이날 버리다니 흑흑:disappointed_relieved: ')

     if message.content.startswith("ㅠ"):        
          await client.send_message(channel,'얘운다 ㅋㅋㅋ')
          
     if message.content.startswith(";"):        
          await client.send_message(channel,'세미콜론')

     if message.content.startswith("넌어디서왔니?"):        
          await client.send_message(channel,'나는 파이썬에서 왔지!')          

          

    

        
     if message.content.startswith('봇게임'):
          if id in owner :
               learn = message.content.split(' ')
               await client.change_presence(game=discord.Game(name=learn[1]))
               await client.send_message(channel,'봇의 게임을 바꾸었습니다.')
          else:
               await client.send_message(channel,'권한이 없습니다!')
        

               

             
     if message.content.startswith('업타임'):
          a = int(time.time())
          await client.send_message(channel,str(a-times)+'초')             
             
     if message.content.startswith('ping'):
         before = time.monotonic()
         msg = await client.send_message(message.channel, '핑측정중...')
         ping = (time.monotonic() - before) * 1000
         text = ":ping_pong:!  {0}ms".format((round(ping,1)))
         embed = discord.Embed(title='핑',description=text,color=0x00ff00)
         await client.edit_message(msg,embed=embed)
         
       

    

         
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


            

client.loop.create_task(my_background_task())
access_token = os.environ [ " BOT_TOKEN " ] 
client.run (access_token)
       
