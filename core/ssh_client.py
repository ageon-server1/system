import paramiko

VPS_LIST = []

async def setup_vps(vps):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(vps['ip'], username=vps['user'], password=vps['pass'])
    ssh.exec_command("cd freeroot && ./root.sh && cd M")
    ssh.close()

async def run_task_on_vps(vps, ip, port, time, thread):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(vps['ip'], username=vps['user'], password=vps['pass'])
    ssh.exec_command(f"cd M && ./run {ip} {port} {time} {thread}")
    ssh.close()
