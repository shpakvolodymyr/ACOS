import os
import sys

child_pid = os.fork()

if child_pid == 0:
    os.execlp("bash", "bash", "-c", "echo 'Я дитина, зараз вийду з кодом 7'; exit 7")
else:
    print(f"Батько: Створено дитину з PID {child_pid}. Очікую...")
    pid, status = os.waitpid(child_pid, 0)
    exit_code = os.waitstatus_to_exitcode(status) 
    print(f"Батько: Дитина {pid} завершилася з кодом {exit_code}")
