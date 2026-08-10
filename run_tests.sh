#!/bin/bash

./.venv/Scripts/python.exe -m pytest

pytest 

if [ $? -eq 0 ]; then
    exit 0 
else 
    exit 1
fi