from discord import *
import discord
import configparser
import sqlite3

con = sqlite3.connect('ShopData')
cur = con.cursor()

def main():
    bot = discord.Bot(guilds_id=pars('guilds_id'))

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
