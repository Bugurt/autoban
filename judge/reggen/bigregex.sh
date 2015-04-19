#!/bin/bash

while read line; do
	echo -e "($(./reggen.py $line)|\c";
done < blacklist.txt;

echo "[^\s\S])"
