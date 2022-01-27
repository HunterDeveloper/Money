from telegram import ReplyKeyboardMarkup, KeyboardButton
ask_phone=ReplyKeyboardMarkup([ 
    [KeyboardButton("📱 Telefon raqamni jo'natish", request_contact=True)]
], resize_keyboard=True)