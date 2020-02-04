import discord
import os
import asyncio
from datetime import datetime

TOKEN = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID = 674180325890457610
GLOBAL_CH_NAME = "issue-global"

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('----------------')
    print('Hello World,issue_bot started.')
    channel = client.get_channel(CHANNEL_ID)
    await channel.purge()
    await channel.send(f'名前:{client.user.name}')  # ボットの名前
    await channel.send(f'ID:{client.user.id}')  # ボットのID
    await channel.send(f'Discord ver:{discord.__version__}')  # discord.pyのバージョン
    await channel.send('----------------')
    await channel.send('状態：安定') 
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='ヘルプ|**is!help**'))
    

@client.event
async def on_message(message):
    
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return

    if message.content == "is!help":
        embed = discord.Embed(title="Issue bot ヘルプ",description="'い' or 'し' or 'ゅ' or 'ー' or 'いしゅー'で反応するよ",color=#00BB00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/663113701859131410/674175699367755796/BOT.png")
        embed.add_field(name="a",value="b",inline=False)
        await channel.send(embed=embed)

    if message.content == 'い' or 'し' or 'ゅ' or 'ー' or 'いしゅー': 
        await message.channel.send('この後｢いしゅー｣が50回スパムされます。\n覚悟があるなら、｢y｣と発言してください。') 
        def  issuespam(m):
            return m.content == "y" and m.author == message.author
        try:
            reply = await client.wait_for( "message" , check = issuespam , timeout = 60 )
        except asyncio.TimeoutError:
            await message.channel.send( "中止します。" )
            return
        else:
            if not reply.content == "y":
                await message.channel.send( "中止します。" )
                return
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            await message.channel.send( "いしゅー" )
            return
        

#-----------グローバルチャット-----------
    if message.channel.name == GLOBAL_CH_NAME:
        # issue-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        if 'discord.gg' in message.content:
            await message.channel.send("ここで招待は送れません。")
            return # 招待は送れません

        channels = client.get_all_channels()
        # channelsはbotの取得できるチャンネルのイテレーター
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # global_channelsは issue-global の名前を持つチャンネルのリスト

        embed = discord.Embed(title="issue-global",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
#-----------グローバルチャット-----------

client.run(TOKEN)
