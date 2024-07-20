#!/bin/bash

echo "Hello"
pwd
uname -a

# マシン名を表示
echo "Hostname: $(hostname)"

# IPアドレスを表示
echo "IP Address: $(hostname -I | awk '{print $1}')"
