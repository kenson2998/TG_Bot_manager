import os


def record_message(msg, file_name, **kwargs):
    data_list = ['ID', 'username', 'name', 'title', 'chat_id', 'time', 'content', 'document', 'photo', 'sticker']
    title_list = ['id', '帐号显示名称', '使用者名称', '群組名称', 'group_id', '传送时间', '传送内容', '传送文件', '传送photo', '传送sticker']
    w_data, file_title = '', ''
    for i in data_list:
        w_data += str(msg.use_data[i]) + ','
    w_data = w_data[:-1] + '\n'
    for i in title_list:
        file_title += i + ','
    file_title = str(file_title[:-1]) + '\n'
    win_path = '%s\\%s' % (os.path.dirname(os.path.abspath(__file__)), file_name)
    mac_path = '%s/%s' % (os.path.dirname(os.path.abspath(__file__)), file_name)
    if os.path.exists(mac_path) is True or os.path.exists(win_path) is True:  # 今日白名单存在的话
        with open(file_name, 'a', encoding='utf-8-sig') as f:
            f.write(w_data)
    else:
        with open(file_name, 'a', encoding='utf-8-sig') as f:
            f.write(file_title)
            f.write(w_data)
