import discord
import random
from discord.ext  import commands
from game import game,Card
bot = commands.Bot(command_prefix='$')
TOKEN = 'NzkyODI5MDE3NTE4MTEyODM5.X-jZjw.ugwj0HPL5ipBvKU_GtAzqUoI33I'
playerlist = []
whosturn = 0 
start = False
session = False 
@bot.event
async def on_ready():
    print('Bot connected')

@bot.command(name="prefix")
async def prefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send("Set prefix to " + prefix)

currentgame = game()
@bot.command(name ='newgame')
async def on_message(ctx):
    global start 
    global session 
    if start == False:
        session = True 
        currentgame = game()
        playerlist = []
        
        playerlist.append(ctx)

@bot.command(name ='join')
async def on_message(ctx):
    global start
    if start == True:
        playerlist.append(ctx)
        return playerlist

@bot.command(name ='Startgame')
async def on_message(ctx):
    global start 
    global session
    if start == False and session == True:
        start = True
        for h in range (currentgame.playernum): 
            currentgame.dealcard(2,x)
        currentgame.getplayernum(len(playerlist) + 1)
        session = False 
@bot.command(name='test')
async def dm(ctx):
    await ctx.author.send(ctx)
    await win()

    
@bot.command(name ='stand')
async def on_message(ctx):
    global start 
    if start == True and ctx == playerlist[whosturn]:
        whosturn = whosturn + 1

@bot.command(name='draw')
async def dm(ctx):
    global start 
    if start == True:
        if  currentgame.total(whosturn) < 21: 
            currentgame.dealcard(1,whosturn)
            await ctx.author.send(currentgame.printcard(whosturn))

@bot.command(name ='Endgame')
async def on_message(ctx):
    global start 
    if start == True:
        for c in range(currentgame.playernum -1):
            if ctx == playerlist[c]:
                start = False
                ctx.send('game has stopped')

async def win():
    global start 
    if whosturn == (len(playerlist) + 1) and start == True:
        winners = currentgame.gamefin()
        for c in winners:
            await bot.say("{} has won".format(playerlist[c].message.author.mention))
    
        start = False 
        

bot.run(TOKEN)
#this starts the bot