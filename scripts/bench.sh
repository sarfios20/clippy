#!/usr/bin/env bash

mkdir -p benchmarks

current_date_time="$(date '+%Y-%m-%d_%H-%M-%S')"

file_size=$(wc -c "../data/$1" | awk '{print $1}')
file_size_KiB="$(($file_size / 1024))"

#/usr/bin/time -v .././main.py "../data/$1" "../data/output.json" 2> benchmarks/results.txt

metrics=$(/usr/bin/time -f "%e %S %P %M %x" .././main.py "../data/$1" "../data/output.json" 2>&1 >/dev/null)

read elapsed_time system_time cpu_utilization mem_kb exit_status <<< "$metrics"

kib_per_second=$(($file_size_KiB / $elapsed_time))

echo "Start: $current_date_time Dataset: $1 File_size: $file_size_KiB KiB Elapsed_time: $elapsed_time Kib/s: $kib_per_second seconds CPU_kernel_time: $system_time seconds CPU_utilization: $cpu_utilization Max_RAM: $mem_kb Kb Exit_status: $exit_status"