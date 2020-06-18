#!/bin/bash

ProgScript=$1
Prefix=$2
Suffix=$3
num=$4

i=0
Path="../codebase/$Prefix"
for File in ${Path}/*$Suffix
do
  Filename=${File#"${Path}/"}
  Dir="../results/${Prefix}_${i}"
  mkdir -p $Dir

  if [[ $Filename == *'$'* ]]; then
     continue
  fi
  if [[ $Filename == *'smell'* ]]; then
    arg="$Dir/smell"
    i=$i+1
  else
    arg="$Dir/norm"
  fi

  ./experiment.sh run_prog_wait $num $Path ${Filename%$Suffix}  "wait_${arg}_0.csv"
  for j in $(seq 0 49)
  do
    ./experiment.sh $ProgScript $num $Path ${Filename%$Suffix}  "${arg}_${j}.csv"
  done
  ./experiment.sh run_prog_wait $num $Path ${Filename%$Suffix}  "wait_${arg}_1.csv"
done
