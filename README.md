# 九色防伪验证机器人 (JiuSeBot)

## 功能
- 输入 @账号 自动判断是否为官方账号
- /list 查看公开的官方账号
- /report 举报假冒账号

## 本地运行
```bash
pip install -r requirements.txt
python main.py
```

## Railway 部署
1. 登录 https://railway.app
2. New Project → Deploy from GitHub Repo → 选择本项目
3. 设置环境变量：
   - `BOT_TOKEN=你的Telegram Bot Token`
4. Done 🎉