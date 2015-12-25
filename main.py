import discord

client = discord.Client()
client.login('the_bender@mail.ru', 'Yfgjbkbvshe,kz')

@client.event
def on_message(message):
    print(message.content)
    print(message.author.name)
    print(message.author.id)
    if message.content.startswith('братишка'):
        client.send_message(message.channel, 'Я вам покушать принес!')
    if (message.author.id == '128768252921774080' or message.author.id == '128780999134806016' or message.author.id == '128775115075747840') and message.content.startswith('ублюдок'):
        client.send_message(message.channel, 'Покидьок, твою мать, ану йди сюди, лайно собаче, вирішив до мене лізти? Ти, засранець смердючий, матір твою, га? Ну йди сюди, спробуй мене трахнути, я тебе сам трахну покидьок, онаніст дідьків, будь ти проклятий, йди ідіот, трахати тебе й усю твою родину, лайно собаче, жлоб смердючий, лайно, сука, падла, йди сюди, мерзотник, негідник, гад, йди сюди ти - лайно, ДУПА!')

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')
    members = client.get_all_members()
    for member in members:
        print(member.name + ' : ' + member.id)


client.run()
