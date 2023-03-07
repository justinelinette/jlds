import discord
from sleep_spell import calc_results
from enemy import Enemy

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    # define function to check for message author and channel
    def check(m):
        return m.author == message.author and m.channel == message.channel

    # check if message starts with $leep
    if message.content.startswith('$leep'):

        # collect user inputs one by one
        await message.channel.send("enter sleep damage:")
        sleep_dmg = await client.wait_for('message', check=check)
        sleep_dmg = int(sleep_dmg.content)
        await message.channel.send("enter number of enemies between 1 and 30:")
        num_enemies = await client.wait_for('message', check=check)
        num_enemies = int(num_enemies.content)

        # create empty enemy_hps list, receive input, split user input and append to enemy_hps list
        enemy_hps = []
        await message.channel.send(f"enter enemy hps separated by commas (ie. '10, 20, 30' ):")
        user_hp_input = await client.wait_for('message', check=check)
        split_hps = user_hp_input.content.split(',')
        for split_hp in split_hps:
            enemy_hps.append(split_hp)

        # create list of enemy objects based on input vals
        enemies = []
        for i, enemy_hp in enumerate(enemy_hps):
            name = f"enemy {i+1}"
            hp = int(enemy_hp)
            enemy = Enemy(name, hp)
            enemies.append(enemy)
        enemies.sort(key=lambda x: x.hp, reverse=True)

        # calculate results and send response in the "general" channel
        response_channel = discord.utils.get(
            message.guild.channels, name="general")
        results = calc_results(enemies, sleep_dmg)
        if results:
            for result in results:
                if " is asleep." in result:
                    await response_channel.send("\u2022  :zzz:  " + result + "\n")
                else:
                    await response_channel.send("\u2022  :alarm_clock:  " + result + "\n")
        else:
            await response_channel.send("justine fucked something up, sorry")


client.run(
    'MTA4MjY2NTExMTUwNTg4MzE0Ng.GxQ411.-k_p4nSniT--zZFu2gECyr8M9EJRfjwHxNc9u4')
