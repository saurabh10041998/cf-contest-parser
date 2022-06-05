#! /usr/bin/bash -e
cd $(pwd)
mkdir -p cf/contest/$1/$2
cd cf/contest/$1/$2
SCRIPT_PATH="/home/kali/codeforces/cf-contest-parser" ape.py $1 $2

