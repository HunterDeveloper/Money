from const import *
from Buttons.inline_btn import *
from db_helper import DBUser
db=DBUser('Data_base.db')
def post(update, context):
    query=update.callback_query
    id=query.message.chat.id
    
    if query.data=="check":
        user=db.get_user()
        if user:
            context.bot.send_message(id,f"Name:{db.get_user_name(user)}\nPhone:{db.get_user_number(user)}", reply_markup=post_btn)
            db.set_position(id, user)
        else:
            context.bot.send_message(id,"Ruxsat so'raganlar yo'q.")
    if query.data=="allow":
        user=int(db.get_position(ADMIN))
        context.bot.send_message(user,"Ruxsat berildi. /start ni bosib foydalanishingiz mumkin")
        context.bot.send_message(id,"Ruxsat berildi.")
        db.set_position(user, "enter")
    elif query.data=='reject':
        user=int(db.get_position(ADMIN))
        db.delete_user(user)
        context.bot.send_message(id,"Rad etildi.")
        context.bot.send_message(user,"Ruxsat berilmadi.")
    
def money(update, context):
    query=update.callback_query
    id=query.message.chat.id
    btn=query.data
    if btn=='money':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=income)
    elif btn=='report':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=statistics_btn)
    elif btn=='come':
        db.set_position(id, btn)
        context.bot.send_message(id, "Qayerdan?🟢\nComment 💬")
        return STATE_MONEY
    elif btn=='gone':
        db.set_position(id, btn)
        context.bot.send_message(id, "Nima uchun?🔴\nComment 💬")
        return STATE_MONEY
    elif btn=='day':
        context.bot.send_message(id, "Kunlik xisobot.")
    elif btn=='month':
        context.bot.send_message(id, "Oylik xisobot.")