from telegram import InlineKeyboardButton, InlineKeyboardMarkup
income=InlineKeyboardMarkup( [
    [ InlineKeyboardButton('💵💵💵➕💵💵💵', callback_data='come'),InlineKeyboardButton('💸💸💸➖💸💸💸', callback_data='gone')],
    [InlineKeyboardButton("⬅️Orqaga", callback_data='main_menu')]
])

type_income=InlineKeyboardMarkup( [
    [ InlineKeyboardButton('Terminal 💳', callback_data='terminal'),InlineKeyboardButton('Cash 💰', callback_data='cash')],
    [InlineKeyboardButton("CliCK 🌐", callback_data='click')],
    [InlineKeyboardButton("⬅️Orqaga", callback_data='main_menu')]
])

type_outlay=InlineKeyboardMarkup( [
    [InlineKeyboardButton("ACADEMY 🏢", callback_data='academy')],
    [InlineKeyboardButton("Shaxsiy 🤵🏻‍♂️", callback_data='personal')]
])
type_outlay_report=InlineKeyboardMarkup( [
    [InlineKeyboardButton("ACADEMY 🏢", callback_data='academy')],
    [InlineKeyboardButton("Shaxsiy 🤵🏻‍♂️", callback_data='personal')],
    [InlineKeyboardButton("Umumiy 📜", callback_data='overall')]
])

admin_btn=InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Kunlik 🗓", callback_data='day'),
        InlineKeyboardButton("Oylik 📅", callback_data='month')
    ],
    [
        InlineKeyboardButton("📤 Xabar jo'natish", callback_data='send_message'),
        InlineKeyboardButton("Check", callback_data='check')
    ],
    [
        InlineKeyboardButton("Pul 💶", callback_data="money"),
        InlineKeyboardButton("Hisobot 📈", callback_data="report")
    ]
])
post_btn=InlineKeyboardMarkup( [
    [InlineKeyboardButton("Ruxsat berish ✅", callback_data="allow"),
    InlineKeyboardButton("Rad etish ❌", callback_data="reject")]
])

main_btn=InlineKeyboardMarkup( [
    [InlineKeyboardButton("Pul 💶", callback_data="money"),
    InlineKeyboardButton("Hisobot 📈", callback_data="report")]
])
statistics_btn=InlineKeyboardMarkup( [
    [
    InlineKeyboardButton("Kunlik 🗓", callback_data='day'),
    InlineKeyboardButton("Oylik 📅", callback_data='month')
    ],
    [
    InlineKeyboardButton("Daromad 😊", callback_data='income'),
    InlineKeyboardButton("Xarajat 😒", callback_data='expense'),
    InlineKeyboardButton("Foyda 😋", callback_data='benefit')
    ],
    [InlineKeyboardButton("⬅️Orqaga", callback_data='main_menu')]
])
prev=InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️Orqaga", callback_data='report')]
    ])
back=InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️Orqaga", callback_data='money')]
    ])
