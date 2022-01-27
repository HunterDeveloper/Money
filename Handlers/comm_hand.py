from Buttons.reply_btn import *
from db_helper import DBUser
from const import *
from Buttons.inline_btn import *

db=DBUser('Data_base.db')
def start(update, context):
    id=update.message.from_user.id
    if id==ADMIN:
        context.bot.send_message(id, "Assalomu alaykum. Quyidagi tugmalardan birini tanlang.", reply_markup=admin_btn)
        return STATE_POST
    if db.check_user(id):
        update.message.reply_text("Assalomu alaykum Hush kelibsiz. Ro'yxatdan o'tish uchun quyidagi tugmani bopsing", reply_markup=ask_phone)
        return STATE_REGISTER
    else:
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=income)
        return 1


def aftor(update, context):
     update.message.reply_text("Yaratuvchi Tursunaliuyev Humoyunmirzo")