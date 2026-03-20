import signal
import time
import sys

stop = False

def handler(signum, frame):
    global stop
    print(f"\n[Handler] Отримано сигнал {signum}. Готуємось до виходу...")
    stop = True

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

tick = 1
while not stop:
    print(f"tick={tick}")
    tick += 1
    time.sleep(1)

print("Робимо cleanup... Звільняємо ресурси... Вихід.")
sys.exit(0)
