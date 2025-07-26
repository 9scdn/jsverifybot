# 九色防伪验证机器人 (JiuSeBot) for Render

## 功能
- 输入 @账号 自动判断是否为官方账号
- /list 查看公开的官方账号
- /report 举报假冒账号

## 在 Render 部署步骤
1. 登录 [https://render.com](https://render.com)
2. 创建 New Web Service
3. 连接 GitHub 或上传代码
4. 环境变量设置：
   - `BOT_TOKEN=你的 Telegram Bot Token`
5. Build Command:
   ```
   pip install -r requirements.txt
   ```
6. Start Command:
   ```
   python main.py
   ```