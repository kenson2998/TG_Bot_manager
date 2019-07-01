''''
Speaker 用於整理TG回传的资料

welcome_message 为群组功能: 监听加入群组和离开踢除群组
欢迎语设定在 welcome_say.txt 里头定义
'''

class Speaker:
    def __init__(self, update):
        self.user_fullname = '%s %s' % (update.message.from_user.first_name, update.message.from_user.last_name)
        self.use_data = {'ID': update.message.from_user.id,  # 發話者ID
                         'name': self.user_fullname,  # 發話者姓名
                         'username': update.message.from_user.username,  # 發話者username
                         'content': update.message['text'],  # 發話者內容
                         'time': update.message.date.strftime("%Y-%m-%d %H:%M:%S"),  # 發話
                         'chat_id': update.message['chat']['id'],  # 發話的群組或私聊的id
                         'type': update.message['chat']['type'],  # 發送類型
                         'title': '私人訊息',  # 群組名字
                         'document': update.message.document,  # 發送的文件
                         'photo': update.message.photo,  # 發送的圖片
                         'sticker': update.message.sticker  # 發送的貼圖
                         }
        if update.message['chat']['type'] == 'group':
            self.use_data['title'] = update.message['chat']['title']
        self.message = update.message

    def welcome_message(self, bot):
        if self.message['new_chat_members'] != []:
            print('歡迎新人：%s' % self.message['new_chat_members'][0]['first_name'])
            bot.send_chat_action(chat_id=self.use_data['chat_id'], action=telegram.ChatAction.TYPING)
            say_text = '歡迎新人： @%s ' % self.message['new_chat_members'][0]['first_name']
            with open('welcome_say.txt', 'r', encoding='utf-8') as f:
                for i in f:
                    say_text += i
            bot.send_message(chat_id=self.use_data['chat_id'], text=say_text)

        if self.message['left_chat_member'] != None:
            print('很不幸 %s 被踢了' % self.message['left_chat_member']['first_name'])
            bot.send_message(chat_id=self.use_data['chat_id'],
                             text='很不幸 %s 被踢了' % self.message['left_chat_member']['first_name'])
