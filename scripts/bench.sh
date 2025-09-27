#!/usr/bin/env bash

mkdir -p benchmarks

current_date_time="$(date '+%Y-%m-%d_%H-%M-%S')"

file_data=$(wc -lc "../data/$1" | awk '{print $1,$2}')

read number_lines file_size <<< "$file_data"

file_size_KiB="$(($file_size / 1024))"

metrics=$(/usr/bin/time -f "%e %S %P %M %x" .././main.py "../data/$1" "../data/output.json" 2>&1 >/dev/null)

read elapsed_time system_time cpu_utilization mem_kb exit_status <<< "$metrics"

kib_per_second=$(echo "scale=2; $file_size_KiB / $elapsed_time" | bc -l)
lines_per_second=$(echo "scale=2; $number_lines / $elapsed_time" | bc -l)

echo "Start: $current_date_time Dataset: $1 File_size: $file_size_KiB KiB Elapsed_time: $elapsed_time seconds Kib/s: $kib_per_second Kib/s Number_lines: $number_lines Lines_per_second: $lines_per_second CPU_kernel_time: $system_time seconds CPU_utilization: $cpu_utilization Max_RAM: $mem_kb Kb Exit_status: $exit_status" | tee -a "benchmarks/results.txt"