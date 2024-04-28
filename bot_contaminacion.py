import discord
from discord.ext import commands
import random
import images
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')
consejos = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
    'Evita tirar botellas de plastico al mar',
]   'Evita que basura caiga el lugars para no contaminar'
]
@bot.command()
async def consejodeldia(ctx):
    consejo = random.choice(consejos)
    await ctx.send(consejo)

# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "La contaminacion es........"
    await ctx.send(definicion)

bot.run()
