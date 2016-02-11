#!/bin/bash
if [ ! -d "refdb" ]; then
  git clone https://github.com/percyliang/refdb
fi
cd refdb
git pull
cd ..
