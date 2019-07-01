from function_search import FC
import telegram


def do_reply(**kwargs):
    cmd, bot, msg, cancel, update, manager = kwargs['cmd'], kwargs['bot'], kwargs['msg'], kwargs['canceel'], kwargs[
        'update'], kwargs['manager']

    content = msg.use_data['content']
    print(content)
    try:
        if content.count('.') > 1 and content[0].isdigit():
            cmd['content'] = msg.use_data['content']
            bot.send_message(chat_id=msg.use_data['chat_id'], text='嗯~這是IP的样子')
        if 'http' in content or 'www' in content:
            cmd['content'] = (content).replace('https://', '').replace('http://', '')
            bot.send_message(chat_id=msg.use_data['chat_id'], text='嗯~這是url的样子')
        if content == 'IP查询' or content == 'DNS查询':
            cmd['function'] = content
            bot.send_message(chat_id=msg.use_data['chat_id'],
                             text='提交的 %s :\n %s \n 請稍候～' % (cmd['function'], cmd['content']))
            bot.send_chat_action(chat_id=msg.use_data['chat_id'], action=telegram.ChatAction.TYPING)
            result_text = FC.func1(function=content, content=cmd['content'])
            bot.send_message(chat_id=msg.use_data['chat_id'], text='您提交的查询:%s\n %s' % (cmd['content'], result_text)
                             , parse_mode=telegram.ParseMode.MARKDOWN)
            cmd = {'function': '', 'content': ''}
        if len(msg.message['new_chat_members']) > 0 or msg.message['left_chat_member'] != None:
            msg.welcome_message(bot)
        if content == '取消':
            cancel(bot, msg, content)
        try:
            not_white(cmd=cmd, bot=bot, msg=msg, canceel=cancel, manager=manager)
        except:
            print('not_white error')
        try:
            join_white(cmd=cmd, bot=bot, msg=msg, canceel=cancel, W_list=kwargs['W_list'], id_path=kwargs['id_path'],
                       manager=manager)
        except:
            print('join_white error')

    except:
        print('bot_reply_function do reply error')


def join_white(**kwargs):
    cmd, bot, msg, cancel, manager = kwargs['cmd'], kwargs['bot'], kwargs['msg'], kwargs['canceel'], kwargs['manager']
    #####
    if msg.use_data['content'] == '加入白名單⭕':
        text1 = "%s,%s,%s\n" % (cmd['content'][0], cmd['content'][1], cmd['content'][2])
        print('tttttt', cmd)
        with open(kwargs['id_path'], 'a', encoding='utf-8-sig') as f:
            if str(cmd['content'][2]) in kwargs['W_list']:
                reply_text = '`%s` 单人已经在白名單囉' % msg.use_data['username']
            else:
                f.write(text1)
                reply_text = "已将 @%s:`%s` 加入白名单" % (msg.use_data['username'], msg.use_data['ID'])
            bot.send_message(chat_id=cmd['content'][2], text=reply_text, parse_mode=telegram.ParseMode.MARKDOWN)

        if cmd['content'][2] != cmd['content'][3]:
            text2 = "%s,%s,%s\n" % (cmd['content'][0], cmd['content'][1], cmd['content'][3])

            with open(kwargs['id_path'], 'a', encoding='utf-8-sig') as f:
                if str(cmd['content'][3]) in kwargs['W_list']:
                    reply_text = '群组名 %s \n使用者:@%s \n已经在白名單囉' % (cmd['content'][0],msg.use_data['username'])
                else:
                    f.write(text2)
                    reply_text = "已将 群组名:%s \n使用者: @%s \n加入白名单" % (cmd['content'][0],msg.use_data['username'])
                bot.send_message(chat_id=(cmd['content'][3]), text=reply_text, parse_mode=telegram.ParseMode.MARKDOWN)
        cancel(bot, msg, reply_text)

    #####
    if msg.use_data['content'] == '不加入白名單❌':
        reply_text = " @%s 白名单審核不通過" % msg.use_data['username']
        bot.send_message(chat_id=cmd['content'][3], text=reply_text, parse_mode=telegram.ParseMode.MARKDOWN)
        cancel(bot, msg, reply_text)


def not_white(**kwargs):
    cmd, bot, msg, cancel, manager = kwargs['cmd'], kwargs['bot'], kwargs['msg'], kwargs['canceel'], kwargs['manager']
    content = msg.use_data['content']

    #####
    if content == "查自己的TG ID":
        if msg.use_data['ID'] == msg.use_data['chat_id']:
            replys = "这是你的Telegram ID: `%s` \n " % msg.use_data['ID']
        else:
            replys = "这是你的Telegram ID: `%s` \n Group ID: `%s` \n Group name: `%s` " \
                     % (msg.use_data['ID'], msg.use_data['chat_id'], msg.use_data['title'])
        bot.send_message(chat_id=msg.use_data['chat_id'],
                         text=replys,
                         parse_mode=telegram.ParseMode.MARKDOWN)
    #####
    if content == "提交管理员白名单":
        txt = "@%s :`%s` 已送出提交,请管理员确认～ " % (msg.use_data['username'], msg.use_data['ID'])
        bot.send_message(chat_id=msg.use_data['chat_id'], text=txt, parse_mode=telegram.ParseMode.MARKDOWN)
        custom_keyboard = [["加入白名單⭕"], ["不加入白名單❌"]]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        cmd['content'] = [msg.use_data['title'], msg.use_data['name'], msg.use_data['ID'], msg.use_data['chat_id']]
        bot.send_message(chat_id=manager,
                         text="收到来自 @%s : `%s`,提交的白名单 " % (msg.use_data['username'], msg.use_data['ID']),
                         parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=reply_markup)
