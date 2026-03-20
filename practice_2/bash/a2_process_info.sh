#!/bin/bash

(sleep 2; exit 7) &
CHILD_PID=$!
echo "Запущено дочірній процес з PID: $CHILD_PID"

wait $CHILD_PID
echo "Дочірній процес завершився з кодом: $?"
