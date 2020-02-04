import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

GLOBAL_CH_NAME = "issue-global"

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_message(message):
    
    if message.author.bot:
        # もし、送信者がbotなら無視する
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

        # embed式
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # global_channelsは hoge-global の名前を持つチャンネルのリスト

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
