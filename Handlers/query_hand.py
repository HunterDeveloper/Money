from const import *
from Buttons.inline_btn import *
from db_helper import DBUser
db=DBUser('Data_base.db')
def post(update, context):
    query=update.callback_query
    id=query.message.chat.id
    user=int(db.get_position(ADMIN))
    if query.data=="check":
        user=db.get_user()
        if user:
            context.bot.send_message(id,f"Name:{db.get_user_name(user)}\nPhone:{db.get_user_number(user)}", reply_markup=post_btn)
            db.set_position(id, user)
        else:
            context.bot.send_message(id,"Ruxsat so'raganlar yo'q.")
    if query.data=="allow":
        context.bot.send_message(user,"Ruxsat berildi. /start ni bosib foydalanishingiz mumkin")
        context.bot.send_message(id,"Ruxsat berildi.")
        db.set_position(user, "enter")
    elif query.data=='reject':
        context.bot.send_message(user,"Ruxsat berilmadi.")
        context.bot.send_message(id,"Rad etildi.")
        db.delete_user(user)

    # return STATE_NUMBER

# def ans_admin(update, context):
#     query=update.callback_query
#     id=query.message.chat.id
#     if query.data=='send_message':
#         context.bot.send_message(id, "Yubormoqchi bo'lgan xabaringizni yozing")
#         return STATE_SEND

#     elif query.data=="show_users":
#         context.bot.send_message(id, "Qaysi kategoriyadagi ma'lumotlarni ko'rmoqchisiz.", reply_markup=number_users)
#     elif query.data=="all":
#         context.bot.send_message(id, f"Umumiy foydalanuvchilar soni: {db.get_count_users()}")
#     else:
#         context.bot.send_message(id, f"Tanlagan kategoriyangizda mahsulotlar soni {db.get_count_category(query.data)}")


# def add_category_number(update, context):
#     query=update.callback_query
#     id=query.message.chat.id
#     context.bot.send_message(id,"Tanlagan kategoriyangizga qo'shmoqchi bo'lgan mahsulotingizni raqamini kiriting.")
#     db.set_position(id,query.data)
