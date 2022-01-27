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
