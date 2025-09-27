#!/usr/bin/env bash

mkdir -p benchmarks

#myfilesize=$(wc -c "../data/$1" | awk '{print $1}')

#/usr/bin/time -v .././main.py "../data/$1" "../data/output.json" 2> benchmarks/results.txt
/usr/bin/time -f "Elapsed_time: %e seconds CPU_kernel_time: %S seconds CPU_utilization: %P Max_RAM: %M Kb Exit_status: %x" .././main.py "../data/$1" "../data/output.json"