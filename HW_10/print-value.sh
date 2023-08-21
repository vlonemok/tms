#!/bin/bash

if [[ $1 ]]; then
	VALUE=$1
	echo "$VALUE"

elif [[ $VALUE ]]; then
	echo "$VALUE"

else
	echo "Вы ввели неверные данные"
	exit 1
fi
