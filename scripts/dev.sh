#!/bin/bash
PYTHONPATH=./api/src uvicorn api.src.main:app --host 0.0.0.0 --port 9000
