@echo off

python -m pip show beautifulsoup4 >nul 2>nul
if errorlevel 1 (
  python -m pip install beautifulsoup4
)

python -m pip show requests >nul 2>nul
if errorlevel 1 (
  python -m pip install requests
)

python sniper.py