@echo off
cd /d "C:\Users\carme\Downloads\assistente_co2"
set API_KEY=co2-4Zx8tA91K3rQp72N
start http://127.0.0.1:8000/docs
uvicorn backend_assistente_co2:app --reload
pause