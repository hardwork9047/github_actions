#!/bin/bash

echo "Hello"
pwd
uname -a

# マシン名を表示
echo "Hostname: $(hostname)"

# IPアドレスを表示
echo "IP Address: $(hostname -I | awk '{print $1}')"

# リポジトリの最新状態を取得
# echo "Pulling latest changes from git repository"
# git pull origin main

echo "Add comment from Ubuntu"