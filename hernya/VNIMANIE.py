import discord

client = discord.Client()
client.login('the_bender@mail.ru', 'Yfgjbkbvshe,kz')

@client.event
def on_message(message):
    if message.content.lower().find('внимание'):
        quotes = message.content
        writer = message.author.name
        time = message.timestamp
        client.send_message(message.channel, '**"**`' + quotes + '`**"**\n**' + writer + '** в ' + str(time.strftime("%H:%M")) + '\n\nСПАСИБО ЗА ВНИМАНИЕ!')

@client.event
def on_ready():
    print('BOT INSTANCE IS RUNNING')

client.run()