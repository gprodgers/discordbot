import discord
from discord.ext import commands
import random
from random import randint
from numpy import sin, cos, mean
import datetime
import youtube_dl
"""
Hello Jeff this Miguel's and Graham's awoo discord bot. The awoo bot can do alot of fun minigames and even play music! 
"""

prefix = '!' 
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

#this changes the prefix for the command

@bot.command()
async def newprefix(ctx, newpre):
    prefix = str(newpre)
    await ctx.send(f"My new prefix is {newpre}")

#this returns awooo ten times
    
@bot.command()
async def awoo(ctx):
    awoo = await ctx.send("AWOOOOOOOOO Awoooo " * 10)
    await awoo.delete(delay=60)

#ummmmm..... dont look at this
    
@bot.command()
async def jeff(ctx):
    jeff = await ctx.send("Please give us a good grade!!!")
    await jeff.delete(delay=60)

#This is a fun simp calculator
    
@bot.command()
async def simp(ctx, calc):
    simp_level = random.randint(0, 100)
    if simp_level < 11:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. You're probably an incel, sorry.")
    elif simp_level > 11 and simp_level < 19:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Do you hate women or something?")
    elif simp_level > 19 and simp_level < 29:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Great placement.")
    elif simp_level > 29 and simp_level < 39:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Resisting temptation well, good job.")
    elif simp_level > 39 and simp_level < 49:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. You're alright, for now.")
    elif simp_level == 50:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Perfectly balanced.")
    elif simp_level > 50 and simp_level < 59:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Pretty average, nothing to feel bad about.")
    elif simp_level > 59 and simp_level < 69:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Baby simp.")
    elif simp_level == 69:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Nice.")
    elif simp_level > 69 and simp_level < 79:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. Delete TikTok, please.")
    elif simp_level > 79 and simp_level < 89:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. How many times do you tweet at neekolul per day?")
    elif simp_level > 89:
        await ctx.send(f"{calc} your simp level is ... {simp_level}. SIMP SIMP SIMP SIMP SIMP SIMP.")

#its a custom dice
        
@bot.command()
async def roll(ctx, num):
    random_num = random.randint(0, int(num))
    await ctx.send(f"The number you rolled was a ... {random_num}")

#rates attractiveness 
    
@bot.command()
async def rate(ctx, *args):
    rate_num = random.randint(0, 10)
    await ctx.send(f"{ctx.message.mentions[0]} you are a {rate_num} out of 10")
    if rate_num == 1:
        await ctx.send("Im so sorry")
    elif rate_num == 2:
        await ctx.send("Yikes dawg that sucks")
    elif rate_num == 3:
        await ctx.send("WOWIE THATS LOW")
    elif rate_num == 4:
        await ctx.send("Below average...")
    elif rate_num == 5:
        await ctx.send("Just average nothing else, bland like white bread")
    elif rate_num == 6:
        await ctx.send("Slighty above average champ, nice work")
    elif rate_num == 7:
        await ctx.send("7 eh? not bad, not bad at all")
    elif rate_num == 8:
        await ctx.send("WOoah Woaha WOah we got a cutie over here")
    elif rate_num == 9:
        await ctx.send("Damn you look so fine, can I date you? jk im a bot... unless")
    elif rate_num == 10:
        await ctx.send("Actually perfect wtf, how do people like you exist?")

#Gives a bar of an amazing song
        
@bot.command()
async def codezone(ctx):
    codezone_line = random.randint(0, 38)
    codelist = ["Only code with anime girls", "Quivering GASP, double jointed python", "Fresh functions, elegant enumeration", "First the commit, then the push", "My terminal is in love with code", "Co-op code edits", "Stuff my code into a script", "Write my code well", "Pressure code my programming projects", "Code blast me and make it snappy", "Code, code, code, code, code, code, code, code", "What's all the codemotion?", "My dad fell into a code shaft", "My dad made my face with code", "Initialize an instance with code", "Code funcs in my trunk", "Code craving toddler", "Code drippin' coder", "Codey Rae Jepsen", "Code my maybe", "Night of the living code", "Nefarious code mastermind", "Code makes me fearless", "Code crammer, code slammer", "Code slammed ya mum", "Mail your mum pieces of my code", "Bazinga!", "Chug the code, code ya mum", "Code my terminal full of code", "Three little words: write code, nerd", "Code stuffer, error debugger", "Write my code puddle", "Would love a GitHub for my code", "Undercoded baby git repos", "Help my dogs get lots of code", "Elkner class full of my code", "Who wrote all my code? A mystery", "Code detective hot on the trail", "Bees make honey, my code runny"]
    await ctx.send(codelist[codezone_line])

#Tells you when you will die

@bot.command()
async def deathdate(ctx, *args):
    day =  random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(2021, 2100)
    await ctx.send(f"{ctx.message.mentions[0]} you are going to die on {month}/{day}/{year}")

#Tells you when you will die
    
@bot.command()
async def marriageage(ctx, *args):
    age = random.randint(0, 77)
    if age == 0:
        await ctx.send(f"ctx.message.mentions[0] uhmmm... im sorry but never") 
    else:
        await ctx.send(f"{ctx.message.mentions[0]} is going to get married or already has at the age of {age}")
        if age == 69:
            ctx.send(f"nice")

#Animated gif of how much two arguements hate each other
            
@bot.command()
async def hatecalc(ctx, name1, name2):
    age = random.randint(0,10)
    if age == 0:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/698956220324905020/0.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** dont hate each other at all, hell I'd go as far to say they're friends")

    if age == 1:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/698956217975963648/10.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** hate each other very little")

    if age == 2:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/698956213588852776/20.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** hate each other a bit")

    if age == 3:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/698941014903357540/30.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** hate each other like siblings")

    if age == 4:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/698966791988445364/40.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** kinda hate each other")

    if age == 5:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/698961315657678878/50.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** hate each other")

    if age == 6:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/698976522819731508/60.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** hate each other more than they should")

    if age == 7:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/699006477805027328/70.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** really hate each other")

    if age == 8:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/699025736690040913/80.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** absolutely hate each other guts")

    if age == 9:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/699041286472073366/90.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** hate each other so much it scary")
 
    if age == 10:
        ten = discord.Embed(title='**HATE -O- METER CALCULATOR SAYS:**',color=0xff0000)
        ten.set_image(url='https://cdn.discordapp.com/attachments/643563629504888834/699058343758790779/100.gif')
        await ctx.send(embed=ten) 
        await ctx.send(f"**{name1}** and **{name2}** hate for each other is so ungodly emense it supasses anyones capabiity of understandment")

 #tells you how to use every command
        
@bot.command(aliases=['h'])
async def help(ctx):
    des = "**!awoo:** gives an AWOOOooing suprise \n **!jeff:** a plead \n **!simp @user:** Gives the users simp level \n **!codezone:** Gives a line of the best song \n **!deathdate @user:** Tells the user when they will die \n **!laidage @user:** Tells the user what age they will/have got laid \n **!hatecalc @user1 @user2:** Calculates how much they hate eachother"
    msg = discord.Embed(title='Commands List',description=des,color=0xffffff)
    await ctx.author.send(embed=msg)
 
#Still not finished but eventionally will be a love fighting mini game
    
@bot.command()
async def lovefight(ctx, *args):
    await ctx.send(f"**{ctx.message.mentions[0]}** you have been challenged by **{ctx.message.author}** do you accept?")    
#here is themusic bot part
players = {}
queues = {}

def checkqueue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] - player
        player.start()
 
# the bot's join command
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
 
# the bot's leave command
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
 
# the bot's command to play music
@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    audio = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

# the command used to pause music
@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

# the command used to stop music
@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

# the command used to resume songs
@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
 
# the command used to queue songs
@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
   
    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say(‘Video added to the queue.’)



bot.run('Njk3NTY3MDAyMzMxNTc4NDAx.Xo975g.UVFhMAXhdFwsYaegilYVaj5dWWQ')
