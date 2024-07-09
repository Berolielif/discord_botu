import discord
import random
from bot_logic import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$naber'):
        await message.channel.send("İyi senden naber?")
    elif message.content.startswith('$şifrem'):
        await message.channel.send(f"Şifreniz: {gen_pass(10)}")
    elif message.content.startswith('emoji'):
        await message.channel.send(f"emojiniz: {emoji_olusturucu()}")









client.run("token")

