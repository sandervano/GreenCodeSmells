#!/bin/bash
Path=$1
Filename=$2
Arg=$3
java -classpath $Path $Filename $Arg > /dev/null 2>&1
