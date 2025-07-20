.PHONY: help setup test clean render

help:
@echo "Available commands:"
@echo "  setup      - Set up the development environment"
@echo "  test       - Run tests"
@echo "  clean      - Clean up generated files"
@echo "  render     - Render example scene"

setup:
python -m venv venv
venv\Scripts\activate && pip install -r requirements.txt

test:
pytest tests/

clean:
rmdir /s /q media 2>nul
del /q output\videos\*.mp4 2>nul

render:
manim scenes/examples/first_animation.py FirstAnimation -pql
