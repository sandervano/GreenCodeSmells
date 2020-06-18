#!/bin/bash

# ./fannkuchredux.gpp-3.gpp_run 12
Path=$1
Filename=$2
Arg=$3

./${Path}/${Filename}.gpp_run $Arg > /dev/null 2>&1
