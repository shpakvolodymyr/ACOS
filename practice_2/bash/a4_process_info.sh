#!/bin/bash
sleep 100 &
PID=$!
echo "Запущено sleep 100 з PID: $PID"

echo "Надсилаємо SIGSTOP..."
kill -STOP $PID
ps -p $PID -o pid,stat,comm

echo "Чекаємо 2 секунди і надсилаємо SIGCONT..."
sleep 2
kill -CONT $PID
ps -p $PID -o pid,stat,comm

echo "Завершуємо через SIGTERM..."
kill -TERM $PID
wait $PID 2>/dev/null
echo "Процес вбито."
