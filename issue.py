import discord
import os
import asyncio
from datetime import datetime

TOKEN = os.environ['DISCORD_BOT_TOKEN']

GLOBAL_CH_NAME = "issue-global"
ISS_SRART = "issue-start"

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('----------------')
    print('Hello World,issue_bot started.')
    channel = client.get_channel(674180325890457610)
    date = datetime.now()
    await channel.send(f'>>> **再起動情報** \n 名前:{client.user.name} \n ID:{client.user.id} \n Discord ver:{discord.__version__} \n ------------------------------- \n 状態：いしゅー \n \n 再起動時間：{date.year}年{date.month}月{date.day}日{date.hour}時{date.minute}分{date.second}秒')  # ボットの名前    
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='ヘルプ| is!help'))

@client.event
async def on_message(message):
    
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return

    if message.content == "is!help":
        embed = discord.Embed(title="Issue bot ヘルプ",description="｢い｣｢し｣｢ゅ｣｢ー｣｢いしゅー｣で反応するよ。\n発言すると覚悟の有無を聞かれるけれど、｢y｣と発言すれば開始するよ。",color=0x2ecc71)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/670982490999226370/674193654344056842/Screenmemo_2020-02-04-18-00-12.png")
        embed.add_field(name="**issue-global**",value="上記の名前でチャンネルを作ると自動でグローバルチャットに接続されます。",inline=False)
        embed.add_field(name="**各種リンク**", value="[BOT招待URL](<https://discordapp.com/api/oauth2/authorize?client_id=674176006801850369&permissions=1812987088&scope=bot>)", inline=False)  
        await message.channel.send(embed=embed)

    if message.content == 'テスト':
        if message.channel.name == GLOBAL_CH_NAME or message.channel.name == ISS_SRART:
            await message.channel.send('ここでは使うことが出来ません。')
            return
        issue_test = 0
        while issue_test < 25:
            embed = discord.Embed(title=" ",description=" ")
            embed.set_image(url="https://cdn.discordapp.com/attachments/674223403313659934/674581603540008970/9QfQXW91k2wAAAAASUVORK5CYII.png")
            await message.channel.send(embed=embed)
            issue_test = issue_test + 1

    if message.content == 'い' or message.content == 'し' or message.content == 'ゅ' or message.content == 'ー' or message.content == 'いしゅー': 
        if message.channel.name == GLOBAL_CH_NAME or message.channel.name == ISS_SRART:
            await message.channel.send('ここでは使うことが出来ません。')
            return
        await message.channel.send('この後｢いしゅー｣が50回スパムされます。\n覚悟があるなら、｢y｣と発言してください。\n何も発言しない(10秒待機)すると停止します。') 
        def  issuespam(m):
            return m.content == "y" and m.author == message.author
        try:
            reply = await client.wait_for( "message" , check = issuespam , timeout = 10.0 )
        except asyncio.TimeoutError:
            await message.channel.send( "中止します。" )
            return
        else:
            if not reply.content == "y":
                await message.channel.send( "中止します。" )
                return
            elif reply.content == "y":
                issue_counter =0
                while issue_counter < 51:
                    await message.channel.send( "いしゅー" )
                    issue_counter = issue_counter + 1
              
client.run(TOKEN)
