import os
import subprocess

pid = os.getpid()
ppid = os.getppid()

print(f"Мій PID: {pid}")
print(f"Мій PPID: {ppid}")
print("Статус процесу:")
subprocess.run(["ps", "-p", str(pid), "-o", "pid,ppid,stat,ni,comm"])
