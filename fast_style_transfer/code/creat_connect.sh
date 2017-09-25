#!/bin/bash

python src/receive.py &

sleep 10

python src/send.py &

wait

