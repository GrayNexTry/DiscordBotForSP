import discord
import configparser
import sqlite3

bot = discord.Bot()
con = sqlite3.connect('ShopData')
cur = con.cursor()

def main():

    @bot.slash_command
    async def

    bot.run(pars('token'))

def pars(arg: str):
    try:
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        result = parser["Discord"][arg]
        return result
    except NameError:
        return 0


if __name__ == '__main__':
    main()
