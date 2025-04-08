from core.ssh_client import VPS_LIST, run_task_on_vps
import random

async def simulate_load(ip): return random.randint(30, 90)

async def select_vps():
    available = []
    for vps in VPS_LIST:
        if await simulate_load(vps['ip']) < 75:
            available.append(vps)
        if len(available) == 5: break
    return available

async def run_balanced_task(ip, port, time, thread):
    selected = await select_vps()
    if not selected: return "⚠️ No VPS available."
    results = []
    for vps in selected:
        try:
            await run_task_on_vps(vps, ip, port, time, thread)
            results.append(f"{vps['ip']} ✅")
        except:
            results.append(f"{vps['ip']} ❌")
    return "\n".join(results)
