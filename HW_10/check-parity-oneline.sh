#!/bin/bash

[[ $(($1 % 2)) -eq 0 ]] && echo "Число является четным" || echo "Число является нечетным"
