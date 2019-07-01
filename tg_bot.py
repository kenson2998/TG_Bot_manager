from telegram.ext.updater import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext.commandhandler import CommandHandler
import telegram.ext.filters
import time
import telegram

func_cmd = {'function': '', 'content': ''}
from TG_Config import welcome_content  # /start 说的话
import TG_Config as TG_Config  # TG_token 与管理员 设定
from bot_reply.bot_reply_funtion import do_reply  # 其他function
from record_message import record_message  # 記錄訊息
from speaker import welcome_message as wm  # 歡迎與創建userdata
from white_list_get import get_white_id as GWI  # 獲得白名單


def start(bot, update, *args):
    welcome_text = welcome_content.text1
    if args != ():
        welcome_text = args[0]
    custom_keyboard = [['/start'], ["查自己的TG ID", "提交管理员白名单"], ["DNS查询", "IP查询"], ["取消"]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id, text=welcome_text, parse_mode=telegram.ParseMode.MARKDOWN,
                     reply_markup=reply_markup)


def canceel(bot, update, content):
    close_text = "關閉了QA.Bot 查詢系統"
    if content != '取消':
        close_text = content
    reply_markup3 = telegram.ReplyKeyboardRemove()

    bot.send_message(chat_id=update.message.chat_id, text=close_text, parse_mode=telegram.ParseMode.MARKDOWN,
                     reply_markup=reply_markup3)


def echo(bot, update):
    msg = wm.Speaker(update)
    msg.welcome_message(bot)
    print('%s 說了:%s %s' % (msg.use_data['name'], msg.use_data['content'], msg.use_data['time']))
    white_ID = GWI.get_whitelist_id(msg.use_data['chat_id'])  # 是否為白名單
    if white_ID.T_or_F is True:
        print('此为白名单')
        file_name = '%s_白名单.csv' % time.strftime('%Y-%m-%d', time.localtime())
        record_message(msg, file_name)
    else:
        print('非白名单')
        file_name = '%s_非白名单.csv' % time.strftime('%Y-%m-%d', time.localtime())
        record_message(msg, file_name)
    do_reply(cmd=func_cmd, bot=bot, msg=msg, canceel=canceel, update=update, W_list=white_ID.W_list,
             id_path=white_ID.id_path, manager=TG_Config.manager_ID)


updater = Updater(TG_Config.bot_token)
dispatcher = updater.dispatcher
echo_handler = MessageHandler(Filters.all, echo)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
print('Run TG_Bot..')
updater.start_polling()
updater.idle()
