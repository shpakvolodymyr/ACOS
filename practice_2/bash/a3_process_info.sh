#!/bin/bash
trap 'echo -e "\nОтримано сигнал! Робимо cleanup..."; exit 0' SIGINT SIGTERM

tick=1
while true; do
    echo "tick=$tick"
    ((tick++))
    sleep 1
done
