from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler,MessageHandler,Filters

from apps.telegrambot.hendlers import commands, common

BOT_TOKEN = "7019583410:AAHZSGHUC44-XDaNFnzM48qj1PAdvX0EjYE"
bot = Bot(token=BOT_TOKEN)

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler(command="start", callback=commands.start))
dispatcher.add_handler(CommandHandler(command="help", callback=commands.help ))
dispatcher.add_handler(MessageHandler(Filters.all, common.echo))


