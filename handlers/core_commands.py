
---

## 📁 `handlers/`

---

### `core_commands.py`
```python
from telegram import Update
from telegram.ext import ContextTypes
from core.task_runner import run_balanced_task
from core.ssh_client import VPS_LIST
from database.models import add_vps, remove_vps, list_resources
from utils.role_check import is_admin

async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 3:
        await update.message.reply_text("Usage: /run <ip> <port> <time>")
        return
    ip, port, time = context.args
    thread = "24"
    await update.message.reply_text("⏳ Running task...")
    result = await run_balanced_task(ip, port, time, thread)
    await update.message.reply_text(result)

async def add_vps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    ip, user, passwd = context.args
    add_vps(ip, user, passwd)
    await update.message.reply_text(f"✅ VPS added: {ip}")

async def remove_vps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    ip = context.args[0]
    remove_vps(ip)
    await update.message.reply_text(f"❌ VPS removed: {ip}")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    statuses = [f"{v['ip']} ✅" for v in VPS_LIST]
    await update.message.reply_text("🧠 VPS Status:\n" + "\n".join(statuses))

async def resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    stats = list_resources()
    await update.message.reply_text(f"🖥️ Resources:\n{stats}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if is_admin(uid):
        await update.message.reply_text("/run /addvps /removevps /resources /genkey /balancekey")
    else:
        await update.message.reply_text("/run /rckey /redeemr")
