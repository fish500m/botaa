import discord 
import setting
import datetime
import time
import os


set = setting.set()

client = discord.Client()

app = discord.Client()

times = int(time.time())

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
     owner = ['558893178732806147','480568196286644224','375951816384446464','536133196706873352']
     if message.author.bot:
          return None
    
     if message.author.id == app.user.id: return


     print("Channel: %s(%s) | Author: %s(#%s) | Message: %s" % (
            message.channel, str(message.channel.id)[:5],
            message.author.name, str(message.author.id),
            message.content
	    	))
	
     if message.content.startswith('게임'):
        if id in owner:         
           learn = message.content.replace('게임', "")
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
	

  
	
     if message.content.startswith('say'):
        learn = message.content.replace('say', "")
        await app.send_message(message.channel,learn+'') 
        
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
            embed.set_footer(text="공지")
            mssg = await app.send_message(message.channel, embed=embed)
            a = []
            b = []
            e = []
            ec = {}
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신중!", value="<@" + message.author.id + ">", inline=True)
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
            embed.set_footer(text="공지")
            await app.edit_message(mssg, embed=embed)
        else:
            await app.send_message(message.channel, "봇 제작자만 사용할수 있는 커맨드입니다!")
            
 
access_token = os.environ["BOT_TOKEN"] 
app.run (access_token)
