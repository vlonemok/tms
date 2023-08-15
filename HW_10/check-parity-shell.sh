#!/usr/bin/sh

numToCheck=$1

if [ $((numToCheck % 2)) -eq 0 ]; then
    echo "Число является четным"

elif [ $((numToCheck % 2)) -ne 0 ]; then
    echo "Число является нечетным"

else
    echo "Вы ввели неверное число"
    exit 1
fi
