from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_bot(bot, update):
    mytext = "Привет, {}!".format(update.message.chat.first_name)
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)


def chat(bot, update):
    text = update.message.text
    logging.info("Пользователь {} ввёл текст '{}'".format(update.message.chat.username, text))
    update.message.reply_text(text)


def main():
    updater = Updater(settings.TELEGRAM_API_KEY)

    updater.dispatcher.add_handler(CommandHandler("start", start_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()
