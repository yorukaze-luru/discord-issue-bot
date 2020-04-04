from discord.ext import commands, tasks # Bot Commands Frameworkをインポート
import traceback # エラー表示のためにインポート
import os
import discord

TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cog.issue'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class MyBot(commands.Bot):

    # MyBotのコンストラクタ。
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print(self.user.name)  # ボットの名前
        print(self.user.id)  # ボットのID
        print(discord.__version__)  # discord.pyのバージョン
        print('----------------')
        print('いしゅー')
        channel = self.get_channel(674180325890457610)
        await channel.send(self.user.name)  # ボットの名前
        await channel.send(self.user.id)  # ボットのID
        await channel.send(discord.__version__)  # discord.pyのバージョン
        await channel.send('----------------')
        await channel.send('いしゅー')
        await self.change_presence(activity=discord.Game(name=f'ヘルプ|is!help')) 

#MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    bot = MyBot(command_prefix='is!') # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(TOKEN) # Botのトークン
