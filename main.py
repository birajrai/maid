import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
import datetime
import logging
import discord
from discord import Activity, ActivityType, Status
from discord.ext import commands, tasks

load_dotenv()

TOKEN = os.getenv('token')
BIRTHDAYS = {
  'Biraj': {
    'month': 10,
    'day': 31
  },
  'Kritika': {
    'month': 9,
    'day': 23
  }
}
CHANNEL_ID = 1083990207143088158

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

app = Flask(__name__)

# Set log level to ERROR for werkzeug logger
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def home():
  latency = round(bot.latency * 1000)
  return f'Ping: {latency}ms'


@bot.command()
async def ping(ctx):
  latency = round(bot.latency * 1000)
  await ctx.send(f'Pong! Latency: {latency}ms | Ping: {latency}ms')


@tasks.loop(minutes=1)
async def check_birthdays():
  now = datetime.datetime.now()
  for name, bday in BIRTHDAYS.items():
    if bday['month'] == now.month and bday['day'] == now.day:
      channel = bot.get_channel(CHANNEL_ID)
      if channel is not None:
        # Get user objects for Biraj and Kritika
        user_id = 835126233455919164 if name == 'Biraj' else 814078256894050305
        user = await bot.fetch_user(user_id)

        # Send birthday message mentioning the user
        await channel.send(f"🎉 Happy birthday {name}! 🎉 {user.mention}")
      else:
        print(f"Channel with ID {CHANNEL_ID} not found.")
        break


@bot.event
async def on_ready():
  print(f'{bot.user.name} has connected to Discord!')
  await bot.change_presence(activity=Activity(name='Minecraft',
                                              type=ActivityType.playing),
                            status=Status.idle)
  check_birthdays.start()


def run():
  bot.run(TOKEN)


def keep_alive():
  server = Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8080})
  server.start()


if __name__ == '__main__':
  keep_alive()
  run()
