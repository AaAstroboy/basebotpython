# Isso é a base de um BOT python que eu fiz, não tem nada, mas ele vai funcionar.
# Quer criar seu bot personalizado ? me procure no Discord: https://discord.gg/minacci
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

TOKEN = 'TOKEN' # Mude o 'TOKEN' e coloque o token do seu bot
bot = commands.Bot(command_prefix='PREFIXO DO BOT', intents=intents)
                
@bot.event
async def on_ready():
    print(f'{bot.user.name} Está operando!')
    
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
    

bot.remove_command('help')
bot.run(TOKEN)
