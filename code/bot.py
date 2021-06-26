from discord.ext import commands, tasks
import discord
import os


TOKEN = 'Enter-your-token-here'


def get_prefix(bot, message):
	if not isinstance(message.guild, discord.Guild):
		return 'Enter-your=prefix-here'

	return ['?', '>','!'']


bot = commands.AutoShardedBot(command_prefix=get_prefix, description='')

          
if __name__=='__main__':
	for cog in os.listdir('./cogs'):
		if cog.endswith('.py') == True:
			bot.load_extension(f'cogs.{cog[:-3]}')


@bot.event
async def on_ready():
	print(f'{bot.user.name} is online and ready!')

bot.run(TOKEN)
