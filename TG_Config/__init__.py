import os
from white_list_get import get_white_id as GWI  # 獲得白名單

files = os.path.dirname(os.path.abspath(__file__)) + '/'

with open(files + 'bot_token.txt', 'r') as token:
    bot_token = token.readline()

if not bot_token:
    print("还没有设定机器人token到/TG_Config/bot_token.txt")
else:
    print('已獲得api token:', bot_token)
with open(files + 'manager_ID.txt', 'r') as m_f:
    manager_ID = m_f.readline()
if not manager_ID:
    print("还没有设定管理员到/TG_Config/manager_ID.txt")
else:
    print('已獲得manager_ID:', str(manager_ID))

white_ID = GWI.get_whitelist_id(manager_ID)  # 是否為白名單

if white_ID.T_or_F is True:
    pass
else:
    print('管理员不在非白名单内 已自动帮你加入白名单')

    text2 = "%s,%s,%s\n" % ('白名单管理员', 'manager', manager_ID)
    id_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'/white_list_get/id.csv'
    with open(id_path, 'a', encoding='utf-8-sig') as f:
        f.write(text2)
