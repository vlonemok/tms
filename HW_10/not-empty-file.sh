#!/bin/bash

[[ -p /dev/stdin ]] && {
	mapfile -t
	set -- "${MAPFILE[@]}"
}

for i in "$@"; do
	if test -s "$i"; then
		echo "$i"
	fi
done
