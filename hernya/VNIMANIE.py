import discord

client = discord.Client()
client.login('the_bender@mail.ru', 'Yfgjbkbvshe,kz')

@client.event
def on_message(message):
    words = message.content.lower().split()
    for word in words:
        if word.startswith('внимание') and message.author.id != '129493465208848384':
            quotes = message.content
            writer = message.author.name
            time = message.timestamp
            client.send_message(message.channel, '**"**`' + quotes + '`**"**\n**' + writer + '** в ' + str(time.strftime("%H:%M")) + '\n\nСПАСИБО ЗА ВНИМАНИЕ!')
            break
@client.event
def on_ready():
    print('BOT INSTANCE IS RUNNING')

client.run()