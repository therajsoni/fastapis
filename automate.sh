#!/bin/bash 

python3 -m venv venv 

source ./venv/bin/activate 

pip install -r requirements.txt 

cd api 

uvicorn app:app --reload --port 5050