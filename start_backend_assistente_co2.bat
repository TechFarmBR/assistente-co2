@echo off
cd /d "C:\Users\carme\Documents"
echo Iniciando servidor FastAPI...
start http://127.0.0.1:8000/docs
uvicorn backend_assistente_co2:app --reload
pause