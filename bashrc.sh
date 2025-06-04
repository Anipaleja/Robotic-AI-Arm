#!/usr/bin/env bash

source ~/venv/bin/activate

cd ~/yrhacks || exit
git pull origin main

python3 main.py
