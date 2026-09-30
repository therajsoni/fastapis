#!/bin/bash 

apt install python3.12-venv

python3 -m venv venv 

source ./venv/bin/activate 

pip install -r requirements.txt 

cd api 

uvicorn app:app --reload --port 5050