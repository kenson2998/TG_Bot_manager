TG_Bot_manager
===

###### tags: `python3` `TG_BOT`

:::info
安装需要:
* python 3
* telegram bot API (python-telegram-bot==11.1.0)
* selenium==3.141.0

功能:
* /start 可編輯想顯示的訊息
* 查詢自己ID
* 白名單功能管理
* 查詢IP
* 查詢DNS
* 群組功能:
  * 主動歡迎新人
  * 被踢出後的回覆

:::

## 设定
TG_Config目錄下:
1.將機器人的`token` 貼到 bot_token.txt

2.將管理者的ID打上 manager_ID.txt

3.執行主程式 tg_bot.py

4.開始請打`/start` ,可以請bot_father 幫你加預設指令

![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/start.jpg)
## 5.查詢自己ID
![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/%E6%9F%A5ID.jpg)

## 6.管理白名單
設定好的管理者會單人訊息接收到加入白名單的要求

所以不會影響群組的GUI 只會單獨顯示在個人訊息上

![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/%E7%99%BD%E5%90%8D%E5%96%AE%E7%AE%A1%E7%90%861.jpg)
![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/%E7%99%BD%E5%90%8D%E5%96%AE%E7%AE%A1%E7%90%862.jpg)
![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/%E7%99%BD%E5%90%8D%E5%96%AE%E7%AE%A1%E7%90%863.jpg)
![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/%E7%99%BD%E5%90%8D%E5%96%AE%E7%AE%A1%E7%90%864.jpg)
## 7.消息管理
可接收訊息並依照日期和白名單、非白名單進行紀錄

![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/%E6%B6%88%E6%81%AF%E7%AE%A1%E7%90%86.jpg)
![](https://raw.githubusercontent.com/kenson2998/TG_Bot_manager/master/img/%E6%B6%88%E6%81%AF%E7%AE%A1%E7%90%862.jpg)