from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime

great_owner_id = 459936557432963103
GLOBAL_CH_NAME = "issue-global"
ISS_SRART = "issue-start"

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    async def say(self, ctx, what):
        await ctx.send(f'{what}')

    @commands.command(aliases=['sinfo'])
    async def serverinfo(self, ctx, server_id: int=None):
        if server_id == None:
            embed = discord.Embed(title="鯖ステータス",description=f"Ping:`{self.bot.ws.latency * 1000:.0f}ms`")
            embed.add_field(name="サーバー名",value=f'`{ctx.guild.name}`')
            embed.add_field(name="現オーナー名",value=f'`{ctx.guild.owner}`')
            guild = ctx.guild
            member_count = sum(1 for member in guild.members if not member.bot) 
            bot_count = sum(1 for member in guild.members if member.bot) 
            all_count = (member_count) + (bot_count)
            embed.add_field(name="総人数",value=f'`{all_count}`',inline=False)
            embed.add_field(name="ユーザ数",value=f'`{member_count}`',inline=False)
            embed.add_field(name="BOT数",value=f'`{bot_count}`',inline=False)
            embed.add_field(name="テキストチャンネル数",value=f'`{len(ctx.guild.text_channels)}`',inline=False)
            embed.add_field(name="ボイスチャンネル数",value=f'`{len(ctx.guild.voice_channels)}`',inline=False)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)
            return
        server = self.bot.get_guild(server_id)
        embed = discord.Embed(title="鯖ステータス",description=f"Ping:`{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="サーバー名",value=f'`{server.name}`')
        embed.add_field(name="現オーナー名",value=f'`{server.owner}`')
        guild = server
        member_count = sum(1 for member in guild.members if not member.bot) 
        bot_count = sum(1 for member in guild.members if member.bot) 
        all_count = (member_count) + (bot_count)
        embed.add_field(name="総人数",value=f'`{all_count}`',inline=False)
        embed.add_field(name="ユーザ数",value=f'`{member_count}`',inline=False)
        embed.add_field(name="BOT数",value=f'`{bot_count}`',inline=False)
        embed.add_field(name="テキストチャンネル数",value=f'`{len(server.text_channels)}`',inline=False)
        embed.add_field(name="ボイスチャンネル数",value=f'`{len(server.voice_channels)}`',inline=False)
        embed.set_thumbnail(url=server.icon_url)
        await ctx.channel.send(embed=embed)

    @commands.group(aliases=['h'])
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            issuep = discord.Embed(title="Issue bot ヘルプ",description="その他ヘルプは`help 各ヘルプコマンド`",color=0x2ecc71)
            issuep.set_thumbnail(url="https://cdn.discordapp.com/attachments/670982490999226370/674193654344056842/Screenmemo_2020-02-04-18-00-12.png")
            issuep.add_field(name="**command prefix**",value="`is!`")
            issuep.add_field(name="**Global Chat**",value="`globalchat (省略はgc)`")
            issuep.add_field(name="**いしゅースパム**",value="`issue (省略はis)`")
            issuep.add_field(name="**各種リンク**", value="[BOT招待URL](<https://discordapp.com/api/oauth2/authorize?client_id=674176006801850369&permissions=1812987088&scope=bot>)", inline=False)  
            await ctx.channel.send(embed=issuep)
            embed = discord.Embed(title=f"{self.bot.user}", description="このBotの情報です",color=0x2ecc71)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(name="SERVERの数", value=f'`{len(self.bot.guilds)}`',inline=False)
            embed.add_field(name="USERの数", value=f'`{len(set(self.bot.get_all_members()))}`',inline=False)
            embed.add_field(name="言語", value='`discord.py`\n`discord.js`',inline=False)
            embed.add_field(name="Ping値", value=f'`{self.bot.ws.latency * 1000:.0f}ms`',inline=False)
            await ctx.channel.send(embed=embed)

    @help.command(aliases=['gc'])
    async def globalchat(self, ctx):
        embed = discord.Embed(title=f"help globalchat", description="Global Chatについてのヘルプです。",color=0x2ecc71)
        embed.add_field(name="**issue-global**", value=f'上記の名前でチャンネルを作ると自動でグローバルチャットに接続されます。',inline=False)
        await ctx.channel.send(embed=embed)

    @help.command(aliases=['is'])
    async def issue(self, ctx):
        embed = discord.Embed(title=f"help issue", description="いしゅースパムについてのヘルプです。",color=0x2ecc71)
        embed.add_field(name="**説明**", value=f'開始コマンドを入力。\n開始するかどうか聞かれるので、｢y｣を入力。\nそうすれば開始されます。\n⚠️｢issue-start｣や｢issue-global｣では使えません')
        embed.add_field(name="**開始コマンド**", value=f'｢い｣｢し｣｢ゅ｣｢ー｣｢いしゅー｣のうちどれか一つ')
        await ctx.channel.send(embed=embed)

    @help.group(aliases=['gl'])
    async def guild_list(self, ctx):
        guildlist = discord.Embed(title=f"Guild List", description="導入鯖名簿です",color=0x2ecc71)
        for g in self.bot.guilds:
            guildlist.add_field(name=f"**{g}**", value=f'{g.id}')
        await ctx.channel.send(embed=guildlist)

    @guild_list.command(aliases=['gll'])
    async def global_list(self, ctx):
        guildlist = discord.Embed(title=f"Guild List", description="導入鯖名簿です",color=0x2ecc71)
        g for g in self.bot.guilds if discord.utils.get(g.channels.name="issue-global"):
            guildlist.add_field(name=f"**{g}**", value=f'{g.id}')
        await ctx.channel.send(embed=guildlist)

    #gbans a user with a reason
    @commands.command()
    async def gban(self, ctx, user_id: int=None, reason =None):
        if ctx.author.id != great_owner_id:
            return
        if reason == None:
            reason = "None"
        for g in self.bot.guilds:
            guildf = self.bot.get_guild(g.id)
            await guildf.ban(discord.Object(user_id), reason=reason)
            await ctx.channel.send(f"{g}からのBANが完了しました。")
            if g == None:
                await self.bot.logout()

    #gunbans a user with a reason
    @commands.command()
    async def gunban(self, ctx, user_id: int=None, reason =None):
        if ctx.author.id != great_owner_id:
            return
        if reason == None:
            reason = "None"
        for g in self.bot.guilds:
            guildf = self.bot.get_guild(g.id)
            await guildf.unban(discord.Object(user_id), reason=reason)
            await ctx.channel.send(f"{g}からのUNBANが完了しました。")
            if g == None:
                await self.bot.logout()

    @commands.Cog.listener()
    @commands.has_permissions(manage_guild=True)
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content == 'pissue':
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

        if message.author.id != great_owner_id:
            return
        if message.content == 'ログ削除して':
            await message.channel.purge()
            msg = await message.channel.send("削除しました。")
            await asyncio.sleep(15)
            await msg.delete()
        if message.content == '再起動して':
            await self.bot.logout()

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot))
