#!/usr/bin/env bash

mkdir -p benchmarks

dataset="test.csv"

/usr/bin/time -v .././main.py "../data/$dataset" "../data/output.json" 2> benchmarks/results.txt