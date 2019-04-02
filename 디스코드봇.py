import setting
import discord
import asyncio
import random
import time
from urllib.request import urlopen, Request
import urllib
import bs4
from urllib.request import Request
import openpyxl
import re
import requests
from bs4 import BeautifulSoup
import datetime
import os
import sys
import json
from selenium import webdriver
set = setting.set()


app = discord.Client()


maker = "480568196286644224"


@app.event
async def on_ready():
    print("login")
    print(app.user.name)
    print(app.user.id)
    print("------------------")
    await app.change_presence(game=discord.Game(name='별로 없어요', type=1))
    
@app.event
async def on_message(message):

     id = message.author.id
     channel = message.channel
     owner = ['480568196286644224','375951816384446464','536133196706873352']
     if message.author.bot:
          return None
    
     if message.author.id == app.user.id: return


     print("Channel: %s(%s) | Author: %s(#%s) | Message: %s" % (
            message.channel, str(message.channel.id)[:5],
            message.author.name, str(message.author.id),
            message.content
	    	))
	
     if message.content.startswith('봇게임'):
        if id in owner:         
           learn = message.content.replace('봇게임', "")
           await app.change_presence(game=discord.Game(name=learn))
           await app.send_message(message.channel, "봇의 플래이중을 바꿨습니다.")
        else:
           await app.send_message(channel,'')
	
     if message.content.startswith('서버'):

         list = []
         for server in app.servers:
             list.append(server.name)
         await app.send_message(message.channel, "\n".join(list))

     if message.content.startswith('시간'):
        channel = message.channel
        embed = discord.Embed(colour = discord.Colour.blue())

        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()         
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        await app.send_message(channel,embed=embed)



     if message.content.startswith('업타임'):
          a = int(time.time())
          await app.send_message(channel,str(a-times)+'초')

	
     if message.content.startswith('서버정보'):
           embed = discord.Embed(title="\"%s\" 서버정보!" % (message.server.name), description=None, color=Setting.embed_color)
           embed.add_field(name="서버 소유자", value="<@%s>" % message.server.owner.id, inline=False)
           embed.add_field(name="서버 생성일", value="%s (UTC)" % (message.server.created_at), inline=False)
           embed.add_field(name="서버 보안등급", value=message.server.verification_level, inline=False)
           embed.add_field(name="서버 위치", value=message.server.region, inline=False)
           embed.add_field(name="서버 잠수채널", value="%s (%s분 이상 잠수이면 이동됨)" % (message.server.afk_channel, message.server.afk_timeout/60), inline=False)
           embed.set_thumbnail(url=message.server.icon_url)
           embed.set_footer(text = "Server ID : %s | Ver. %s | %s" % (message.server.id, Setting.version, Copyright))
           await app.send_message(message.channel, embed=embed)
	
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

        await app.send_message(channel,embed=embed)  
        
     if message.content.startswith('따라해'):
        if id in owner:
         await app.delete_message(message)            
         learn = message.content.replace('따라해', "")
         await app.send_message(message.channel,learn+'')     
        else:
          await app.send_message(channel,'')

     if message.content.startswith('날씨'):
        try:
            embed = discord.Embed(title='잠시만요',description='불러오고있습니다!',color=0x00ff00)
            meg = await app.send_message(channel,embed=embed)
            learn = message.content.split(" ")
            location = learn[1]
            enc_location = urllib.parse.quote(location+'날씨')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bs_obj = bs4.BeautifulSoup(html, "html.parser")
            div = bs_obj.find("span",{"class":'todaytemp'})
            div2 = bs_obj.find("p",{"class":"cast_txt"})
            embed = discord.Embed(title=location+'날씨',description=div.text+'℃'+'\n'+div2.text+'\n'+'네이버 날씨',color=0x00ff00)
            await app.edit_message(meg,embed=embed)
        except:
           await app.send_message(channel,'없는 도시입니다!')
            
     if message.content.startswith('미세먼지'):
        try:
           embed = discord.Embed(title='잠시만요',description='불러오고있습니다!',color=0x00ff00)
           meg = await app.send_message(channel,embed=embed)
           learn = message.content.split(" ")
           location = learn[1]
           enc_location = urllib.parse.quote(location+'미세먼지')
           hdr = {'User-Agent': 'Mozilla/5.0'}
           url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
           req = Request(url, headers=hdr)
           html = urllib.request.urlopen(req)
           bs_obj = bs4.BeautifulSoup(html, "html.parser")
           div = bs_obj.find("em",{"class":'main_figure'})
           div2 = bs_obj.find("span",{'class':'update'})
           learn2 = int(div.text)
           if learn2 < 16:
               a = '최고'
           elif learn2 < 31:
               a = '좋음'
           elif learn2 < 41:
               a = '양호'
           elif learn2 < 51:
               a = '보통'
           elif learn2 < 76:
               a = '나쁨'
           elif learn2 < 101:
               a = '상당히 나쁨'
           elif learn2 < 151:
               a = '매우나쁨'
           elif learn2 > 150:
               a = '최악'
           embed = discord.Embed(title=learn[1]+'미세먼지',description='**'+str(learn2)+'㎍/㎥ \n'+a+'**\n'+div2.text+'\n'+'네이버 미세먼지/미세먼지 기준 미세미세8단계',color=0x00ff00)
           await app.edit_message(meg,embed=embed)
        except:
            await app.send_message(channel,'없는 도시 거나 도/시는 미세먼지 검색이 안됩니다.')

     if message.content.startswith('청소'):
        if id in owner:    
             learn = message.content.split(' ')
             mgs = []
             number = int(learn[1])
             async for x in app.logs_from(message.channel, limit = number+1):
                  mgs.append(x)
             await app.delete_messages(mgs)
             delembed = discord.Embed(title=":speech_left: 메세지 삭제됨. (이 메세지는 3초 후 삭제됩니다)",color=0x4286f4)
             delmsg = await app.send_message(channel,embed = delembed)
             await asyncio.sleep(3)
             await app.delete_message(delmsg)	
        else:
            await app.send_message(message.channel, "당신은 권한이 없습니다!")    	
	
     if message.content.startswith('초미세먼지'):
            learn = message.content.split(' ')
            embed = discord.Embed(title='잠시만요',description='불러오고있습니다!',color=0x00ff00)
            meg = await app.send_message(channel,embed=embed)
            location = learn[1]
            enc_location = urllib.parse.quote(location+'초미세먼지')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bs_obj = bs4.BeautifulSoup(html, "html.parser")
            div = bs_obj.find("em",{"class":'main_figure'})
            div2 = bs_obj.find("span",{'class':'update'})
            learn2 = int(div.text)
            if learn2 < 16:
                a = '최고'
            elif learn2 < 31:
                a = '좋음'
            elif learn2 < 41:
                a = '양호'
            elif learn2 < 51:
                a = '보통'
            elif learn2 < 76:
                a = '나쁨'
            elif learn2 < 101:
                a = '상당히 나쁨'
            elif learn2 < 151:
                 a = '매우나쁨'
            elif learn2 > 150:
                 a = '최악'
            embed = discord.Embed(title=learn[1]+'초미세먼지',description='**'+str(learn2)+'㎍/㎥ \n'+a+'**\n'+div2.text+'\n'+'네이버 초미세먼지/초미세먼지 기준 미세미세8단계',color=0x00ff00)
            await app.edit_message(meg,embed=embed)	

  
	
     if message.content.startswith('say'):
        learn = message.content.replace('say', "")
        await app.send_message(message.channel,learn+'') 

	
     if message.content.startswith('정보'):
           date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
           embed = discord.Embed(color=0x00ff00)
           embed.add_field(name="이름",value=message.author.name,inline=True)
           embed.add_field(name='서버닉네임',value=message.author.display_name, inline=True)
           embed.add_field(name='가입일',value=str(date.year) +'년' +str(date.month) + '월' + str(date.day) + '일', inline=True)
           embed.add_field(name='아이디',value=message.author.id,inline=True)
           embed.set_thumbnail(url=message.author.avatar_url)
           await app.send_message(channel,embed=embed)      
	
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
            await app.send_message(message.channel, embed=embed)  




     if message.content.startswith('공지'):
        if id in owner:
            notice = message.content.replace('공지', "")
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신 준비중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="admin", icon_url="https://cdn.discordapp.com/avatars/480568196286644224/028222f9980e8d76db87dde612ea430d.png?size=1024")	
            embed.set_footer(text="공지")
            mssg = await app.send_message(message.channel, embed=embed)
            a = []
            b = []
            e = []
            ec = {}
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="admin", icon_url="https://cdn.discordapp.com/avatars/480568196286644224/028222f9980e8d76db87dde612ea430d.png?size=1024")	
            embed.set_footer(text="봇공지")
            await app.edit_message(mssg, embed=embed)
            for server in app.servers:
                for channel in server.channels:
                    for tag in set.allowprefix:
                        if tag in channel.name:
                            dtat = True
                            for distag in set.disallowprefix:
                                if distag in channel.name:
                                    dtat = False
                            if dtat:
                                if not server.id in a:
                                    try:
                                        await app.send_message(channel, notice)
                                    except discord.HTTPException:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "HTTPException"
                                    except discord.Forbidden:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "Forbidden"
                                    except discord.NotFound:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "NotFound"
                                    except discord.InvalidArgument:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "InvalidArgument"
                                    else:
                                        a.append(str(server.id))
                                        b.append(str(channel.id))
            asdf = "```\n"
            for server in app.servers:
                if not server.id in a:
                    if set.nfct:
                        try:
                            ch = await app.create_channel(server, set.nfctname)
                            await app.send_message(ch, notice)
                        except:
                            asdf = asdf + str(server.name) + "[채널 생성 실패]\n"
                        else:
                            asdf = asdf + str(server.name) + "[채널 생성 및 재발송 성공]\n"
                    else:
                        asdf = asdf + str(server.name) + "\n"
            asdf = asdf + "```"
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신완료!", value="<@" + message.author.id + ">", inline=True)
            bs = "```\n"
            es = "```\n"
            for bf in b:
                bn = app.get_channel(bf).name
                bs = bs + str(bn) + "\n"
            for ef in e:
                en = app.get_channel(ef).name
                es = es + str(app.get_channel(ef).server.name) + "(#" + str(en) + ") : " + ec[ef] + "\n"
            bs = bs + "```"
            es = es + "```"
            if bs == "``````":
                bs = "``` ```"
            if es == "``````":
                es = "``` ```"
            if asdf == "``````":
                asdf = "``` ```"
            sucess = bs
            missing = es
            notfound = asdf
            embed.add_field(name="공지 발신 성공 채널:", value=sucess, inline=True)
            embed.add_field(name="공지 발신 실패 채널:", value=missing, inline=True)
            embed.add_field(name="공지 채널 없는 서버:", value=notfound, inline=True)
            embed.set_author(name="admin", icon_url="https://cdn.discordapp.com/avatars/480568196286644224/028222f9980e8d76db87dde612ea430d.png?size=1024")		
            embed.set_footer(text="봇 공지")
            await app.edit_message(mssg, embed=embed)
        else:
            await app.send_message(message.channel, "당신은 권한이 없습니다!")            

            
      

            

access_token = os.environ["BOT_TOKEN"] 
app.run (access_token)
