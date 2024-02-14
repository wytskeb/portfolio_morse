#!/bin/bash

for PID in $(sudo lsof -nP | grep TCP | grep LISTEN | grep python | awk '{print $2'})
do
    sudo kill -9 $PID
done