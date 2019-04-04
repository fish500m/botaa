import discord 




client = discord.Client()






@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='별로 없어요', type=0))
    
@client.event
async def on_message(message):

     if message.content.startswith("봇만들기"):
         await client.send_message(message.channel, '파일 이름을 입력해주세요')
         n = await client.wait_for_message(timeout=30, author=message.author)
         n = n.content
         await client.send_message(message.channel, "유저의 말을 입력해주세요")
         a = await client.wait_for_message(timeout=30, author=message.author)
         a = a.content
         await client.send_message(message.channel, "봇의 응답을 입력해주세요")
         b = await client.wait_for_message(timeout=30, author=message.author)
         b = b.content
         await client.send_message(message.channel, "봇 토큰을 입력해주세요")
         c = await client.wait_for_message(timeout=30, author=message.author)
         c = c.content
         await client.send_message(message.channel, "플레이중 값을 입력해주세요")
         d = await client.wait_for_message(timeout=30, author=message.author)
         d = d.content
         
         
         file = open(n + ".py", "w")
         file.write("#-*-coding:cp949\n"     
                    "import discord\n\n"
                    "client = discord.Client()\n\n"
                    "@client.event\n"
                    "async def on_ready():\n"
                    "    print('login')\n"
                    "    print(client.user.name)\n"
                    "    print(client.user.id)\n"
                    "    print('--------------------')\n"
                    "    await client.change_presence(game=discord.Game(name='" + d + "', type=1))\n\n"
                    "@client.event\n"
                    "async def on_message(message):\n"
                    "    if message.content.startswith('" +a+ "'):\n"         
                    "       await client.send_message(message.channel, '" +b+ "')\n\n"
                    "client.run('" +c+ "')")
         
         file.close()
                  
         await client.send_file(message.channel, n + ".py")

         
access_token = os.environ["TOKEN"] 
client.run (access_token)
