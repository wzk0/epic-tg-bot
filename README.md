# e宝

> 一个获取Epic喜加一信息的简易tgbot

## 搭建

首先, 申请一个Telegram bot并获取token以备用.

打开已经安装过pip, python3的终端, 安装相关依赖:

```sh
pip3 install requests beautifulsoup4 pyTelegramBotAPI html5lib
```

clone此仓库:
```
git clone https://github.com/wzk0/epic-tg-bot
```

运行:
```
python3 bot.py
```

## 使用

/help - 获取帮助
/epic - 获取喜加一信息

## 其他

`epic.py`里是一个API, 爬的是`https://steamstats.cn/xi`.