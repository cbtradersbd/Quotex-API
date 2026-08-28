@echo off
title CB Traders BD - API Server
echo Starting 24/7 API Server...
python -m uvicorn src.core.engine:app --host 0.0.0.0 --port 8000 --reload
pause
