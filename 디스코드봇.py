import discord
import asyncio
import time
import os


countG = 0
client = discord.Client()
players = {}
queues= {}
musiclist=[]

def check_queue(id):
    if queues[id]!=[]:
        player = queues[id].pop(0)
        players[id] = player
        del musiclist[0]
        player.start()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='"도움말"입력', type=1))



@client.event
async def on_member_join(member):
    fmt = '{0.mention} 님환영합니다'
    channel = member.server.get_channel("520152171338268672")
    await client.send_message(channel, fmt.format(member, member.server))
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("520152171338268672")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))    

@client.event
async def on_message(message):
                    
    if message.content.startswith("모두모여"):
       await client.send_message(message.channel, "@everyone")
 
    if message.content.startswith("신청서 주소"):
       embed = discord.Embed(title="신청서 주소", description="https://docs.google.com/forms/d/e/1FAIpQLSfzEuv2SFgEO17gVKZfZHwa3YjALc9zEYbIlc6MmeDzTUef2w/viewform 입니다 , 그리고 팀모아서 오시거나 팀이 없다면 runkan#0001 로 마크 닉과 이메일을 주세요.", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)
        
    if message.content.startswith('봇 제작자'):
       embed = discord.Embed(title="봇 제작자", description="#0025입니다 공백이 들어가 있습니다.", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)
       
    if message.content.startswith('유튜브'):
       embed = discord.Embed(title="런칸님의 유튜브 채널!", description="https://www.youtube.com/channel/UCrepox4D94t7RZCNRdoSaDQ", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)   
        
    if message.content.startswith('초대링크'):
       embed = discord.Embed(title="디스코드방 초대링크", description=" https://discord.gg/mgHaBwT", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)
       
    if message.content.startswith('봇 초대'):
       embed = discord.Embed(title="런칸 봇 추가", description="https://discordapp.com/oauth2/authorize?client_id=492857931843371008&scope=bot&permissions=1610087799", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)

    if message.content.startswith('오늘배그'):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="배그각입니다.", color=discord.Color.blue()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="자러갑시다....", color=discord.Color.red()))

    if message.content.startswith('ban'):
         try:
             if message.author.server_permissions.administrator:
                 learn = message.content.split(' ')
                 member = discord.utils.get(client.get_all_members(),id=learn[1])
                 await client.ban(member, 1)
                 await client.send_message(channel,'성공적으로 벤이 완료되었습니다.')
             else:
                 await client.send_message(channel,'관리자 권한이 있어야 합니다!')
         except:
                 await client.send_message(channel,'그 유저가 권한이 높거나 같거나 봇 권한없습니다.')
        
    if message.content.startswith('kick'):
         try:
             if message.author.server_permissions.administrator:
                 learn = message.content.split(' ')
                 member = discord.utils.get(client.get_all_members(),id=learn[1])
                 await client.kick(member)
                 await client.send_message(channel,'성공적으로 킥이 완료되었습니다.')
             else:
                 await client.send_message(channel,'관리자 권한이 있어야 합니다!')
         except:
                 await client.send_message(channel,'그 유저가 권한이 높거나 같거나 봇 권한없습니다.')



    if message.content.startswith('ping'):
         before = time.monotonic()
         msg = await client.send_message(message.channel, '핑측정중...')
         ping = (time.monotonic() - before) * 1000
         text = ":ping_pong:!  {0}ms".format((round(ping,1)))
         embed = discord.Embed(title='핑',description=text,color=0x00ff00)
         await client.edit_message(msg,embed=embed)            

    if message.content.startswith('고양이'):
        embed = discord.Embed(
            title='고양이는',
            description='야옹야옹',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('도움말'):
       embed = discord.Embed(title="도움말",color=0x00ff00)
       embed = discord.Embed(description="신청서 주소 , 신청서 주소 , 봇 제작자 , 유튜브 , 타이머 , 봇 초대 , 주사위 , 복권 , 이모티콘 , 오늘배그 , 초대링크", color=0x00ff00)
       await client.send_message(message.channel, embed=embed)

    if message.content.startswith("복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('이모티콘'):

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] # 이모티콘 배열입니다.

        randomNum = random.randrange(0, len(emoji)) # 0 ~ 이모티콘 배열 크기 중 랜덤숫자를 지정합니다.
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await client.send_message(message.channel, embed=discord.Embed(description=emoji[randomNum])) # 랜덤 이모티콘을 메시지로 출력합니다.

    if message.content.startswith('주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))

    if message.content.startswith('타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint

        for i in range(sec, 0, -1):
            print(i)
            await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)

        else:
            print("땡")
            await client.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))

    if message.content.startswith('공지'):

        embed = discord.Embed(title="입력", description="보낼 메시지를 입력하시오..", color=0x00ff00)

        await client.send_message(message.channel, embed=embed)
        
        msg = await client.wait_for_message()
        if msg is None:

            

            return

        else:

            channel = discord.Object(id='527778051728343041')

            await client.send_message(channel, msg.content)

            await client.send_message(message.channel, '성공!')
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
       
