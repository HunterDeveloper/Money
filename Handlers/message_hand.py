from unicodedata import name
from const import *
from db_helper import DBUser
from Buttons.inline_btn import *
from telegram import ReplyKeyboardRemove
import time
db=DBUser('Data_base.db')

def phone_contact(update, context):
    id=update.message.from_user.id
    if db.check_user(id):
        db.add_user(id, update.message.contact.phone_number, update.message.contact.first_name)
        context.bot.send_message(id, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz. Admin ruxsat berishini kuting", reply_markup=ReplyKeyboardRemove())
    # Admin bazaga qo'shilgan bo'lishi kerak. Bo'lmasa xatolik beradi.
    context.bot.send_message(ADMIN, f"Sizdan foydalanuvchilar ruxsat so'ramoqda.\nName: {update.message.contact.first_name}\nNumber: {update.message.contact.phone_number}", reply_markup=post_btn)
    db.set_position(ADMIN,id)
    return STATE_POST

def admin_send_message(update, context):
    users=db.get_all_users()
    message_id=update.message.message_id
    j=0
    for i in users:
        try:
            context.bot.copy_message(i[0], ADMIN, message_id)
            j+=1
            if j==30:
                time.sleep(1)
                j=0
        except Exception as e:
            context.bot.send_message(ADMIN, f"Xabar yuborishda xatolik. {e}\n{i[0]}")
            continue

def take_comment(update, context):
    id=update.message.from_user.id
    text=update.message.text
    if len(text)>=2:
        context.bot.send_message(id, "Summani kiriting\nMisol:10 000/10000")
        db.add_money(id,update.message.from_user.first_name, text,db.get_position(id))
        return STATE_SUMA
    else:
        context.bot.send_message(id, "Commentni qatatdan kiriitng.")

def take_money(update, context):
    id=update.message.from_user.id
    text=update.message.text
    text=str(text).replace(" ",'')
    name=update.message.from_user.first_name
    if text.isnumeric():
        db.set_value(db.get_position(id),int(text))
        context.bot.send_message(id, "Bazaga qo'shildi.")
    else:
        context.bot.send_message(id, "Summani boshqatdan kiriting.\nSummadfa faqat sonlar bo'ladi!")
    