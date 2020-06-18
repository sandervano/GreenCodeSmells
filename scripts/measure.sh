#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10
do
      echo "doing $i"
      ./rapl_read/rapl-read >> results/test.txt
      echo "Time: $(date)" >> results/test.txt
      sleep 1
done
