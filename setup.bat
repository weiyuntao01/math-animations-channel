@echo off
echo Setting up Math Animations Project...

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete!
echo To start working:
echo   1. Run: venv\Scripts\activate
echo   2. Test: manim scenes\examples\first_animation.py FirstAnimation -pql
