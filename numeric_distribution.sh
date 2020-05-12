#!/bin/bash

file=$(ls -t ${1})

for i in $file
do
    python distrib_visualize.py "${i}" || exit
done
