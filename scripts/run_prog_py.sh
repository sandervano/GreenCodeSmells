#!/bin/bash
cd $1
python3 ${2}.py $3 > /dev/null 2>&1
