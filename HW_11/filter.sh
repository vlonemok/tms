#!/bin/bash

while getopts ":f:" opt; do
  case $opt in
    f)
      file="$OPTARG"
      ;;
    \?)
      echo "Неверный аргумент: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

shift $((OPTIND-1))
rule="$1"
shift

if [ -n "$file" ]; then
  lines=$(cat "$file")
else
  lines=$(cat)
fi

filter_lines() {
  local rule="$1"
  local token="$2"
  local lines="$3"

  case "$rule" in
    contains)
      echo "$lines" | grep "$token"
      ;;
    startswith)
      echo "$lines" | grep "^$token"
      ;;
    endswith)
      echo "$lines" | grep "$token$"
      ;;
    *)
      echo "Неверное правило: $rule. Поддерживаемые правила: contains, startswith, endswith." >&2
      exit 1
      ;;
  esac
}

filtered_lines=$(filter_lines "$rule" "$1" "$lines")

echo "$filtered_lines"