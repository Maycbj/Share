#!/bin/bash
python receive.py &

sleep 8

python send.py &

wait

