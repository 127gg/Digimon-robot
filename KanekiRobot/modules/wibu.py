import json
import requests
import html
import random
import time
from KanekiRobot import dispatcher
from KanekiRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async, CallbackQueryHandler
from KanekiRobot.modules.helper_funsc.chat_status import (is_user_admin)
from KanekiRobot.modules.helper_funsc.extraction import extract_user
from telegram import ParseMode, Update, InlineKeyboardMarkup, InlineKeyboardButton, replymarkup, ChatPermissions
from telegram.error import BadRequest

def wibu():
    url = "https://tede-api.herokuapp.com/api/asupan/wibu"
    # since text attribute returns dictionary like string
    response = requests.get(url)
    try:
        dic = json.loads(response.text)
    except Exception:
        pass
    wibu = dic["wibu"]
    wibu = dic["wibu"]
    asupan = dic["asupan"]
    return wibu, wibu, asupan
def asupan(update: Update, context: CallbackContext):
    message = update.effective_message
    wibu, wibu, asupan = wibu()
    msg = f"<i>❝{wibu}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="`Change`",
            callback_data="change_wibu")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )
def change_quote(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = update.effective_chat
    message = update.effective_message
    wibu, wibu, asupan = wibu()
    msg = f"<i>❝{wibu}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="`Change`",
            callback_data="wibu_change")]])
    message.edit_text(msg, reply_markup=keyboard,
                      parse_mode=ParseMode.HTML)
    
def wibu(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_vidio = message.reply_to_message.reply_vidio if message.reply_to_message else message.reply_vidio
    reply_vidio(
        random.choice(WIBU_VID))
WIBU_VID = (
      "https://telegra.ph/file/e5670f0f0470be68e4bd1.mp4"
      
      )    
WIBU_HANDLER = DisableAbleCommandHandler("wibu", wibu)
ASUPAN_HANDLER = DisableAbleCommandHandler("asupan", asupan)

CHANGE_WIBU = CallbackQueryHandler(
    change_quote, pattern=r"change_.*")
WIBU_CHANGE = CallbackQueryHandler(
    change_quote, pattern=r"quote_.*")
dispatcher.add_handler(CHANGE_WIBU)
dispatcher.add_handler(WIBU_CHANGE)
dispatcher.add_handler(WIBU_HANDLER)
dispatcher.add_handler(ASUPAN_HANDLER)

__command_list__ = [

    "wibu",
    "asupan"

]

__handlers__ = [

    WIBU_HANDLER,
    ASUPAN_HANDLER

]
