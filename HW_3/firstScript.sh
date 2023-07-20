#!/bin/bash

free -h | awk '{ print $1, $4 }' | sed 's/total//g' | sed 's/shared/Свободная память/g' | sed 's/Gi/ Гб/g' | sed 's/Mem/ОЗУ/g' | sed 's/Swap/Свап/g'

echo ""

echo -n "Использование процессора: " 
mpstat | grep -A 5 "%idle" | tail -n 1 | awk '{ print 100 -  $ 12 }'

echo ""

echo -n "IP адрес: " && hostname -I
