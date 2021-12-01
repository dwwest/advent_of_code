#!/usr/bin/env bash

set -eu

day=$1
year=$2
day_for_filename=$(printf "day_%02d" "$day")
mkdir -p "$year/$day_for_filename"
curl --cookie cookies.txt "https://adventofcode.com/"$year"/day/$day/input" -o "${year}/${day_for_filename}/input.txt"

