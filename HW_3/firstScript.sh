#!/bin/bash

free -h | awk '{ print $1, $4 }' | sed 's/total//g' | sed 's/shared/Свободная память/g' | sed 's/Gi/ Гб/g' | sed 's/Mem/ОЗУ/g' | sed 's/Swap/Свап/g'

echo ""

echo -n "Использование процессора: " 
sar -u 1 1 | awk '{ print $3 }' | sed 's/%user/CPU usage/g'

echo ""

echo -n "IP адрес: " && hostname -I
