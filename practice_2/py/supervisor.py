import subprocess
import time

MAX_RESTARTS = 3
restarts = 0

while restarts < MAX_RESTARTS:
    print(f"[Supervisor] Запуск worker.py (Спроба {restarts + 1} з {MAX_RESTARTS})")
    
    proc = subprocess.run(["python3", "worker.py"])
    
    print(f"[Supervisor] Worker завершився з кодом {proc.returncode}")
    restarts += 1
    time.sleep(1)

print("[Supervisor] Досягнуто ліміт перезапусків. Робота завершена.")
