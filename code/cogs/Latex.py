
from discord.ext import commands, tasks
import discord
import random
from latex import lat


class Latex(commands.Cog):
    def _init_(self,bot):
        super()._init_()
        self.bot = bot

    def random_color(self):
        hexa = "0123456789abcd"
        random_hex = "0x"
        for i in range(6):
            random_hex += random.choice(hexa)
        return discord.Colour(int(random_hex,16))

    def create_embed(self,title,desc,colour,image=""):
        embed = discord.Embed()
        embed.title = title
        embed.description = desc
        embed.colour = colour
        if (image !=""):
            embed.set_image(url=image)
        return embed


    @commands.command(name='lat',aliases=['l','la'])
    async def lat(self, ctx, *args):
        """Renders the latex you do not need to add the $ $ - for simple renders"""
        x = ' '.join(args)
        t = '$'+x+'$'
        color = self.random_color()
        description = 'Latex Render'
        title = t
        await lat(t)
        file = discord.File("l.png")
        img = "attachment://l.png"
        embed = self.create_embed(title,description,color,img)
        message = await ctx.send(file=file,embed = embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Latex(bot))
