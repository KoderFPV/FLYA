#!/bin/bash
source ./api/venv/bin/activate
PYTHONPATH=./api/src uvicorn --reload api.src.main:app --host 0.0.0.0 --port 9000
