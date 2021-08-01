from KanekiRobot.modules import ALL_MODULES
from KanekiRobot.modules.helper_funsc.chat_status import is_user_admin
from KanekiRobot.modules.helper_funsc.misc import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update

async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n✅ **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url=f"https://t.me/kanekisupport"
                    ),
                    InlineKeyboardButton(
                        "Created By", url=f"https://t.me/rizexx"
                    )
                ]
            ]
        )
   )

__command_list__ = [

    "reload",

]

__handlers__ = [

    RELOAD_HANDLER,

]
