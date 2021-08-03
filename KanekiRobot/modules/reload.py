
import importlib
import time
import re
from sys import argv
from typing import Optional

from KanekiRobot import (
    ALLOW_EXCL,
    CERT_PATH,
    DONATION_LINK,
    LOGGER,
    OWNER_ID,
    PORT,
    SUPPORT_CHAT,
    TOKEN,
    URL,
    WEBHOOK,
    SUPPORT_CHAT,
    dispatcher,
    StartTime,
    telethn,
    pbot,
    updater,
)

# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from KanekiRobot.modules import ALL_MODULES
from KanekiRobot.modules.helper_funsc.chat_status import is_user_admin
from KanekiRobot.modules.helper_funsc.misc import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown


@run_async
      filters.command("reload")
    & filters.group
    & ~ filters.edited
def get_reload(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            update.effective_message.reply_text(
                f"• `Bot berhasil dimulai ulang`\n\n• `Daftar admin telah diperbarui` {module.capitalize()}",
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


    RELOAD_HANDLER = DisableAbleCommandHandler("reload", reload)
CHANGE_RELOAD = CallbackQueryHandler(
    change_reload, pattern=r"reload_.*")
RELOAD_CHANGE = CallbackQueryHandler(
    change_quote, pattern=r"reload_.*")
dispatcher.add_handler(RELOAD_QUOTE)

__command_list__ = [

    "reload",

]

__handlers__ = [

    RELOAD_HANDLER,

]
