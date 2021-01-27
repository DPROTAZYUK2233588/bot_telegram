import json
import requests
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = '1528620417:AAGk76spvzoNwiwXTnTFG-1apEsc47fXi2M'

def start(update, context):
	update.message.reply_text('Hi!')


def help(update, context):	
	update.message.reply_text('Help!')


def echo(update, context):
	update.message.reply_text(update.message.text)



def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)


def echo(update, context):
	update.message.reply_text(update.message.text)



def main():
	updater = Updater(TOKEN, use_context=True)	
	dp = updater.dispatcher	
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(MessageHandler(Filters.text, echo))
	dp.add_error_handler(error)
	updater.start_webhook(listen="0.0.0.0",	
	port=int(PORT),	
	url_path=TOKEN)
	
	updater.bot.setWebhook('https://https://ekaterinanovozheeva.herokuapp.com/' + TOKEN)
	
	updater.idle()

if __name__ == '__main__':
    main()
