#!/bin/bash

file=$(ls -t ${1})

for i in $file
do
    python plot_bar.py "${i}" || exit
done
