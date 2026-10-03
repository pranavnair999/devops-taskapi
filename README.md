# Task Manager API - End-to-End CI/CD with GitHub Actions

Flask REST API + pytest + Docker + GitHub Actions (CI) + GHCR + Render (CD).

Run locally: `pip install -r requirements.txt && python app.py`
Run tests:   `pytest --cov=app`
Docker:      `docker build -t taskapi . && docker run -p 5000:5000 taskapi`
