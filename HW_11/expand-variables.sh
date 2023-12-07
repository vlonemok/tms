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
key_value_pair="$*"

if [ -n "$file" ]; then
  template=$(cat "$file")
else
  template=$(cat)
fi

IFS=' ' read -ra vars <<< "$key_value_pair"
for var in "${vars[@]}"; do
  export "$var"
done

result=$(echo "$template" | envsubst)

echo "$result"