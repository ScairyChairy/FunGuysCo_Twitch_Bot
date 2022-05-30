import os # for importing env vars for the bot to use
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['ACCESS_TOKEN'], prefix='!', initial_channels=['drjuicyplays'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send(f'Ban me. I am testing a bot :)')
    
    @commands.command(name='bald')
    async def bald(self, ctx: commands.Context):
        await ctx.send('Wayn is bald!')


    @commands.command(name='bad')
    async def bad(self, ctx: commands.Context):
        await ctx.send('Wayn is bad at Apex and Val')

    @commands.command(name='wayn')
    async def wayn(self, ctx: commands.Context):
        await ctx.send('Wayn is ugly')

    @commands.command(name='best')
    async def best(self, ctx: commands.Context):
        await ctx.send('Chair is best')

if __name__ == "__main__":
    bot = Bot()
    bot.run()
