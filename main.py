import discord
import re
from rss_bot.pikabu import get_hot


client = discord.Client()
client.login('the_bender@mail.ru', 'Yfgjbkbvshe,kz')

@client.event
def on_message(message):

    if message.content.startswith('!get-pikabu-hot') and message.author.id != '129493465208848384':
        num = re.search('!get-pikabu-hot (\d+)', message.content)
        print(num.group(1))
        top = get_hot(num.group(1))
        for post in top:
            client.send_message(message.channel, "**[" + post['rating'] + "]** **`" + post['header'] + "`**\n __" + post['creation_time'] + "__\n```" + post['link'] + "```\n\n")

    if message.content.lower().find('внимание') != -1 and message.author.id != '129493465208848384':
        quotes = message.content
        writer = message.author.name
        time = message.timestamp
        client.send_message(message.channel, '**"**`' + quotes + '`**"**\n**' + writer + '** в ' + str(time.strftime("%H:%M")) + '\n\nСПАСИБО ЗА ВНИМАНИЕ!')

    if message.content.startswith('братишка') and message.author.id != '129493465208848384':
        client.send_message(message.channel, 'Я вам покушать принес!')

    if message.content.lower().find('ублюдок') != -1 and message.author.id != '129493465208848384':
        client.send_message(message.channel, 'Покидьок, твою мать, ану йди сюди, лайно собаче, вирішив до мене лізти? Ти,'
                                             ' засранець смердючий, матір твою, га? Ну йди сюди, спробуй мене трахнути, '
                                             'я тебе сам трахну покидьок, онаніст дідьків, будь ти проклятий, йди ідіот, '
                                             'трахати тебе й усю твою родину, лайно собаче, жлоб смердючий, лайно, сука, '
                                             'падла, йди сюди, мерзотник, негідник, гад, йди сюди ти - лайно, ДУПА!')

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')
    members = client.get_all_members()
    for member in members:
        print(member.name + ' : ' + member.id)


client.run()
