import os
import sys

child_pid = os.fork()

if child_pid == 0:
    # Це код дочірнього процесу
    # Замінюємо поточний процес новим
    os.execlp("bash", "bash", "-c", "echo 'Я дитина, зараз вийду з кодом 7'; exit 7")
else:
    # Це код батьківського процесу
    print(f"Батько: Створено дитину з PID {child_pid}. Очікую...")
    pid, status = os.waitpid(child_pid, 0)
    # Зсуваємо біти, щоб отримати правильний код завершення
    exit_code = os.waitstatus_to_exitcode(status) 
    print(f"Батько: Дитина {pid} завершилася з кодом {exit_code}")
