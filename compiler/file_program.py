
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is ready! yay')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def ban(ctx, member: discord.Member, *, reason):
    if ctx.message.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
        
    else:
        await ctx.send('You do not have permission to ban members!')
    


@bot.command()
async def kick(ctx, member: discord.Member, *, reason):
    if ctx.message.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')
    
    else:
        await ctx.send('You do not have permission to kick members!')
    
        

@bot.command()
async def clear(ctx, amount=5):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount)
        
    else:
        await ctx.send('You do not have permission to clear messages!')
        


@bot.command()
async def timeout(ctx, member: discord.Member, duration, *, reason):
    if ctx.message.author.guild_permissions.moderate_members:
        await member.timeout(duration, reason=reason)
        await ctx.send(f'Timed out {member.mention}')
    
    else:
        await ctx.send('You do not have permission to timeout members!')
        


@bot.command()
async def untimeout(ctx, member: discord.Member):
    if ctx.message.author.guild_permissions.moderate_members:
        await member.untimeout()
        await ctx.send(f'Untimed out {member.mention}')
    
    else:
        await ctx.send('You do not have permission to untimeout members!')
    
        

@bot.command()
async def kill(ctx):
    if (ctx.author.id == 1118732605165146144):
        await ctx.send("fellas, ima commit die")
        quit()
    else:
      await ctx.send("you cant kill me :3 ")    

#Bot toke

bot.run('MTE5NDgzMDA5NjM1NjM1NjE5Ng.Gl82Jq.jKsZTXdkiZTVuFvjSXwFx3CRTFeTnZPMhfitaQ')