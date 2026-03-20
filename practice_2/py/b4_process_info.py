import subprocess
import signal
import time

print("Запуск sleep 100...")
proc = subprocess.Popen(["sleep", "100"])
print(f"PID: {proc.pid}")

time.sleep(1)
print("Надсилаємо SIGSTOP...")
proc.send_signal(signal.SIGSTOP)

time.sleep(2)
print("Надсилаємо SIGCONT...")
proc.send_signal(signal.SIGCONT)

time.sleep(2)
print("Надсилаємо SIGTERM (terminate)...")
proc.terminate()

proc.wait()
print(f"Процес завершився з кодом: {proc.returncode}")
