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
    else:
        return STATE_MONEY
    
def money(update, context):
    query=update.callback_query
    id=query.message.chat.id
    btn=query.data
    if btn=="main_menu":
        context.bot.send_message(id, "Quyidagi Menyulardan birini tanlang", reply_markup=main_btn)
    elif btn=='money':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=income)
        return STATE_MONEY
    elif btn=='report':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=statistics_btn)
        return STATE_REPORT
    elif btn=='come':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=type_income)
    elif btn=='terminal' or btn=="cash" or btn=="click":
        db.set_position(id, "come_"+str(btn))
        context.bot.send_message(id, "Qayerdan?🟢\nComment 💬")
    elif btn=='gone':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=type_outlay)
    
def report(update, context):
    query=update.callback_query
    id=query.message.chat.id
    btn=query.data
    if btn=="main_menu":
        context.bot.send_message(id, "Quyidagi Menyulardan birini tanlang", reply_markup=main_btn)
    elif btn=='money':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=income)
        return STATE_MONEY
    elif btn=='report':
        context.bot.send_message(id, "Quyidagi tuqmalardan birini tanlang", reply_markup=statistics_btn)
    elif btn=='day':
        context.bot.send_message(id, "Quyidagilardan birini tanlang.", reply_markup=type_outlay_report)
        db.set_position(id,btn)
    elif btn=='month':
        context.bot.send_message(id, "Quyidagilardan birini tanlang.", reply_markup=type_outlay_report)
        db.set_position(id,btn)
    elif btn=="academy":
        time=db.get_position(id)
        if time=="day":
            report=db.get_dayly()
            kirim, chiqim=0,0
            for i in report:
                if i[-1]=="gone_academy":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🔴""")
                    chiqim+=1
                elif i[-1]!="gone_personal":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🟢""")
                    kirim+=1
            context.bot.send_message(id, f"Kun davomida academiyada:\n{kirim} 🟢{db.get_dayly_income()}\n{chiqim} 🔴{db.get_dayly_expense_academy()}", reply_markup=prev)
        else:
            context.bot.send_message(id, "Oylik xisobot academiyada.")
            report=db.get_monthly()
            kirim, chiqim=0,0
            for i in report:
                if i[-1]=="gone_academy":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🔴""")
                    chiqim+=1
                elif i[-1]!="gone_personal":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🟢""")
                    kirim+=1
            context.bot.send_message(id, f"Oy davomida academiyada:\n{kirim} 🟢{db.get_monthly_income()}\n{chiqim} 🔴{db.get_monthly_expense_academy()}", reply_markup=prev)
    elif btn=="personal":
        time=db.get_position(id)
        if time=="day":
            report=db.get_dayly()
            kirim, chiqim=0,0
            for i in report:
                if i[-1]=="gone_personal":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🔴""")
                    chiqim+=1
                elif i[-1]!="gone_academy":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🟢""")
                    kirim+=1
            context.bot.send_message(id, f"Kun davomida shaxsiy:\n{kirim} 🟢{db.get_dayly_income()}\n{chiqim} 🔴{db.get_dayly_expense_personal()}", reply_markup=prev)
        else:
            context.bot.send_message(id, "Oylik xisobot shaxsiy.")
            report=db.get_monthly()
            kirim, chiqim=0,0
            for i in report:
                if i[-1]=="gone_personal":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🔴""")
                    chiqim+=1
                elif i[-1]!="gone_academy":
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🟢""")
                    kirim+=1
            context.bot.send_message(id, f"Oy davomida shaxsiy:\n{kirim} 🟢{db.get_monthly_income()}\n{chiqim} 🔴{db.get_monthly_expense_personal()}", reply_markup=prev)
    elif btn=="overall":
        time=db.get_position(id)
        if time=="day":
            report=db.get_dayly()
            kirim, chiqim=0,0
            for i in report:
                if str(i[-1]).startswith("gone"):
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🔴""")
                    chiqim+=1
                else:
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🟢""")
                    kirim+=1
            context.bot.send_message(id, f"Kun davomida Umumiy:\n{kirim} 🟢{db.get_dayly_income()}\n{chiqim} 🔴{db.get_dayly_expense()}", reply_markup=prev)
        else:
            context.bot.send_message(id, "Oylik xisobot Umumiy.")
            report=db.get_monthly()
            kirim, chiqim=0,0
            for i in report:
                if str(i[-1]).startswith("gone"):
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🔴""")
                    chiqim+=1
                else:
                    context.bot.send_message(id, f"""{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n🟢""")
                    kirim+=1
            context.bot.send_message(id, f"Oy davomida Umumiy:\n{kirim} 🟢{db.get_monthly_income()}\n{chiqim} 🔴{db.get_monthly_expense()}", reply_markup=prev)
    elif btn=="income":
        context.bot.send_message(id, f"Umumiy daromad 🟢\n{db.get_income()}", reply_markup=prev)
    elif btn=="expense":
        context.bot.send_message(id, f"Umumiy xarajat 🔴\n{db.get_expense()}",reply_markup=prev)
    elif btn=="benefit":
        context.bot.send_message(id, f"Umumiy Foyda \n{db.get_income()-db.get_expense()}",reply_markup=prev)
