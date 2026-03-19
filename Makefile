.PHONY: help install dev-frontend dev-backend test clean docker-up docker-down

help:
	@echo "Available commands:"
	@echo "  make install        - Install all dependencies"
	@echo "  make dev-frontend   - Start frontend development server"
	@echo "  make dev-backend    - Start backend development server"
	@echo "  make test           - Run all tests"
	@echo "  make docker-up      - Start all services with Docker Compose"
	@echo "  make docker-down    - Stop all Docker services"
	@echo "  make clean          - Clean build artifacts and caches"

install:
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "Installing backend dependencies..."
	cd backend && python -m venv venv && . venv/bin/activate && pip install -r requirements.txt
	@echo "Dependencies installed!"

dev-frontend:
	cd frontend && npm run dev

dev-backend:
	cd backend && . venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	@echo "Running backend tests..."
	cd backend && . venv/bin/activate && pytest
	@echo "Running frontend tests..."
	cd frontend && npm test

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

clean:
	@echo "Cleaning build artifacts..."
	rm -rf frontend/node_modules frontend/.next frontend/out
	rm -rf backend/venv backend/__pycache__ backend/**/__pycache__
	rm -rf backend/.pytest_cache backend/htmlcov
	@echo "Clean complete!"
