#!/bin/bash

if [[ $1 ]]; then
        VALUE=$1
        echo "$VALUE"

elif [[ $VALUE ]]; then
        echo "$VALUE"

elif [[ $1 -eq "" ]] || [[ $VALUE -eq "" ]]; then
        echo "Вы ничего не ввели"

else
        echo "Вы ввели неверные данные"
        exit 1
fi
