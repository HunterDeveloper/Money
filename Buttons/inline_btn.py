from telegram import InlineKeyboardButton, InlineKeyboardMarkup
income=InlineKeyboardMarkup( [
    [ InlineKeyboardButton('💵💵💵+💵💵💵', callback_data='come'),InlineKeyboardButton('💸💸💸-💸💸💸', callback_data='gone')]
])

admin_btn=InlineKeyboardMarkup([
    [
    InlineKeyboardButton("Kunlik", callback_data='day'),
    InlineKeyboardButton("Oylik", callback_data='month')
    ],
    [
        InlineKeyboardButton("📤 Xabar jo'natish", callback_data='send_message'),
        InlineKeyboardButton("Check", callback_data='check')
    ]
])
post_btn=InlineKeyboardMarkup( [
    [InlineKeyboardButton("Ruxsat berish ✅", callback_data="allow"),
    InlineKeyboardButton("Rad etish ❌", callback_data="reject")]
])