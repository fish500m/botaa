import discord
import asyncio
import random
import openpyxl
import urllib
import urllib.request
import bs4
import os
import sys
import json
import datetime
import time

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='"도움말"입력', type=1))  

@client.event
async def on_message(message):


     if message.content.startswith("서버주소"):
        channel = message.channel
        embed = discord.Embed(
            title = '서버주소들 입니다.',
            description = '가고 싶은 서버에 가세요! 단 차단된서버는 못갑니다.',
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
        embed.add_field(name='**마인크래프트코리아**', value = 'https://discord.gg/mgHaBwT',inline = False)
        embed.add_field(name='**카트라이더**', value='https://discord.gg/Mweertm', inline=False)
        embed.add_field(name='**프리즘**', value='https://discord.gg/Mweertm', inline=False)
        embed.add_field(name='**이브 네트워크**', value='https://discord.gg/vPaaf7a', inline=False)

        
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
        embed.add_field(name='봇 제작자 or 봇제작자', value='봇제작자 알려줌', inline=False)
        embed.add_field(name='유튜브 채널 or 유튜브', value='유튜브 채널 알려줌', inline=False)
        embed.add_field(name='런칸봇 초대 or 봇 초대', value='봇의 초대링크를 알려줌', inline=False)
        embed.add_field(name='프로필', value='사용법 : @멘션', inline=False)
        embed.add_field(name='서버주소', value='디스코드 서버주소를 알려줌', inline=False)        



        await client.send_message(channel,embed=embed)        

     if message.content.startswith("GG구구"):
        embed = discord.Embed(title="구구!", color=0x00ff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/541153887847972864/545524626474926082/unknown.png")
        await client.send_message(message.channel, embed=embed)      
        
     if message.content.startswith('봇 제작자') or message.content.startswith('봇제작자'):
       embed = discord.Embed(title="봇 제작자", description="#0025입니다 공백이 들어가 있습니다.", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)
       
     if message.content.startswith('유튜브 채널') or message.content.startswith('유튜브'):
       embed = discord.Embed(title="런칸님의 유튜브 채널!", description="https://www.youtube.com/channel/UCrepox4D94t7RZCNRdoSaDQ", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)   
       
     if message.content.startswith('런칸봇 초대') or message.content.startswith('봇 초대'):
       embed = discord.Embed(title="런칸 봇 추가", description="https://discordapp.com/oauth2/authorize?client_id=492857931843371008&scope=bot&permissions=1610087799", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)

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

     if message.content.startswith("공지"):

        await client.send_message(message.channel, '보낼 메시지를 입력해 주세요.(최대한 빠르게)')

        msg = await client.wait_for_message()

 

        if msg is None:

            

            return

        else:

            channel = discord.Object(id='549473115340668949')

            await client.send_message(channel, msg.content)

            await client.send_message(message.channel, '성공적으로 전송을 했습니다.')

         
         

access_token = os.environ [ " BOT_TOKEN " ] 
client.run (access_token)
       
