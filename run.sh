echo "Starting main application"
poetry run uvicorn app.main:app --reload --port 8000