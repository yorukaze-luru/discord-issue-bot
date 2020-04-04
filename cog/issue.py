from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime

great_owner_id = 459936557432963103

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
        embed = discord.Embed(title=f"{self.bot.user}", description="このBotの情報です")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="SERVERの数", value=f'`{len(self.bot.guilds)}`',inline=False)
        embed.add_field(name="USERの数", value=f'`{len(set(self.bot.get_all_members()))}`',inline=False)
        embed.add_field(name="言語", value='`discord.py`\n`discord.js`',inline=False)
        embed.add_field(name="Ping値", value=f'`{self.bot.ws.latency * 1000:.0f}ms`',inline=False)
        embed.add_field(name="各種リンク", value="[このBOTの公式開発鯖](<https://discord.gg/ENxnsJM>)", inline=False)
        await ctx.channel.send(embed=embed)
            
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
        
    # メインとなるroleコマンド
    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['ad'])
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send('付与しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーから指定した役職を剥奪する。
    @role.command(aliases=['rm'])
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send('剥奪しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['cr'])
    async def create(self, ctx, what):
        guild = ctx.guild
        set_name2 = f"{what}"
        await guild.create_role(name=set_name2)
        await ctx.send(f'作成しました。@' + set_name2)
        
    @commands.Cog.listener()
    @commands.has_permissions(manage_guild=True)
    async def on_message(self, message):
        if message.author.bot:
            return
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
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
