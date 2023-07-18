#!/bin/bash

free -h | awk '{ print $1, $4 }' | sed 's/total//g' | sed 's/shared/Свободная память/g' | sed 's/Gi/ Гб/g' | sed 's/Mem/ОЗУ/g' | sed 's/Swap/Свап/g'

echo ""

echo "Использование процессора: " 
mpstat | awk '$12 ~ /[0-9.]+/ { print 100 - $12"%" }'

echo ""

echo "IP адрес: " && hostname -I
