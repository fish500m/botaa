import discord 
import setting
import datetime
import time
import os
import random
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
     owner = ['480568196286644224','375951816384446464','536133196706873352','558893178732806147']
     if message.author.bot:
          return None
    
     if message.author.id == app.user.id: return




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
            await app.send_message(message.channel, "봇 제작자만 사용할수 있는 커맨드입니다!")            

            

app.run('NTYxNTQxMjE4MTQ5MDcyODk2.XJ9wBg.IJZCKYLQPH1rWQa_fYDPcpl7D4U')
