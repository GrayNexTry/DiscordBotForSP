import discord
import configparser
import sqlite3

bot = discord.Bot()


def main():
    bot.run(pars('token'))
    bd = sqlite3.connect('SPData.db')

def pars(arg: str):
    try:
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        result = parser["Discord"][arg]
        return result
    except:
        return 0


if __name__ == '__main__':
    main()
