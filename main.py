from telegram.ext import Updater, ConversationHandler, CommandHandler,CallbackQueryHandler, MessageHandler, Filters
from telegram import BotCommand


from const import *

from Handlers.comm_hand import *
from Handlers.message_hand import *
from Handlers.query_hand import *
def main():
    updater = Updater(TOKEN)
    dispacher= updater.dispatcher
    dispacher.bot.set_my_commands([
        BotCommand('start', 'Foydalanishni boshlash')
    ])
    conv_hand=ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_REGISTER: [
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                MessageHandler(Filters.contact, phone_contact)
            ],
            STATE_POST: [
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                CallbackQueryHandler(post)
            ],
            STATE_MONEY: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                CallbackQueryHandler(money),
                MessageHandler(Filters.text, take_comment)
            ], 
            STATE_SUMA: [ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                CommandHandler('hammasini_uchir', clear),
                CallbackQueryHandler(money),
                MessageHandler(Filters.text, take_money)

            ],
            STATE_REPORT:[ 
                CommandHandler('start', start),
                CommandHandler('aftor', aftor),
                CallbackQueryHandler(report)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispacher.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()
main()