#!/bin/bash
echo "Мій PID: $$"
echo "Мій PPID: $PPID"
echo "Статус процесу:"
ps -p $$ -o pid,ppid,stat,ni,comm
