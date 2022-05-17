import os # for importing env vars for the bot to use
from twitchio.ext import commands

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")

if __name__ == "__main__":
    print("BOT NICK:", os.environ['BOT_NICK'],)
    bot.run()

# This is a test to see if !bald will work
@bot.command(name='bald')
    async def bald(ctx):
        await ctx.send('Wayn is bald!')


# This is a !bad test to see if the command will work
@bot.command(name='bad')
    async def bad(ctx):
        await ctx.send('Wayn is bad at Apex and Val')
