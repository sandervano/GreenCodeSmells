#!/bin/bash

File="../results/*"
for f in $File
do
    if [[ $f == *'figures' ]]; then
        continue
    fi
    Name="$f/*"
    if [[ -d "$f" ]]; then
        for g in $Name
        do
            if [[ -d "$g" ]]; then
                Path="${g#"../results/"}/"
                echo $Path
                python3 analyse.py $Path
            fi
        done
    fi
done
